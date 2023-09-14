from extras.reporting import CustomLogger

import time

logger = CustomLogger().get_logger()

def test_GET_metadata_pipelines(api_session):
    session, base_url = api_session
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

    assert response.status_code == 200

def test_GET_draft_pipelines(api_session):
    session, base_url = api_session
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

    assert response.status_code == 200

def test_POST_run_pipelines(api_session):
    # need to publish the pipeline first and give that api in the url with version 
    session, base_url = api_session
    url = base_url + "/api/v2/pipelines/pipeline/generate-alerts-suppression-policy-pstream/version/2023_09_13_1/run"
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

    assert response.status_code == 200
