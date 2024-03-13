import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_current_user(session, base_url):
    url = base_url + "/api/v2/current_user"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_users(session, base_url):
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_organizations(session, base_url):
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

def test_add_usergroup(session, base_url, unique_id):
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

def test_add_user(session, base_url, unique_id):
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

def test_add_user_negative(session, base_url, unique_id):
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
    assert response.status_code == 409

def test_add_user_unkonw_usergroup(session, base_url):
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": "unkonw_user_group",
        "firstname": "test1234",
        "lastname": "t",
        "id": "test_user1234@cfx.com"
        }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 500

def test_deactivate_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_deactivate_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unknow@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.status_code == 404
    
def test_activate_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_activate_user_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unknow@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

def test_change_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": f"{unique_id}_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_change_unknown_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": "test_unknown_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

def test_change_user_group_unknow_user(session, base_url, unique_id):
    url = base_url + "/api/v2/users/user/unkonwn@cfx.com/group"
    data = {
        "group": "test_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 500

def test_deactivate_added_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_added_usergroup(session, base_url, unique_id):
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
    