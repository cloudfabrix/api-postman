import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_dashboard(session, base_url):
    url = base_url + "/api/v2/dashboards"
    response = session.get(url, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dashboard_cfxql(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "cfxql_query":"dashboard_type ~ 'app'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "app" in response_json["dashboards"][0]["dashboard_type"]

def test_get_dashboard_search(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":"topology-details-app-template"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "topology-details-app-template"
    assert response_json["num_items"] != 0

def test_get_dashboard_sort(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_dashboard_limit(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["limit"] == 10

def test_add_dashboard(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "name": f"{unique_id}_dashboard",
        "label": "API testing dashboard",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_cfxqls": {},
        "dashboard_sections": [
            {
                "title": f"{unique_id}_dashboard",
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

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_added_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    assert response_json["num_items"] != 0

def test_update_dashboard(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}_dashboard"
    data = {
        "name": f"{unique_id}_dashboard",
        "label": "API testing dashboard Updated",
        "description": "Dashboard",
        "enabled": True,
        "dashboard_cfxqls": {},
        "dashboard_sections": [
            {
                "title": f"{unique_id}_dashboard",
                "widgets": [
                    {
                        "widget_type": "label",
                        "label": "<center><h2>Platform API Automation Updated</h2></center>", #Changing the label.
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

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_updated_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    time.sleep(10)
    response = session.get(url, json=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "Updated" in response_json["dashboards"][0]["label"]

def test_delete_dashboard(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}_dashboard"
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(20)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_deleted_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    assert response_json["num_items"] == 0