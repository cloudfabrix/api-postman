import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_user_groups(session, base_url):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_org_data(session, base_url):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    global c_name, c_id, tenentId
    c_name = response_json["organizations"][0]["name"]
    c_id = response_json["organizations"][0]["id"]
    tenentId = response_json["organizations"][0]["parentResourceId"]

def test_add_user_group(session, base_url, unique_id):
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
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_msp_admin(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
    "chatbot_policy":"policy-update",
    "description":"MSP admin update",
    "name":f"{unique_id}_user_group",
    "profile":"msp-admin",
    "project_cfxql": f"customerName='{c_name}'",
    "selection_type": "cfxql_filter",
    "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_msp_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
    "chatbot_policy":"policy-update",
    "description":"MSP User update",
    "name":f"{unique_id}_user_group",
    "profile":"msp-user",
    "project_cfxql": f"customerName='{c_name}'",
    "selection_type": "cfxql_filter",
    "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_msp_user_read_only(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
    "chatbot_policy":"policy-update",
    "description":"MSP User Read Only update",
    "name":f"{unique_id}_user_group",
    "profile":"msp-user-read-only",
    "project_cfxql": f"customerName='{c_name}'",
    "selection_type": "cfxql_filter",
    "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_tenant_admin_profile(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {       
        "chatbot_policy": "policy update",
        "description": "Tenant admin update",
        "name": f"{unique_id}_user_group",
        "profile": "tenant-admin-profile",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_tenant_user_profile(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {       
        "chatbot_policy": "policy update",
        "description": "Tenant user update",
        "name": f"{unique_id}_user_group",
        "profile": "tenant-user-profile",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_tenant_user_read_only(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {       
        "chatbot_policy": "policy update",
        "description": "Tenant user read only update",
        "name": f"{unique_id}_user_group",
        "profile": "tenant-user-read-only",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_l3_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {       
        "chatbot_policy": "policy update",
        "description": "L3 user update",
        "name": f"{unique_id}_user_group",
        "profile": "l3-user",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_edit_usergroup_l1_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {       
        "chatbot_policy": "policy update",
        "description": "L1 user update",
        "name": f"{unique_id}_user_group",
        "profile": "l1-user",
        "selection_type": "tabular_report",
        "projects": [
            {
                "customerName": f"{c_name}",
                "customerId": f"{c_id}"
            }
        ],
        "tenantId":f"{tenentId}"
    }
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

def test_delete_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
        "tenantId":f"{tenentId}"
    }
    response = session.delete(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"