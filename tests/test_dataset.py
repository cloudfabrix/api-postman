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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_cfxql(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":"name ~ 'sample'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_search(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":"synthetic_syslogs_dataset",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_limit(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":3,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

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
    time.sleep(12)
    response.raise_for_status()

def test_added_dataset_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": "test"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 409

def test_get_added_dataset_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dataset"

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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    response_json["dataset_data"] == [{"__uuid": f"{unique_id}", "column1":"row2"}]

def test_delete_dataset_rows(session, base_url, unique_id):
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
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(30)
    response.raise_for_status()

def test_deleted_dataset_verf_cfxql(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='{unique_id}_dataset'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

def test_deleted_dataset_verf_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0