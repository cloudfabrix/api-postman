import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_metadata_pipelines(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/pipelines"
    data = {
        "cfxql_query":"*",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    response.raise_for_status()

def test_get_draft_pipelines(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/pipelines/draft"
    data = {
        "cfxql_query":"*",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    response.raise_for_status()

def test_post_run_pipelines(api_session, base_url):
    session = api_session
    base_url = base_url
    url = base_url + "/api/v2/pipelines/pipeline/generate-alerts-suppression-policy-dataset/version/2023_09_20_1/run"
    data = {
        "site":"*",
        "enable_tracing":True,
        "enable_logging":True
    }
    request_body = [
        {}
    ]
    response = session.post(url, params=data, json=request_body, headers=session.headers, verify=False)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}")
    if response.status_code != 200:
        logger.error(f"---------API Error---------\n{response.text}")
    else:
        logger.info(f"---------API Response----------\n{response.text}")

    response.raise_for_status()
