import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_metadata_dashboard(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/dashboards"
    data = {
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_post_add_dashboard(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + "/api/v2/dashboards"
    data = {
        "name": unique_id,
        "label": "API testing dashboard",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_filters": {},
        "dashboard_sections": [
            {
                "title": unique_id,
                "widgets": [
                    {
                        "widget_type": "label",
                        "label": "<center><h2>API Automation</h2></center>",
                        "min_width": 12,
                        "max_width": 12,
                        "height": 1
                    }
                ]
            }
        ]
    }
    response = session.post(url, json=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_put_update_dashboard_data(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}"
    data = {
        "name": unique_id,
        "label": "API testing dashboard",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_filters": {},
        "dashboard_sections": [
            {
                "title": unique_id,
                "widgets": [
                    {
                        "widget_type": "label",
                        "label": "<center><h2>Platform API Automation</h2></center>", #Changing the label.
                        "min_width": 12,
                        "max_width": 12,
                        "height": 1
                    }
                ]
            }
        ]
    }
    time.sleep(10)
    response = session.put(url, json=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dashboard(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}"
    time.sleep(10)
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
