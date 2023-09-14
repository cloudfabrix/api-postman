import pytest
import time
import os
import requests
import socket
from extras.reporting import CustomLogger

logger = CustomLogger().get_logger()

def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="10.95.110.144", help="API host IP address")
    parser.addoption("--user", action="store", default="admin@cfx.com", help="API username")
    parser.addoption("--password", action="store", default="admin1234", help="API password")
    parser.addoption("--cleanup", action="store_true", default=False, help="Clean logs and reports")

@pytest.fixture
def user(request):
    # Your fixture setup code here
    option = request.config.getoption("--user")
    yield option 

@pytest.fixture
def password(request):
    # Your fixture setup code here
    option = request.config.getoption("--password")
    yield option 

@pytest.fixture(scope="session")
def api_session(request):
    # Get command-line arguments
    hostip = request.config.getoption("--host")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    # Create a session to maintain the connection
    session = requests.Session()

    # Define test data for POST request (login)
    post_data = {
        "user": user,
        "password": password
    }

    # Define headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Perform login
    base_url = f"https://{hostip}"
    login_url = base_url + '/api/v2/login'
    response = session.post(login_url, json=post_data, headers=headers, verify=False)

    if response.status_code != 200:
        logger.error(f"Login failed with status code {response.status_code}:\n {response.text}")
    else:
        logger.info(f"::::::SESSION OPENED::::::")
        logger.info(f"Login Success with status code {response.status_code}:\n {response.text}")

    assert response.status_code == 200  # Adjust the expected status code as per your API
    
    yield session, base_url # Provide the session and base_url object function to test functions

    # Close the session when all tests are done
    session.close()
    logger.info(f"::::::SESSION CLOSED::::::")

# def pytest_html_report_title(report):
#     # Set the report title
#     report.title = "CFX API Automation Report"

# def pytest_cmdline_preparse(args):
#     global html_report_path
#     if not os.path.exists('./reports'):
#         os.makedirs('./reports')
#     dt_str = time.strftime("%Y_%m_%d_%H_%M_%S")
#     html_file_name = "cfx_api_test_" + dt_str + ".html"
#     html_report_path = "./reports/" + html_file_name
#     print(html_report_path)
#     args.extend(['--html', html_report_path])
#     args.extend(['--self-contained-html'])

# @pytest.fixture(scope="session", autouse=True)
# def cleanup(request):
#     cleanup_flag = request.config.getoption("--cleanup", default=False)

#     if cleanup_flag:
#         # Clear api_automation.log
#         if os.path.exists('api_automation.log'):
#             os.remove('api_automation.log')

#         # Clear all previous report.html files in the reports folder
#         reports_folder = 'reports'
#         if os.path.exists(reports_folder):
#             for filename in os.listdir(reports_folder):
#                 if filename.startswith("cfx_api_test_") and filename.endswith(".html"):
#                     file_path = os.path.join(reports_folder, filename)
#                     os.remove(file_path)

# # Default values for command-line arguments