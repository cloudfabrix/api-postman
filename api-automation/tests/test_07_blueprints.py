from extras.reporting import CustomLogger

import time

logger = CustomLogger().get_logger()

def test_GET_metadata_blueprints(api_session):
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
