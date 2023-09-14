from extras.reporting import CustomLogger

import time

logger = CustomLogger().get_logger()

def test_GET_metadata_dashboard(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/dashboards"
    data = {
        "cfxql_query":"*",
        "search":"",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_POST_add_dashboard(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/dashboards"
    data = {
        "name": "test_api_dashboard9",
        "label": "API testing dashboard",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_filters": {},
        "dashboard_sections": [
            {
                "title": "test_api_example",
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
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_PUT_update_dashboard_data(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/dashboards/dashboard/test_api_dashboard9"
    data = {
        "name": "test_api_dashboard9",
        "label": "API testing dashboard",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_filters": {},
        "dashboard_sections": [
            {
                "title": "test_api_example",
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
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

