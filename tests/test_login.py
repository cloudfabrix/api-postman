import requests
import time
from tests.conftest import logging
import pytest

logger = logging.getLogger(__name__)

def test_POST_login(base_url, username, password):
    session = requests.Session()
    post_data = {
        "user": username,
        "password": password
    }
    url = base_url + "/api/v2/login"
    response = session.post(url, json=post_data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"---- API Log ---- {url}:::{response.status_code}::::{response.text}")
    response.raise_for_status()

def test_POST_login_negative_user(base_url, password):
    session = requests.Session()
    post_data = {
        "user": "unknow@cfx.com",
        "password": password
    }
    url = base_url + "/api/v2/login"
    response = session.post(url, json=post_data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"---- API Log ---- {url}:::{response.status_code}::::{response.text}")
    assert response.status_code == 400

def test_POST_login_negative_password(base_url, username, password):
    session = requests.Session()
    post_data = {
        "user": username,
        "password": "unkown"
    }
    url = base_url + "/api/v2/login"
    response = session.post(url, json=post_data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"---- API Log ---- {url}:::{response.status_code}::::{response.text}")
    assert response.status_code == 401


