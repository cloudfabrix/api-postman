import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_blueprints(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    response = session.get(url, headers=session.headers, verify=False, timeout=30)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_blueprints_cfxql(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "cfxql_query":"name ~ 'Alerts'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=30)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "Alerts" in response_json["blueprints"][0]["name"]

def test_get_blueprints_search(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "search":"Alerts Enricher"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=30)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "Alerts Enricher"
    assert response_json["num_items"] != 0

def test_get_blueprints_sort(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=30)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_blueprints_limit(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "limit":1
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=30)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 1