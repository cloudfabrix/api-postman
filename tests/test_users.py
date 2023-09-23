from tests.conftest import logging

logger = logging.getLogger(__name__)


def test_get_current_user(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/current_user"
    response = session.get(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_get_users(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response.raise_for_status()

def test_post_add_user(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": "test_user_group",
        "firstname": "test",
        "lastname": "api",
        "id": f"{unique_id}@cfx.com"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_put_deactivate_user(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_put_activate_user(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_put_change_user_group(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/users/user/{unique_id}@cfx.com/group"
    data = {
        "group": "test_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()
