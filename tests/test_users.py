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

def test_add_user(session, base_url, unique_id):
    
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": "test_user_group",
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
        "group": "test_user_group",
        "firstname": "test",
        "lastname": "api",
        "id": f"{unique_id}@cfx.com"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 409

def test_add_user_unkonw_usergroup(session, base_url, unique_id):
    
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
    assert response.status_code == 409

def test_deactivate_user(session, base_url, unique_id):
    
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_deactivate_user_negative(session, base_url, unique_id):
    
    url = base_url + f"/api/v2/users/user/unknow@cfx.com/status"
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
    url = base_url + f"/api/v2/users/user/unknow@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    assert response.status_code == 404

def test_change_user_group(session, base_url, unique_id):
    
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": "test_user_group"
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
    
    url = base_url + f"/api/v2/users/user/unkonwn@cfx.com/group"
    data = {
        "group": "test_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    assert response.status_code == 500


def test_delete_user(session, base_url, unique_id):
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()