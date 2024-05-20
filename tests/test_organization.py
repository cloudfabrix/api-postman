import time
from tests.conftest import logging

logger = logging.getLogger(__name__)

def test_get_organizations(session, base_url):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)

    #time.sleep(5)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_add_organizations(session, base_url, unique_id):
    url = base_url + "/api/v2/organizations"
    data = {
  "description": "Automation Org",
  "name": f"{unique_id}_api_organization",
  "tag": "CFX-API-AUTO"
}
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()

    assert response_json['status'] == "SUBMIT_OK"

def test_get_added_organizations(session, base_url, unique_id):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)


    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()
    assert any(org['name'] == f'{unique_id}_api_organization' for org in data.get('organizations', []))

'''common method to get org id'''
def get_org_id(session, base_url, unique_id):
    # get the org id
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)
    data = response.json()
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    organizations = data.get('organizations', [])
    for org in organizations:
        if org.get('name') == f"{unique_id}_api_organization":
            org_id = org.get('id')
    return org_id

def test_update_organizations(session, base_url, unique_id):
    org_id = get_org_id(session, base_url, unique_id)
    url = base_url + f"/api/v2/organizations/organization/{org_id}"
    data = {
  "description": "Description-updated",
  "name": f"{unique_id}_api_organization"
}
    response = session.put(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()

    assert response_json['serviceResult']['status'] == "SUBMIT_OK"

def test_get_updated_organizations(session, base_url, unique_id):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)


    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()

    org_description = next((org['description'] for org in data['organizations'] if org['name'] == f'{unique_id}_api_organization'), None)
    assert org_description == "Description-updated"

def test_delete_organizations(session, base_url, unique_id):
    org_id = get_org_id(session, base_url, unique_id)
    url = base_url + f"/api/v2/organizations/organization/{org_id}"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

    response_json = response.json()

    assert response_json['serviceResult']['status'] == "SUBMIT_OK"


def test_get_deleted_organizations(session, base_url, unique_id):
    url = base_url + "/api/v2/organizations"
    response = session.get(url, headers=session.headers, verify=False, timeout=60)


    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()

    for org in data.get('organizations', []):
        if org.get('name') == f"{unique_id}_api_organization":
            assert False
            