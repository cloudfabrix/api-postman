import pytest
from tests.conftest import logging

logger = logging.getLogger(__name__)

@pytest.mark.sanity
def test_pipelines_get(session, base_url):
    url = base_url + "/api/v2/pipelines"
    response = session.get(url, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_pipelines_get_cfxql(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "cfxql_query":"version ~ '2024'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_pipelines_get_search(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "search":"rda"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "rda"
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_pipelines_get_limit(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "limit":10
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_pipelines_get_sort(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

@pytest.mark.sanity
def test_pipelines_get_draft(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_pipelines_get_draft_cfxql(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "cfxql_query":"name ~ 'db_alerts'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "db_alerts" in response_json["draft_pipelines"][0]["name"]

@pytest.mark.sanity
def test_pipelines_get_draft_search(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "search":"db_incidents_clustering"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "db_incidents_clustering"
    assert response_json["num_items"] != 0

@pytest.mark.sanity
def test_pipelines_get_draft_sort(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

@pytest.mark.sanity
def test_pipelines_get_draft_limit(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "limit":5
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 5
