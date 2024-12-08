import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)

@pytest.mark.sanity
def test_users_get_current(session, base_url):
    url = base_url + "/api/v2/current_user"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_get(session, base_url):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_get_organizations(session, base_url):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    global c_name, c_id, tenentId
    c_name = response_json["organizations"][0]["name"]
    c_id = response_json["organizations"][0]["id"]
    tenentId = response_json["organizations"][0]["parentResourceId"]

@pytest.mark.sanity
def test_users_add_usergroup(session, base_url, unique_id):
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
def test_users_get_added_user_group(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response_json = response.json()
    response.raise_for_status()
    user_groups = response_json.get('user_groups', [])

    assert any(group['name'] == f'{unique_id}_user_group' for group in user_groups)

@pytest.mark.sanity
def test_users_add_user(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_users_get_added(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    email_address = f'{unique_id}@cfx.com'

    if not any(user['emailId'] == email_address for user in response_json.get('users', [])):
        assert False

def test_users_add_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": f"{unique_id}_user_group",
        "firstname": "negative-",
        "lastname": "api",
        "id": f"12@#45@cfx.com"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

def test_users_add_user_unknown_usergroup_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": "unkonw_user_group",
        "firstname": "test1234",
        "lastname": "t",
        "id": "unknown_user_group@cfx.com"
        }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    assert response.status_code == 409

@pytest.mark.sanity
def test_users_deactivate_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_deactivate_status(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    response_json = response.json()
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'{unique_id}@cfx.com'), None)
    if not user.get('status') == 'Suspended':
        assert False

def test_users_deactivate_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unknow@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.status_code == 404
    
@pytest.mark.sanity
def test_users_activate_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_activate_status(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    response_json = response.json()
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'{unique_id}@cfx.com'), None)
    if not user.get('status') == 'Active':
        assert False

def test_users_activate_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unknow@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

@pytest.mark.sanity
def test_users_change_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": f"{unique_id}_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_change_unknown_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": "test_unknown_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

@pytest.mark.sanity
def test_users_change_user_group_unknow_user(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unkonwn@cfx.com/group"
    data = {
        "group": "test_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 500

@pytest.mark.sanity
def test_users_deactivate_added_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_deactivate_negative_added_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/unknown_user_group@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

@pytest.mark.sanity
def test_users_get_deactivated_users(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    response_json = response.json()
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'{unique_id}@cfx.com'), None)
    if not user and user.get('status') == 'Suspended':
        assert False

@pytest.mark.sanity
def test_users_get_deactivated_unknown_users_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    response_json = response.json()
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'unknown_user_group@cfx.com'), None)
    assert user == None

@pytest.mark.sanity
def test_users_delete_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_users_get_deleted_users(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'{unique_id}@cfx.com'), None)
    if user:
        assert False

@pytest.mark.sanity
def test_users_get_deleted_unknown_users_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'unknown_user_group@cfx.com'), None)
    if user:
        assert False

@pytest.mark.sanity
def test_users_delete_added_usergroup(session, base_url, unique_id):
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
def test_users_get_deleted_usergroup(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    user = next((user for user in response_json.get('users', []) if user['emailId'] == f'test_user{unique_id}@cfx.com'), None)
    if user:
        assert False
