import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)


@pytest.mark.sanity
def test_dashboard_get(session, base_url):
    url = base_url + "/api/v2/dashboards"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_dashboard_get_cfxql(session, base_url):
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

def test_dashboard_get_cfxql_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "cfxql_query":"dashboard_type ~ 'negative'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_dashboard_get_search(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":"topology-details-app-template"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "topology-details-app-template"
    dashboard_names = [dashboard['name'] for dashboard in response_json['dashboards']]
    assert dashboard_names == ['topology-details-app-template']
    assert response_json["num_items"] != 0

def test_dashboard_get_search_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_dashboard_get_sort(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "sort":"name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['name']

    dashboard_names = [dashboard['name'] for dashboard in response_json['dashboards']]
    assert dashboard_names == sorted(dashboard_names)

def test_dashboard_get_sort_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "sort":"-negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

@pytest.mark.sanity
def test_dashboard_get_limit(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 10

    dashboards = response_json.get('dashboards', [])
    num_blueprints = len(dashboards)
    assert num_blueprints == 10

def test_dashboard_get_limit_negative(session, base_url):
    url = base_url + "/api/v2/dashboards"
    data = {
        "limit":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

@pytest.mark.sanity
def test_dashboard_check_if_exists(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    dashboard_names = [dashboard['name'] for dashboard in response_json['dashboards']]
    assert dashboard_names != f"{unique_id}_dashboard"
    assert response_json["num_items"] == 0


@pytest.mark.sanity
def test_dashboard_add(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_dashboard_added_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    dashboard_names = [dashboard['name'] for dashboard in response_json['dashboards']]
    assert dashboard_names == [f"{unique_id}_dashboard"]
    assert response_json["num_items"] != 0

def test_dashboard_added_verf_negative(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_dashboard_update(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_update_dashboard_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/negative_dashboard"
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
                        "label": "<center><h2>Platform API Automation Updated</h2></center>",
                        "min_width": 12,
                        "max_width": 12,
                        "height": 1
                    }
                ]
            }
        ]
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 400

@pytest.mark.sanity
def test_dashboard_updated_verf(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_dashboard_delete(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboards/dashboard/{unique_id}_dashboard"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_dashboard_delete_negative(session, base_url):
    url = base_url + f"/api/v2/dashboards/dashboard/negative_dashboard"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_dashboard_deleted_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboards"
    data = {
        "search":f"{unique_id}_dashboard"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dashboard"
    dashboard_names = [dashboard['name'] for dashboard in response_json['dashboards']]
    assert dashboard_names == []
    assert response_json["num_items"] == 0


'''  -------------------------- run all parameters ----------------------------------'''

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_dashboard_add_all_params(session, base_url, unique_id, name):
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
                "title": f"{name}_dashboard",
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_dashboard_get_search_all_params(session, base_url, name):
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
def test_dashboard_update_all_params(session, base_url, unique_id, name):
    url = base_url + f"/api/v2/dashboards/dashboard/{name}"
    data = {
    "dashboard_filters": {
        "columns_filter": [],
        "group_filters": [],
        "time_filter": True
    },
    "dashboard_pages": [],
    "dashboard_sections": [ {
                "title": f"{name}_dashboard",
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
    "description": "Updated-122334",
    "enabled": True,
    "label": "API testing dashboard Updated",
    "name": name,
    "status_poller": {},
    "version": "24.4.10.1"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)

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
def test_dashboard_delete_all_params(session, base_url, unique_id, name):
    url = base_url + f"/api/v2/dashboards/dashboard/{name}"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
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
def test_dashboard_deleted_verf_all_params(session, base_url, unique_id, name):
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
