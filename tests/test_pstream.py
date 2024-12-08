from tests.conftest import logging
import pytest 

logger = logging.getLogger(__name__)

@pytest.mark.sanity
def test_pstream_get(session, base_url):
    url = base_url + "/api/v2/pstreams"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_pstream_get_cfxql(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "cfxql_query":"name ~ 'rda_system_bot_package_changes'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == ['rda_system_bot_package_changes']

@pytest.mark.sanity
def test_pstream_get_search(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "search":"rda_system_bot_package_changes"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == ['rda_system_bot_package_changes']
    assert response_json["search"] == "rda_system_bot_package_changes"
    assert response_json["num_items"] != 0


@pytest.mark.sanity
def test_pstream_get_sort(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "sort":"name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['name']

    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == sorted(pstream_names)

@pytest.mark.sanity
def test_pstream_get_limit(session, base_url):
    url = base_url + "/api/v2/pstreams"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 10

    pstream = response_json.get('pstreams', [])
    num_pstream = len(pstream)
    assert num_pstream == 10

@pytest.mark.sanity
def test_pstream_add(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_pstream_added_verf(session, base_url, unique_id):
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
    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == [f"{unique_id}_pstream"]

@pytest.mark.sanity
def test_pstream_add_empty_name_verf(session, base_url):
    url = base_url + "/api/v2/pstreams"
    request_body = {
        "attributes": {
            "retention_days": 31
        },
        "name": ""
    }
    response = session.post(url, json=request_body, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    # response.raise_for_status()

    expected_response = {"detail":"Persistent Stream name must not be empty"}
    actual_response = response.json()
    assert actual_response == expected_response

@pytest.mark.sanity
def test_pstream_update(session, base_url, unique_id):
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
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_pstream_updated_verf(session, base_url, unique_id):
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
    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == [f"{unique_id}_pstream"]

@pytest.mark.sanity
def test_pstream_delete(session, base_url, unique_id):
    base_url = base_url
    unique_id = unique_id
    url = base_url + f"/api/v2/pstreams/pstream/{unique_id}_pstream"
    data = {
        "delete_data": True
    }
    response = session.delete(url, params=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

@pytest.mark.sanity
def test_pstream_deleted_verf(session, base_url, unique_id):
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
    pstream_names = [pstream['name'] for pstream in response_json['pstreams']]
    assert pstream_names == []

@pytest.mark.sanity
def test_pstream_get_data(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0

@pytest.mark.sanity
def test_pstream_get_data_cfxql(session, base_url):
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

@pytest.mark.sanity
def test_pstream_get_data_search(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "search":"ml-regression-training-data"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    
    response_json = response.json()
    assert response_json["search"] == "ml-regression-training-data"
    pstream_names = [pstream['name'] for pstream in response_json['pstream_data']]
    assert pstream_names == ["ml-regression-training-data"]
    assert response_json["num_items"] != 0
    
@pytest.mark.sanity
def test_pstream_get_data_sort(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "sort":"name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['name']

    pstream_names = [pstream['name'] for pstream in response_json['pstream_data']]
    assert pstream_names == sorted(pstream_names)

@pytest.mark.sanity
def test_pstream_get_data_limit(session, base_url):
    # used existsing pstream
    url = base_url + "/api/v2/pstreams/pstream/rda_pstreams_meta/data"
    data = {
        "limit":5
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 5

    pstream = response_json.get('pstream_data', [])
    num_pstream = len(pstream)
    assert num_pstream == 5
