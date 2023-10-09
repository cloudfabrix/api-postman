import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_user_groups(session, base_url):
    url = base_url + "/api/v2/user_groups"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_add_user_group(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    data = {
        "name":f"{unique_id}_user_group"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_edit_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    response = session.put(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_delete_user_group(session, base_url, unique_id):
    url = base_url + f"/api/v2/user_groups/user_group/{unique_id}_user_group"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["serviceResult"]["status"] == "SUBMIT_OK"

def test_deleted_user_group_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/user_groups"
    data = {
        "search":f"{unique_id}_user_group",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_user_group"
    assert response_json["num_items"] != 0