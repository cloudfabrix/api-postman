import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)

@pytest.mark.sanity
def test_usergroups_get(session, base_url):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_usergroups_get_org_data(session, base_url):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    global c_name, c_id, tenentId
    for org in response_json['organizations']:
        if org['name'] == 'OIA-CloudFabrix':
            c_name = org['customerName']
            c_id = org['customerId']
            tenentId = org['parentResourceId']
            break

@pytest.mark.sanity
def test_usergroups_add(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_usergroups_get_added(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response_json = response.json()
    response.raise_for_status()
    user_groups = response_json.get('user_groups', [])

    assert any(group['name'] == f'{unique_id}_user_group' for group in user_groups)

@pytest.mark.sanity
def test_usergroups_edit_msp_admin(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
  "profile": "msp-admin",
  "chatbot_policy": "policy-update",
  "tenantId": f"{tenentId}",
  "projects": [
    {
      "customerId": f"{c_id}",
      "customerName": f"{c_name}"
    }
  ],
  "selection_type": "tabular_report"
}

    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_msp_admin(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)
    if user_group and user_group.get('chatbot_policy') == 'policy-update':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_msp_user(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_msp_user(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'msp-user':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_msp_user_read_only(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_msp_user_read_only(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'msp-user-read-only':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_tenant_admin_profile(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_tenant_admin_profile(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'tenant-admin-profile':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_tenant_user_profile(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_tenant_user_profile(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'tenant-user-profile':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_tenant_user_read_only(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_tenant_user_read_only(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'tenant-user-read-only':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_l3_user(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_l3_user(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'l3-user':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_edit_l1_user(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_edit_l1_user(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response_json = response.json()
    response.raise_for_status()
    user_group = next((group for group in response_json.get('user_groups', []) if group['name'] == f'{unique_id}_user_group'), None)

    if user_group and user_group.get('profile') == 'l1-user':
        assert True
    else:
        assert False

@pytest.mark.sanity
def test_usergroups_delete(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    data = {
        "tenantId":f"{tenentId}"
    }
    response = session.delete(url, json=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_usergroups_get_deleted(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user_groups = response_json.get('user_groups', [])

    if any(group['name'] == f'{unique_id}_user_group' for group in user_groups):
        assert False