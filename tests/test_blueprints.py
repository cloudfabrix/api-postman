import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_metadata_blueprints(api_session, base_url):
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
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
