from tests.conftest import logging
import pytest

logger = logging.getLogger(__name__)
@pytest.mark.sanity
# adding spam dataset for limit and sort as there are no default datasets
def test_dataset_add_for_limit_sort(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    for i in range(10):
        dataset_name = f"{chr(97 + i)}_dataset"
        data = {
            "name": dataset_name,
            "folder": "Default",
            "schema_name": "",
            "tag": ""
        }
        response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
        logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()

@pytest.mark.sanity
def test_dataset_get(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

@pytest.mark.sanity
def test_dataset_get_cfxql(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":"name ~ 'a_dataset'",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    dataset_names = [dataset['name'] for dataset in response_json['datasets']]
    assert dataset_names == ['a_dataset']

def test_dataset_get_cfxql_negative(session, base_url):
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


@pytest.mark.sanity
def test_dataset_get_search(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":"b_dataset",
        "offset":0,
        "limit":100,
        "sort":"-timestamp"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    dataset_names = [dataset['name'] for dataset in response_json['datasets']]
    assert dataset_names == ['b_dataset']

def test_dataset_get_search_negative(session, base_url):
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

@pytest.mark.sanity
def test_dataset_get_limit(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":3,
        "sort":"name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 3

    dataset = response_json.get('datasets', [])
    num_dataset = len(dataset)
    assert num_dataset == 3

@pytest.mark.sanity
def test_dataset_get_sort(session, base_url):
    url = base_url + "/api/v2/datasets"
    data = {
        "offset":0,
        "limit":3,
        "sort":"name"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()

    dashboard_names = [dashboard['name'] for dashboard in response_json['datasets']]
    assert dashboard_names == sorted(dashboard_names)

    response_json = response.json()
    assert response_json["sort"] == ['name']

@pytest.mark.sanity
# deleting spam dataset for limit and sort as there are no default datasets
def test_dataset_delete_for_limit_sort(session, base_url):
    for i in range(10):
        dataset_name = f"{chr(97 + i)}_dataset"
        url = base_url + f"/api/v2/datasets/dataset/{dataset_name}"
        response = session.delete(url, headers=session.headers, verify=False, timeout=60)
        logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()

@pytest.mark.sanity
# check if the spam datasets exists
def test_dataset_deleted_verf_for_limit_sort(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    for i in range(10):
        dataset_name = f"{chr(97 + i)}_dataset"
        data = {
            "search":f"{dataset_name}"
        }
        response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
        logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
        response.raise_for_status()
        response_json = response.json()
        assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_dataset_add(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "name": f"{unique_id}_dataset",
        "folder": "Default",
        "schema_name": "",
        "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

def test_dataset_get_added_negative(session, base_url):
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

@pytest.mark.sanity
def test_dataset_get_added_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=40)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    dataset_names = [dataset['name'] for dataset in response_json['datasets']]
    assert dataset_names == [f"{unique_id}_dataset"]
    assert response_json["search"] == f"{unique_id}_dataset"

@pytest.mark.sanity
def test_dataset_update_data(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_dataset_replace_data(session, base_url, unique_id):
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

def test_dataset_replace_data_negative(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_dataset_get_added_data(session, base_url, unique_id):
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

@pytest.mark.sanity
def test_dataset_delete_rows(session, base_url, unique_id):
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

def test_dataset_delete_rows_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset/data"
    data = {
        "keys":"column1"
    }
    request_body = [
        {"column1":"row2"}
    ]
    response = session.delete(url, params=data, json=request_body, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

@pytest.mark.sanity
def test_dataset_delete_all_data(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset/data/all"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dataset_delete_all_data_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset/data/all"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    assert response.status_code == 404

@pytest.mark.sanity
def test_dataset_delete(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/{unique_id}_dataset"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()

def test_dataset_delete_negative(session, base_url, unique_id):
    url = base_url + f"/api/v2/datasets/dataset/negative_dataset"
    response = session.delete(url, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
    response.raise_for_status()

@pytest.mark.sanity
def test_dataset_deleted_verf_cfxql(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='{unique_id}_dataset'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    dataset_names = [dataset['name'] for dataset in response_json['datasets']]
    assert dataset_names == []
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_dataset_deleted_verf_cfxql_negative(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "cfxql_query":f"name='neagtive_dataset'"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    assert response_json["num_items"] == 0

@pytest.mark.sanity
def test_dataset_deleted_verf_search(session, base_url, unique_id):
    url = base_url + "/api/v2/datasets"
    data = {
        "search":f"{unique_id}_dataset"
    }
    response = session.get(url, params=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    response.raise_for_status()
    response_json = response.json()
    dataset_names = [dataset['name'] for dataset in response_json['datasets']]
    assert dataset_names == []
    assert response_json["num_items"] == 0

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_dataset_add_all_params(session, base_url,name):
    url = base_url + "/api/v2/datasets"
    data = {
            "name": name,
            "folder": "Default",
            "schema_name": "",
            "tag": ""
    }
    response = session.post(url, json=data, headers=session.headers, verify=False, timeout=60)
    logger.info(f"----API Log---- {url}:::{response.status_code}::::\n{response.text}")
    
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
def test_dataset_get_all_params_verf(session, base_url, name):
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
#     dataset_name = data['datasets'][0]['name']
#     assert response.status_code == 200
#     assert dataset_name == name

@pytest.mark.parametrize("name", [
    'data~sample', 'data`sample', 'data!sample', 'data@sample', 'data#sample', 'data$sample', 'data%sample', 
    'data^sample', 'data&sample', 'data*sample', '(data)sample', 'data_sample', 'data+sample', 'data-sample', 
    'data=sample', 'data{sample', 'data}sample', 'data[sample]','data|sample','data:sample', 'data;sample', 
     'data<sample', 'data>sample', 'data,sample', 'data.sample', 'data/sample','data\\sample'
])
def test_dataset_delete_all_params(session, base_url,name):
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
def test_dataset_get_deleted_all_params_verf(session, base_url, name):
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