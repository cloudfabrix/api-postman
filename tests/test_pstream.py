import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_metadata_pstream(api_session, base_url):
    session = api_session
    base_url = base_url
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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_post_add_pstream(api_session, base_url):
    session = api_session
    base_url = base_url
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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_put_edit_pstream(api_session, base_url):
    session = api_session
    base_url = base_url
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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response.raise_for_status()

def test_get_single_pstream(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/pstreams/pstream/rda_secrets_meta/data"
    data = {
        "cfxql_query":"*",
        "offset":0,
        "limit":100
    }
    time.sleep(10)
    response = session.get(url, params=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")

    response.raise_for_status()

def test_delete_pstream(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/pstreams/pstream/test_api_pstream"
    data = {
        "delete_data": True
    }
    time.sleep(10)
    response = session.delete(url, params=data, headers=session.headers, verify=False)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
