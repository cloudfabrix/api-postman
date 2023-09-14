from extras.reporting import CustomLogger

logger = CustomLogger().get_logger()

def test_GET_current_user(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/current_user"
    response = session.get(url, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_GET_users(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/users"
    response = session.get(url, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_POST_add_user(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/users"
    data = {
        "remoteUser": False,
        "authenticationType": "ad",
        "group": "test_user_group",
        "firstname": "test",
        "lastname": "api",
        "id": "user_test9@cfx.com"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_PUT_deactivate_user(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/users/user/user_test9@cfx.com/status"
    data = {
        "activate": False
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_PUT_activate_user(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/users/user/user_test@cfx.com/status"
    data = {
        "activate": True
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_PUT_change_user_group(api_session):
    session, base_url = api_session
    url = base_url + f"/api/v2/users/user/user_test@cfx.com/group"
    data = {
        "group": "test_user_group"
    }
    response = session.put(url, params=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200
