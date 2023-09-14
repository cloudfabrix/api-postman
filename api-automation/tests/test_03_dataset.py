from extras.reporting import CustomLogger

import time

logger = CustomLogger().get_logger()

def test_GET_metadata_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets"
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

def test_POST_add_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets"
    data = {
        "name": "test_api_dataset9",
        "folder": "Default",
        "schema_name": "",
        "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    time.sleep(10)
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_PUT_update_dataset_data(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets/dataset/test_api_dataset9/data"
    data = {
        "replace": True
    }
    request_body = [
        {"column1":"row1"}, {"column2":"row1"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_GET_added_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets/dataset/test_api_dataset9/data"
    data = {
        "cfxql_query":"*",
        "search":"test_api_dashboard",
        "offset":0,
        "limit":100
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200
