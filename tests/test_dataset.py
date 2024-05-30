import json
import time
from tests.conftest import logging
import pytest

logger = logging.getLogger(__name__)

def test_get_dataset(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    time.sleep(10)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_cfxql(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":"name ~ 'sample'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_cfxql_negative(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":"name ~ 'negative'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_search(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":"synthetic_syslogs_dataset",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_search_negative(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":"negative",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_dataset_limit(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":3,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

def test_add_dataset(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

def test_added_dataset_verf(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": "test"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 409

def test_get_dataset_added_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"negative",
        "folder": "Default",
        "schema_name": "",
        "tag": "test"
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 409

def test_get_added_dataset_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["search"] == f"{unique_id}_dataset"

def test_update_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "replace": True
    }
    request_body = [
        {"__uuid": f"{unique_id}", "column1":"row1"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

# def test_update_dataset_data_negative(session, base_url, unique_id):
#     url = base_url + f"/api/v2/datasets/dataset/negative_dataset/data"
#     data = {
#         "replace": True
#     }
#     request_body = [
#         {"__uuid": f"{unique_id}", "column1":"row1"}
#     ]
#     response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
#     logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
#     response.raise_for_status()

def test_replace_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "replace": True
    }
    request_body = [
        {"__uuid": f"{unique_id}", "column1":"row2"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_replace_dataset_data_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "replace": True
    }
    request_body = [
        {"__uuid": f"{unique_id}", "column1":"row2"}
    ]
    response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_get_added_dataset_data(session, base_url, unique_id):
    # need fix
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "offset":0,
        "limit":100
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    response_json["dataset_data"] == [{"__uuid": f"{unique_id}", "column1":"row2"}]

def test_delete_dataset_rows(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data"
    data = {
        "keys":"column1"
    }
    request_body = [
        {"column1":"row2"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dataset_rows_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset/data"
    data = {
        "keys":"column1"
    }
    request_body = [
        {"column1":"row2"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_all_dataset_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data/all"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_all_dataset_data_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset/data/all"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_delete_dataset(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

def test_delete_dataset_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(15)
    response.raise_for_status()

def test_deleted_dataset_verf_cfxql(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='{unique_id}_dataset'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

def test_deleted_dataset_verf_cfxql_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='neagtive_dataset'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

def test_deleted_dataset_verf_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_add_all_params_dataset_negative(session, base_url,name):
    url = base_url + "/api/v2/datasets"
    data = {
            "name": name,
            "folder": "Default",
            "schema_name": "",
            "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    time.sleep(12)
    data_schema = {
    "cfxql_query":f"name = '{name}'",
    "offset":0,
    "limit":100,
    "sort":"-timestamp"
    }
    response = session.get(url, params=data_schema, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["total_count"] >= 0
    assert response_json["num_items"] >= 0

@pytest.mark.parametrize("name", [
'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_get_all_params_dataset_verf(session, base_url, name):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name ~ '{name}'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()
    dataset_name = data['datasets'][0]['name']
    assert response.status_code == 200
    assert dataset_name == name
    
''' to-do as the dataset is currenctly not taking special chars'''
# @pytest.mark.parametrize("name", [
#     'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
#     'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
#     'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
#      'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
# ])
# def test_update_all_params_dataset_negative(session, base_url, name):
#     url = base_url + f"/api/v2/datasets/dataset/{name}/data"
#     data = {
#         "replace": True
#     }
#     request_body = [
#         {"__uuid": f"{name}", "column1":"row1"}
#     ]
#     response = session.put(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
#     logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
#     response.raise_for_status()

# @pytest.mark.parametrize("name", [
# 'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
#     'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
#     'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
#      'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
# ])
# def test_get_all_params_updated_dataset_negative(session, base_url, name):
#     url = base_url + "/api/v2/datasets"
#     data = {
#         "cfxql_query":f"name ~ '{name}'",
#         "offset":0,
#         "limit":100,
#         "sort":"-timestamp"
#     }
#     response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
#     logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
#     response.raise_for_status()
#     data = response.json()
#     print(data, '--------------------')
#     dataset_name = data['datasets'][0]['name']
#     assert response.status_code == 200
#     assert dataset_name == name

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_delete_all_params_dataset_negative(session, base_url,name):
    url = base_url + f"/api/v2/datasets/dataset/{name}"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_get_deleted_all_params_dataset_verf(session, base_url, name):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name ~ '{name}'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    data = response.json()
    dataset = data['num_items']
    assert response.status_code == 200
    assert dataset == 0