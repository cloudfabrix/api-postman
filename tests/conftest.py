import pytest
import time
import os
import requests
import logging.config
import yaml
import datetime

def setup_logging():
    with open('custom_logger.yaml', 'r') as config_file:
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
    dt_str = time.strftime("%Y_%m_%d_%H_%M_%S")
    html_file_name = "cfx_api_test_" + dt_str + ".html"
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
def unique_id():  # sourcery skip: inline-immediately-returned-variable
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d%H%M")
    uniqueID = f"test_api_{formatted_datetime}"
    return uniqueID

@pytest.fixture(scope="session")
def base_url(request):
    host = request.config.getoption("--host")
    return f"https://{host}"

@pytest.fixture(scope="session")
def api_session(base_url, username, password):
    # Create a session to maintain the connection
    session = requests.Session()

    try:
        # Define test data for POST request (login)
        post_data = {
            "user": username,
            "password": password
        }

        # Define headers
        headers = {
            'Content-Type': 'application/json'
        }

        # Perform login
        login_url = f"{base_url}/api/v2/login"
        response = session.post(login_url, json=post_data, headers=headers, verify=False)

        logger.info(f"----Login session----:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()

        yield session  # Provide the session object function to test functions

    finally:
        # Close the session when all tests are done
        session.close()
        logger.info("::::::SESSION CLOSED::::::")

def pytest_addoption(parser):
    parser.addoption("--host", action="store", required=True, default=None, help="Platform IP address")
    parser.addoption("--user", action="store", required=True, default=None, help="Platform username")
    parser.addoption("--password", action="store", required=True, default=None, help="Platform password")
    parser.addoption("--cleanup", action="store", default=False, help="Clean logs and reports")

@pytest.fixture(scope="session")
def host(request):
    return request.config.getoption("--host")

@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--user")

@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")
