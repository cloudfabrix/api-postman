import pytest
import time
import os
import requests
import logging.config
import yaml
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import paramiko
import base64
import subprocess

def setup_logging():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    yaml_file_path = os.path.join(script_dir, 'custom_logger.yaml')
    with open(yaml_file_path, 'r') as config_file:
        config = yaml.safe_load(config_file)
        logging.config.dictConfig(config)

setup_logging()

logger = logging.getLogger(__name__)

def pytest_html_report_title(report):
    report.title = "CFX API Automation Report"

def pytest_cmdline_preparse(args):
    global html_report_path, html_file_name
    if not os.path.exists('./reports'):
        os.makedirs('./reports')
    dt_str = time.strftime("%Y%m%d_%H%M")
    html_file_name = "API_" + dt_str + ".html"
    html_report_path = "./reports/" + html_file_name
    print(html_report_path)
    args.extend(['--html', html_report_path])
    args.extend(['--self-contained-html'])

@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    cleanup_flag = request.config.getoption("--cleanup", default=False)
    
    if cleanup_flag:
        # Clear api_automation.log
        if os.path.exists('api_automation.log'):
            os.remove('api_automation.log')

        # Clear all previous report.html files in the reports folder
        reports_folder = 'reports'
        if os.path.exists(reports_folder):
            for filename in os.listdir(reports_folder):
                if filename.startswith("cfx_api_test_") and filename.endswith(".html"):
                    file_path = os.path.join(reports_folder, filename)
                    os.remove(file_path)

@pytest.fixture(scope="session")
def unique_id(): 
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
    return f"test_api_{formatted_datetime}"

@pytest.fixture(scope="session")
def base_url(request):
    host = request.config.getoption("--host")
    return f"https://{host}"

@pytest.fixture(scope="session")
def session(base_url, username, password, reset_password):
    # Create a session to maintain the connection
    session = requests.Session()
    admin_session = requests.Session()
    try:
        login_data = {
            "user": username,
            "password": password
        }
        headers = {
            'Content-Type': 'application/json'
        }

        if reset_password:
            reset_pswd = {
            "new_password": "admin1234",
            "confirm_password": "admin1234"
        }
            admin_login_url = base_url + "/api/v2/login"
            admin_login_response = admin_session.post(admin_login_url, json=login_data, headers=headers, verify=False, timeout=60)
            logger.info(f"---- API Log ---- {admin_login_url}:::{admin_login_response.status_code}::::{admin_login_response.text}")
            admin_login_response.raise_for_status()
            
            reset_pswd_url = base_url + "/api/v2/users/resetpassword"
            reset_pswd_response = admin_session.post(reset_pswd_url, json=reset_pswd, headers=headers, verify=False, timeout=60)
            logger.info(f"----API Log---- {reset_pswd_url}:::{reset_pswd_response.status_code}::::\n{reset_pswd_response.text}")
            reset_pswd_response.raise_for_status()
            logger.info("::::::RESET PASSWORD SUCCESSFULL::::::")
        
        login_url = f"{base_url}/api/v2/login"
        response = session.post(login_url, json=login_data, headers=headers, verify=False)
        logger.info(f"----Login session----:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()
        org_creation(base_url, session)
        yield session
    finally:
        session.close()
        logger.info("::::::SESSION CLOSED::::::")

def org_creation(base_url, session):
    # check if the org exists
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()
    organizations = data.get('organizations', [])
    found = False
    for org in organizations:
        if org.get('name') == 'OIA-CloudFabrix':
            found = True
            break

    if not found:
        # org creation
        org_url = f"{base_url}/api/v2/organizations"
        data = {
        "description": "Description",
        "name": "OIA-CloudFabrix",
        "tag": "CFX"
        }
        response = session.post(org_url, json=data, headers=session.headers, verify=False, timeout=60)
        logger.info(f"----API Log---- {org_url}:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()

def pytest_addoption(parser):
    parser.addoption("--host", action="store", required=True, default=None, help="Platform IP address")
    parser.addoption("--user", action="store", required=True, default=None, help="Platform username")
    parser.addoption("--password", action="store", required=True, default=None, help="Platform password")
    parser.addoption("--cleanup", action="store_true", default=False, help="Clean logs and reports")
    parser.addoption("--reset-password", action="store_true", default=False, help="reset admin password")
    parser.addoption("--post-to-slack", action="store_true", default=False, help="Use when want post the test results to slack")
    parser.addoption("--slack-channel", default=None, help="Enter slack channel id to post test results in slack")
    parser.addoption("--description", default='No_description_provided', help="Enter description for execution! Ex: OIA, AIA, OIA_Sanity & AIA_Sanity")
    parser.addoption("--automation-user", default='CFX_name', help="Enter Executer Name")

@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")

@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--user")

@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")

@pytest.fixture(scope="session")
def reset_password(request):
    return request.config.getoption("--reset-password")

@pytest.fixture(scope="session")
def post_to_slack(request):
    return request.config.getoption("--post-to-slack")

@pytest.fixture(scope="session")
def slack_channel(request):
    return request.config.getoption("--slack-channel")

@pytest.fixture(scope="session")
def description(request):
    return request.config.getoption("--description")

@pytest.fixture(scope="session")
def automation_user(request):
    return request.config.getoption("--automation-user")

def pytest_configure(config):
    raw_description = str(config.getoption('--description'))
    description = raw_description.replace("_", " ").split()
    final_description = " ".join(description)
    config._metadata["Execution Description"] = final_description
    config._metadata["Slack Channel"] = config.getoption('--slack-channel')
    if config.getoption("--automation-user") is not None:
        config._metadata["Automation Ran By"] = config.getoption('--automation-user')

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    global total_testcases, pass_count, fails_count, pass_percentage
    total_testcases = len(session.items)
    reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    passed = reporter.stats.get('passed', [])
    pass_count = len(passed)
    fails_count = total_testcases - pass_count
    pass_percentage = (pass_count / total_testcases) * 100
    
    # print("Total_Testcases"+total_testcases, "Passed_Count"+pass_count, "Failed_Count"+fails_count, "Pass_Percentage"+pass_percentage)
    # commented as the could'nt push the commit with slack API token key
    client = """###"""
    channel_id = str(session.config._metadata["Slack Channel"])
    post_to_slack = session.config.getoption("--post-to-slack")
    print(post_to_slack)
    if post_to_slack == True:
        try:
            # Call the conversations.list method using the WebClient
            result = client.chat_postMessage(
                channel=channel_id,
                text="Automation Report",
                blocks=[
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "RDAF Platform APIs Automation Results",
                        },
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Automation Ran By:*\n{}".format(str(session.config._metadata["Automation Ran By"]))
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Git Branch:*\n{}".format(str(get_current_branch_name()))
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Testcases Collected:*\n{}".format(
                                    str(total_testcases)
                                ),
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Pass Percentage:*\n{}".format(
                                    str(pass_percentage)
                                ),
                            },
                        ],
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Testcases Failed:*\n{}".format(
                                    str(fails_count)
                                ),
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Testcases Passed:*\n{}".format(
                                    str(pass_count)
                                ),
                            },
                        ],
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*Execution Description:*\n{}".format(
                                str(session.config._metadata["Execution Description"])
                            ),
                        },
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Detailed Report",
                                },
                                "value": "click_me_123",
                                "url": "{}".format(
                                    'http://10.95.159.105/automation_reports/'
                                    + html_file_name
                                ),
                            }
                        ],
                    },
                ],
            )
            # Print result, which includes information about the message (like TS)
            logger.info(result)

        except SlackApiError as e:
            logger.error(f"Error: {e}")

def get_current_branch_name():
    try:
        branch_name = os.environ.get("GIT_BRANCH")
        if not branch_name:
            branch_name = subprocess.check_output(["git", "symbolic-ref", "--short", "HEAD"], text=True).strip()
        return branch_name
    except subprocess.CalledProcessError:
        return None

def decode(encoded_data):
    decoded_bytes = base64.b64decode(encoded_data)
    return decoded_bytes.decode('utf-8')

def transfer_html_report(html_file_path):
    centos_host = "10.95.159.105"
    centos_username = decode('cm9vdA==')
    centos_password = decode('YWJjZDEyMyQ=')
    destination_path = "/var/www/html/automation_reports/"
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=centos_host, username=centos_username, password=centos_password)
        sftp_client = ssh_client.open_sftp()
        sftp_client.put(html_file_path, f"{destination_path}/{os.path.basename(html_file_path)}")
        sftp_client.close()
        print(f"HTML Report transferred successfully to {centos_host}")
        return True
    except Exception as e:
        print(f"Error occurred during file transfer: {e}")
        return False
    finally:
        ssh_client.close()

def pytest_unconfigure(config):
    post_to_slack_value = config.getoption("--post-to-slack")
    if post_to_slack_value:
        transfer_html_report(html_report_path)