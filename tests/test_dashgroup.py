import time
import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_dashgroup(session, base_url):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dashboard_group_get_organizations(session, base_url):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    global c_name, c_id, tenentId
    for org in response_json['organizations']:
        if org['name'] == 'CloudFabrix-1':
            c_name = org['customerName']
            c_id = org['customerId']
            tenentId = org['parentResourceId']
            break

def test_dashboard_group_add_usergroup(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    data = {       
        "chatbot_policy": "policy",
        "description": "MSP admin Added",
        "name": f"{unique_id}_user_group",
        "profile": "msp-admin",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_dashboard_group_get_added_user_group(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response_json = response.json()
    response.raise_for_status()
    user_groups = response_json.get('user_groups', [])

    assert any(group['name'] == f'{unique_id}_user_group' for group in user_groups)

def test_dashboard_group_add_user(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": f"{unique_id}_user_group",
        "firstname": "test",
        "lastname": "api",
        "id": f"{unique_id}@cfx.com"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dashboard_group_get_user(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    email_address = f'{unique_id}@cfx.com'

    if not any(user['emailId'] == email_address for user in response_json.get('users', [])):
        assert False

def test_dashboard_group_get_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    email_address = f'negative@cfx.com'

    if not any(user['emailId'] == email_address for user in response_json.get('users', [])):
        assert True

def test_add_dashgroup(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    data = {
    "name": f"{unique_id}_dashboard_group",
    "label": "API testing dashboard",
    "userGroups": [
        {
    "tenantId": f"{tenentId}",
    "name": "{unique_id}_user_group",
    "role": "msp-admin",
    "profile": "msp-admin",
    "tags": [],
    "projects": f"{c_id}"
        }
    ],
    "dashboardList": [
        {
    "id": "user-dashboard-rda-artifact-dependencies-app",
    "name": "rda-artifact-dependencies-app"
        }
    ]
}
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dashgroup_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = f"{unique_id}_dashboard_group"
    is_dashboard_group_present = any(group['name'] == dashboard_group_name for group in data.get('dashboard_groups', []))
    assert is_dashboard_group_present
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()


def test_get_dashgroup_verf_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = f"negative_dashboard_group"
    is_dashboard_group_present = any(group['name'] == dashboard_group_name for group in data.get('dashboard_groups', []))
    assert not is_dashboard_group_present
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

def test_update_dashgroup(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/{unique_id}_dashboard_group"
    data = {  
   "description": "Edited_api_edited",
   "existing_dashboards": [
       "rda-artifact-dependencies-app"
   ],
   "label": "test_api_edited_api_edited",
   "name": f"{unique_id}_dashboard_group",
   "overwrite": True,
   "userGroups": [
       {
           "chatbot_policy": "",
           "name": "{unique_id}_user_group",
           "profile": "msp-admin",
           "project_cfxql": "",
           "projects": f"{c_id}",
           "role": "msp-admin",
           "tags": [],
           "tenantId": f"{tenentId}"
       }
   ],
   "dashboardList": [
        {
            "id": "user-dashboard-topology-details-with-static-first-column-and-graphdb",
            "name": "topology-details-with-static-first-column-and-graphdb"
        }
    ]
}

    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json['statusMessage'] == f"Dashboard Group {unique_id}_dashboard_group:test_api_edited_api_edited added successfully"

def test_update_dashgroup_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/negative_dashboard_group"
    data = {  
   "description": "Edited_api_edited",
   "existing_dashboards": [
       "rda-artifact-dependencies-app"
   ],
   "label": "test_api_edited_api_edited",
   "name": f"negative_dashboard_group",
   "overwrite": True,
   "userGroups": [
       {
           "chatbot_policy": "",
           "name": "{unique_id}_user_group",
           "profile": "msp-admin",
           "project_cfxql": "",
           "projects": f"{c_id}",
           "role": "msp-admin",
           "tags": [],
           "tenantId": f"{tenentId}"
       }
   ],
   "dashboardList": [
        {
            "id": "user-dashboard-topology-details-with-static-first-column-and-graphdb",
            "name": "topology-details-with-static-first-column-and-graphdb"
        }
    ]
}

    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json['statusMessage'] == f"Dashboard Group negative_dashboard_group:test_api_edited_api_edited added successfully"

def test_updated_dashgroup_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    # Extracting the relevant information
    dashboard_groups = data["dashboard_groups"]

    # Checking if the conditions are met
    for group in dashboard_groups:
        if group["name"] == f"{unique_id}_dashboard_group" and group["label"] == "test_api_edited_api_edited":
            assert True
            break
    else:
        assert False

    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()


def test_get_dashgroup_verf_update(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = f"{unique_id}_dashboard_group"
    is_dashboard_group_present = any(group['name'] == dashboard_group_name for group in data.get('dashboard_groups', []))

    assert is_dashboard_group_present
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_updated_dashgroup_verf_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = f"test_api_edited_api_edited"
    is_dashboard_group_present = any(group['label'] == dashboard_group_name for group in data.get('dashboard_groups', []))
    assert not is_dashboard_group_present
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dashgroup(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/{unique_id}_dashboard_group"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    #time.sleep(5)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json["statusMessage"] == "Group deleted successfully"

def test_delete_dashgroup_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/negative_dashboard_group"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    #time.sleep(5)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json["statusMessage"] == "Group deleted successfully"

def test_get_dashgroup_deleted_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = f"{unique_id}_dashboard_group"
    dashboard_groups = data.get("dashboard_groups", [])

    assert not any(dashgroup.get("name") == dashboard_group_name for dashgroup in dashboard_groups)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dashboard_group_deactivate_added_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dashboard_group_deactivate_added_user_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/negative@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

def test_dashboard_group_delete_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dashboard_group_deleted_users_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'{unique_id}@cfx.com'), None)
    if user:
        assert False

def test_dashboard_group_delete_added_usergroup(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
        "tenantId":f"{tenentId}"
    }
    response = session.delete(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_dashboard_group_deleted_user_groups_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user_groups = response_json.get('user_groups', [])

    if any(group['name'] == f'{unique_id}_user_group' for group in user_groups):
        assert False

'''  -------------------------- run all parameters ----------------------------------  '''

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_add_dashgroup_all_params(session, base_url, unique_id, name):
    url = base_url + "/api/v2/dashboard_groups"
    data = {
    "name": name,
    "label": "API testing dashboard",
    "userGroups": [
        {
    "tenantId": f"{tenentId}",
    "name": "{unique_id}_user_group",
    "role": "msp-admin",
    "profile": "msp-admin",
    "tags": [],
    "projects": f"{c_id}"
        }
    ],
    "dashboardList": [
        {
    "id": "user-dashboard-rda-artifact-dependencies-app",
    "name": "rda-artifact-dependencies-app"
        }
    ]
}
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_get_dashgroup_verf_all_params(session, base_url, unique_id, name):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = name
    is_dashboard_group_present = any(group['name'] == dashboard_group_name for group in data.get('dashboard_groups', []))
    assert is_dashboard_group_present
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_update_dashgroup_all_params(session, base_url, unique_id, name):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/{name}"
    data = {  
   "description": "Edited_api_edited",
   "existing_dashboards": [
       "rda-artifact-dependencies-app"
   ],
   "label": "test_api_edited_api_edited",
   "name": name,
   "overwrite": True,
   "userGroups": [
       {
           "chatbot_policy": "",
           "name": "{unique_id}_user_group",
           "profile": "msp-admin",
           "project_cfxql": "",
           "projects": f"{c_id}",
           "role": "msp-admin",
           "tags": [],
           "tenantId": f"{tenentId}"
       }
   ],
   "dashboardList": [
        {
            "id": "user-dashboard-topology-details-with-static-first-column-and-graphdb",
            "name": "topology-details-with-static-first-column-and-graphdb"
        }
    ]
}

    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json['statusMessage'] == f"Dashboard Group {name}:test_api_edited_api_edited added successfully"

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_get_updated_dashgroup_verf_all_params(session, base_url, unique_id, name):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    # Extracting the relevant information
    dashboard_groups = data["dashboard_groups"]

    # Checking if the conditions are met
    for group in dashboard_groups:
        if group["name"] == name and group["label"] == "test_api_edited_api_edited":
            assert True
            break
    else:
        assert False

    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()


@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_delete_dashgroup_all_params(session, base_url, name):
    url = base_url + f"/api/v2/dashboard_groups/dashboard_group/{name}"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    #time.sleep(5)
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"
    assert response_json["statusMessage"] == "Group deleted successfully"


@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data\sample'])
def test_get_dashgroup_deleted_verf_all_params(session, base_url, name):
    url = base_url + "/api/v2/dashboard_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    dashboard_group_name = name
    dashboard_groups = data.get("dashboard_groups", [])

    assert not any(dashgroup.get("name") == dashboard_group_name for dashgroup in dashboard_groups)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()