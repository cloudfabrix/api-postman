import time
from extras.reporting import CustomLogger

logger = CustomLogger().get_logger()

def test_DELETE_row_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets/dataset/test_api_dataset9/data"
    data = {
        "keys":"column2"
    }
    request_body = [
        {"column2":"row1"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_DELETE_all_data_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets/dataset/test_api_dataset9/data/all"
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200

def test_DELETE_dataset(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/datasets/dataset/test_api_dataset9"
    time.sleep(10)
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200



def test_DELETE_pstream(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/pstreams/pstream/test_api_pstream"
    data = {
        "delete_data": True
    }
    time.sleep(10)
    response = session.delete(url, params=data, headers=session.headers, verify=False)
    logger.info(f"---- API Log ---- {url} == {response.status_code}")
    if response.status_code != 200:
        logger.error(f"----------API Error----------\n{response.text}")
    else:
        logger.info(f"----------API Response----------\n{response.text}")
    
    assert response.status_code == 200

def test_DELETE_dashboard(api_session):
    session, base_url = api_session
    url = base_url + "/api/v2/dashboards/dashboard/test_api_dashboard9"
    time.sleep(10)
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    assert response.status_code == 200