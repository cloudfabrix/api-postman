import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)


@pytest.mark.sanity
def test_blueprints_get(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_blueprints_get_cfxql(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "cfxql_query":"name ~ 'Alerts'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "Alerts" in response_json["blueprints"][0]["name"]

def test_blueprints_get_cfxql_negative(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "cfxql_query":"name ~ 'negative'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_blueprints_get_search(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "search":"Alerts Enricher"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "Alerts Enricher"
    assert response_json["num_items"] != 0

def test_blueprints_get_search_negative(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "search":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_blueprints_get_sort(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_blueprints_get_sort_negative(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "sort":"negative"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422

@pytest.mark.sanity
def test_blueprints_get_limit(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "limit":1
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 1

    blueprints = response_json.get('blueprints', [])

    num_blueprints = len(blueprints)
    assert num_blueprints == 1

def test_blueprints_get_limit_negative(session, base_url):
    url = base_url + "/api/v2/Blueprints"
    data = {
        "limit":'negative'
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 422
