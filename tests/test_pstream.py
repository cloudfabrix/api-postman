import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_pstream(session, base_url):
    url = base_url + "/api/v2/pstreams"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_pstream_cfxql(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "cfxql_query":"name ~ 'rda'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "rda" in response_json["pstreams"][0]["name"]

def test_get_pstream_search(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "search":"rda_datasets_meta"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "rda_datasets_meta"
    assert response_json["num_items"] != 0

def test_get_pstream_sort(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_pstream_limit(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 10

def test_add_pstream(session, base_url, unique_id):
    url = base_url + "/api/v2/pstreams"
    request_body = {
        "attributes": {
        "retention_days": 31,
        "unique_keys": [
            "AIA",
            "OIA"
        ]
        },
        "name": f"{unique_id}_pstream"
    }
    response = session.post(url, json=request_body, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_added_pstream_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/pstreams"
    data = {
        "search":f"{unique_id}_pstream"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_pstream"
    assert response_json["num_items"] != 0
    assert response_json["pstreams"][0]["retention_days"] == 31

def test_add_empty_name_pstream_verf(session, base_url):
    url = base_url + "/api/v2/pstreams"
    request_body = {
        "attributes": {
            "retention_days": 31
        },
        "name": ""
    }
    response = session.post(url, json=request_body, headers=session.headers, verify=False, timeout=60)
    time.sleep(12)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    # response.raise_for_status()

    expected_response = {"detail":"Persistent Stream name must not be empty"}
    actual_response = response.json()
    assert actual_response == expected_response

def test_update_pstream(session, base_url, unique_id):
    url = base_url + f"/api/v2/pstreams/pstream/{unique_id}_pstream"
    request_body = {
        "attributes": {
            "retention_days": 62,
            "unique_keys": [
                "OIA",
                "AIA"
            ]
        }
    }
    response = session.put(url, json=request_body, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_updated_pstream_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/pstreams"
    data = {
        "search":f"{unique_id}_pstream"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert response_json["pstreams"][0]["retention_days"] == 62

def test_delete_pstream(session, base_url, unique_id):
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/pstreams/pstream/{unique_id}_pstream"
    data = {
        "delete_data": True
    }
    response = session.delete(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(15)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_deleted_pstream_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/pstreams"
    data = {
        "search":f"{unique_id}_pstream"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_pstream"
    assert response_json["num_items"] == 0

def test_get_pstream_data(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0

def test_get_pstream_data_cfxql(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "cfxql_query":"system_defined = 'no'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "no" in response_json["pstream_data"][0]["system_defined"]

def test_get_pstream_data_search(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "search":"oia-events-stream"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    
    response_json = response.json()
    assert response_json["search"] == "oia-events-stream"
    assert response_json["num_items"] != 0

def test_get_pstream_data_sort(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_pstream_data_limit(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 10