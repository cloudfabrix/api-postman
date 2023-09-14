from extras.reporting import CustomLogger

import time

logger = CustomLogger().get_logger()

def test_GET_metadata_pstream(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/pstreams"
    data = {
        "cfxql_query":"*",
        "search":"",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_POST_add_pstream(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/pstreams"
    request_body = {
        "attributes": {
            "retention_days": 31,
            "unique_keys": [
            "OIA",
            "AIA"
            ]
        },
        "name": "test_api_pstream"
    }
    response = session.post(url, json=request_body, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_PUT_edit_pstream(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/pstreams/pstream/test_api_pstream"
    request_body = {
        "attributes": {
            "retention_days": 62,
            "unique_keys": [
            "AIA",
            "OIA"
            ]
        }
    }
    time.sleep(10)
    response = session.put(url, json=request_body, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_GET_single_pstream(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/pstreams/pstream/rda_secrets_meta/data"
    data = {
        "cfxql_query":"*",
        "offset":0,
        "limit":100
    }
    time.sleep(10)
    response = session.get(url, params=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")

    assert response.status_code == 200

