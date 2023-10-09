import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_pipelines(session, base_url):
    url = base_url + "/api/v2/pipelines"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_pipelines_cfxql(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "cfxql_query":"version ~ '2024'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 0

def test_get_pipelines_search(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "search":"rda"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "rda"
    assert response_json["num_items"] == 0

def test_get_pipelines_limit(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "limit":1
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 1

def test_get_pipelines_sort(session, base_url):
    url = base_url + "/api/v2/pipelines"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_draft_pipelines(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_draft_pipelines_cfxql(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "cfxql_query":"name ~ 'db_alerts'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] != 0
    assert "db_alerts" in response_json["draft_pipelines"][0]["name"]

def test_get_draft_pipelines_search(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "search":"db_incidents_clustering"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["search"] == "db_incidents_clustering"
    assert response_json["num_items"] != 0

def test_get_draft_pipelines_sort(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "sort":"-name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["sort"] == ['-name']

def test_get_draft_pipelines_limit(session, base_url):
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "limit":5
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()
    assert response_json["num_items"] == 5