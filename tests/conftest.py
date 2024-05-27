import pytest
import time
import os
import requests
import logging.config
import yaml
import datetime

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
    global html_report_path
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
        if org.get('name') == 'CloudFabrix-1':
            found = True
            break

    if not found:
        # org creation
        org_url = f"{base_url}/api/v2/organizations"
        data = {
    "description": "Description",
    "name": "CloudFabrix-1",
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