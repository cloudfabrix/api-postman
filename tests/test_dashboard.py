import time
from tests.conftest import logging
import pytest

logger = logging.getLogger(__name__)

def test_get_dashboard(session, base_url):
    url = base_url + "/api/v2/dashboards"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dashboard_cfxql(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "cfxql_query":"dashboard_type ~ 'app'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "app" in response_json["dashboards"][0]["dashboard_type"]

def test_get_dashboard_cfxql_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "cfxql_query":"dashboard_type ~ 'negative'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

def test_get_dashboard_search(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":"topology-details-app-template"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "topology-details-app-template"
    assert response_json["num_items"] != 0

def test_get_dashboard_search_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

def test_get_dashboard_sort(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_dashboard_sort_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "sort":"-negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

def test_get_dashboard_limit(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 10

def test_get_dashboard_limit_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "limit":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

def test_add_dashboard(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
  "dashboard_filters": {
    "columns_filter": [],
    "group_filters": [],
    "time_filter": True
  },
  "dashboard_pages": [],
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
        ],
  "dashboard_style": "tabbed",
  "dashboard_type": "app",
  "description": "test",
  "enabled": True,
  "label": "API testing dashboard",
  "name": f"{unique_id}_dashboard",
  "status_poller": {},
  "version": "24.4.10.1"
}
    
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_added_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    assert response_json["num_items"] != 0

def test_added_dashboard_verf_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"negative_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"negative_dashboard"
    assert response_json["num_items"] == 0

def test_update_dashboard(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}_dashboard"
    data = {
    "dashboard_filters": {
        "columns_filter": [],
        "group_filters": [],
        "time_filter": True
    },
    "dashboard_pages": [],
    "dashboard_sections": [ {
                "title": f"{unique_id}_dashboard",
                "widgets": [
                    {
                        "widget_type": "label",
                        "label": "<center><h2>API Automation Updated</h2></center>",
                        "min_width": 12,
                        "max_width": 12,
                        "height": 1
                    }
                ]
            }],
    "dashboard_style": "tabbed",
    "dashboard_type": "app",
    "description": "Updated",
    "enabled": True,
    "label": "API testing dashboard Updated",
    "name": f"{unique_id}_dashboard",
    "status_poller": {},
    "version": "24.4.10.1"
    }
    
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

# def test_update_dashboard_negative(session, base_url, unique_id):
#     url = base_url + f"/api/v2/dashboards/dashboard/negative_dashboard"
#     data = {
#         "name": f"{unique_id}_dashboard",
#         "label": "API testing dashboard Updated",
#         "description": "Dashboard",
#         "enabled": True,
#         "dashboard_cfxqls": {},
#         "dashboard_sections": [
#             {
#                 "title": f"{unique_id}_dashboard",
#                 "widgets": [
#                     {
#                         "widget_type": "label",
#                         "label": "<center><h2>Platform API Automation Updated</h2></center>", #Changing the label.
#                         "min_width": 12,
#                         "max_width": 12,
#                         "height": 1
#                     }
#                 ]
#             }
#         ]
#     }
#     response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
#     time.sleep(15)
#     logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
#     assert response.status_code == 400

def test_updated_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "Updated" in response_json["dashboards"][0]["label"]

def test_delete_dashboard(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}_dashboard"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_delete_dashboard_negative(session, base_url):
    url = base_url + f"/api/v2/dashboards/dashboard/negative_dashboard"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_deleted_dashboard_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    assert response_json["num_items"] == 0


'''  -------------------------- run all parameters ----------------------------------'''

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_add_dashboard_all_params(session, base_url, unique_id, name):
    url = base_url + "/api/v2/dashboards"
    data = {
  "dashboard_filters": {
    "columns_filter": [],
    "group_filters": [],
    "time_filter": True
  },
  "dashboard_pages": [],
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
        ],
  "dashboard_style": "tabbed",
  "dashboard_type": "app",
  "description": "test",
  "enabled": True,
  "label": "API testing dashboard",
  "name": name,
  "status_poller": {},
  "version": "24.4.10.1"
}
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_get_dashboard_search_all_params(session, base_url, name):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":name
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == name
    assert response_json["num_items"] != 0

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_update_dashboard_all_params(session, base_url, unique_id, name):
    url = base_url + f"/api/v2/dashboards/dashboard/{name}"
    data = {
    "dashboard_filters": {
        "columns_filter": [],
        "group_filters": [],
        "time_filter": True
    },
    "dashboard_pages": [],
    "dashboard_sections": [ {
                "title": f"{unique_id}_dashboard",
                "widgets": [
                    {
                        "widget_type": "label",
                        "label": "<center><h2>API Automation Updated</h2></center>",
                        "min_width": 12,
                        "max_width": 12,
                        "height": 1
                    }
                ]
            }],
    "dashboard_style": "tabbed",
    "dashboard_type": "app",
    "description": "Updated",
    "enabled": True,
    "label": "API testing dashboard Updated",
    "name": name,
    "status_poller": {},
    "version": "24.4.10.1"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'
])
def test_delete_dashboard_all_params(session, base_url, unique_id, name):
    url = base_url + f"/api/v2/dashboards/dashboard/{name}"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'
])
def test_deleted_dashboard_verf_all_params(session, base_url, unique_id, name):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":name
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == name
    assert response_json["num_items"] == 0

