import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_metadata_dataset(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_post_add_dataset(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + "/api/v2/datasets"
    data = {
        "name": unique_id,
        "folder": "Default",
        "schema_name": "",
        "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(10)

    response.raise_for_status()

def test_put_update_dataset_data(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}/data"
    data = {
        "replace": True
    }
    request_body = [
        {"column1":"row1"}, {"column2":"row1"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_added_dataset(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}/data"
    data = {
        "search":unique_id,
        "offset":0,
        "limit":100
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_row_dataset(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}/data"
    data = {
        "keys":"column2"
    }
    request_body = [
        {"column2":"row1"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_all_data_dataset(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}/data/all"
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dataset(api_session, base_url, unique_id):
    session = api_session
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}"
    time.sleep(10)
    response = session.delete(url, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()