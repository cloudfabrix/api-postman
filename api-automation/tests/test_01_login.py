from extras.reporting import CustomLogger


logger = CustomLogger().get_logger()

def test_POST_login(api_session, user, password):
    session, base_url = api_session
    post_data = {
        "user": user,
        "password": password
    }
    url = base_url + "/api/v2/login"
    response = session.post(url, json=post_data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")

    assert response.status_code == 200