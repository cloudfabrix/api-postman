import json
import time
from tests.conftest import logging
import pytest

logger = logging.getLogger(__name__)

def test_get_dataset(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_using_cfxql(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":"name ~ 'sample'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_using_search(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":"synthetic_syslogs_dataset",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_using_limit(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":3,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 3, "num_items is not equal to 3 in the response"

def test_add_dataset(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(10)
    response.raise_for_status()

def test_added_dataset_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": "test"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(10)
    assert response.status_code == 409

def test_get_added_dataset_cfxql(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    name = unique_id + "_dataset"
    data = {
        "cfxql_query":f"name={name}"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["datasets"][0]["name"] == name

def test_get_added_dataset_using_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    name = unique_id + '_dataset'
    data = {
        "search":name,
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["datasets"][0]["name"] == unique_id + '_dataset'

def test_update_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "replace": True
    }
    request_body = [
        {"__uuid": f"{unique_id}", "column1":"row1"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_replace_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "replace": True
    }
    request_body = [
        {"__uuid": f"{unique_id}", "column1":"row2"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_added_dataset_data(session, base_url, unique_id):
    # need fix
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "offset":0,
        "limit":100
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    response_json["dataset_data"] == [{"__uuid": f"{unique_id}", "column1":"row2"}]

def test_delete_dataset_rows(session, base_url, unique_id):
    unique_id = "test_api_20231001115143"
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "keys":"column1"
    }
    request_body = [
        {"column1":"row2"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_all_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data/all"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dataset(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset"
    time.sleep(10)
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()


def test_deleted_datasets_verf_cfxql(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='{unique_id}_dataset'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    time.sleep(20)
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

def test_deleted_dataset_verf_using_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0