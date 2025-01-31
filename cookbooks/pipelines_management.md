# Pipelines

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.


## Get All Versions of a Published Pipeline

### Endpoint:
GET `/api/v2/pipelines/pipeline/{name}/versions`

### Description:
Retrieve a list of all versions of a specified published pipeline.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/pipeline/test_pipeline/versions' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5eNE|Z5eNE'
```

### Output:
![get_all_pipeline_versions](https://github.com/user-attachments/assets/a1824865-0263-4049-b5bb-835bae78517d)


## Get All Versions of a Draft Pipeline

### Endpoint:
GET `/api/v2/pipelines/draft/{name}/versions`

### Description:
Retrieve a list of all versions of a specified draft pipeline.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/draft/test_draft_pipeline/versions' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5eNm|Z5eNE'
```

### Output:
![get_all_draft_pipeline_versions](https://github.com/user-attachments/assets/2bf92c91-7257-4649-88fc-7edb60593b6b)


## Get a Specific Version of a Published Pipeline

### Endpoint:
GET `/api/v2/pipelines/pipeline/{name}/version/{version}`

### Description:
Retrieve the content and details of a specific version of a published pipeline.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline to retrieve. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/pipeline/test_pipeline/version/2025_01_27_2' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5eQ1|Z5eNE'
```

### Output:
![get_a_pipeline_version](https://github.com/user-attachments/assets/4e4b48e3-0907-461c-8f0e-5e6efe329e8e)


## Get a Specific Version of a Draft Pipeline

### Endpoint:
GET `/api/v2/pipelines/draft/{name}/version/{version}`

### Description:
Retrieve the content and details of a specific version of a draft pipeline.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline to retrieve. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/draft/test_draft_pipeline/version/2025_01_27_2' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5ePc|Z5eNE'
```

### Output:
![get_specific_draft_pipeline](https://github.com/user-attachments/assets/1bca605d-5712-402c-bfd2-22730be8aeb8)


## Add a Published Pipeline

### Endpoint:
POST `/api/v2/pipelines`

### Description:
Add a new published pipeline with specified details such as name, version, content, and optional parameters like category, use case, folder, and site selection.

### Query Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline. **Required.**
- `category` (string): The category of the pipeline. *(Optional)*
- `usecase` (string): The use case associated with the pipeline. *(Optional)*
- `folder` (string): The folder name for the pipeline. *(Default: "Default")*
- `skip_verification` (bool): Whether to skip verification during pipeline addition. *(Default: `false`)*
- `sites` (string): A regular expression to select a worker to run the pipeline. *(Default: "*")*

### Request Body:
The request body should contain the pipeline content in plain text format.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines?name=example_publish_pipeline&version=v1&category=api_test&usecase=postman_test&folder=Default&skip_verification=false&sites=*' \
--header 'Content-Type: text/plain' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QNl|Z0QB7' \
--data-raw '@c:timed-loop
        interval = 3660
    --> @exec:run-pipeline
            name = "aws-dependency-mapper-inner-pipeline" & ignore_failures = "yes"'
```

### Output:
![add_published_pipeline_output](https://github.com/user-attachments/assets/079173fa-628c-42c1-ac78-162c1174f758)


## Add a Draft Pipeline

### Endpoint:
POST `/api/v2/pipelines/draft`

### Description:
Add a new draft pipeline with details such as name, version, content, and optional parameters like category, use case, folder, and site selection.

### Query Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline. **Required.**
- `category` (string): The category of the pipeline. *(Optional)*
- `usecase` (string): The use case associated with the pipeline. *(Optional)*
- `folder` (string): The folder name for the pipeline. *(Default: "Default")*
- `skip_verification` (bool): Whether to skip verification during pipeline addition. *(Default: `false`)*
- `sites` (string): A regular expression to select a worker to run the pipeline. *(Default: "*")*

### Request Body:
The request body should contain the pipeline content in plain text format.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/draft?name=example_draft_pipeline&version=v1&category=api_test&usecase=postman_tests&folder=Default&skip_verification=false&sites=*' \
--header 'Content-Type: text/plain' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QPS|Z0QB7' \
--data-raw '## Load dataset
@dm:recall
            name="sample-servicenow-incidents"
    --> @dm:head
            n=1
    --> @dm:eval
            recipient = "'\''john.doe@example.com'\''" &
            subject = "'\''eBonding from ServiceNow: '\'' + str(number) + '\'': '\'' + short_description" &
            message_mime_type = "'\''html'\''"
    --> @dm:apply-template-by-row
            template_name = "Email HTML Template" &
            output_col = "message"
    --> @dm:selectcolumns
            include="^message$"'
```

### Output:
![add_draft_pipeline_output](https://github.com/user-attachments/assets/888c2043-bb61-4e5d-be76-29b822fb46cd)



## Edit a Published Pipeline

### Endpoint:
PUT `/api/v2/pipelines/pipeline/{name}`

### Description:
Edit an existing published pipeline. If the pipeline does not exist, it will be added with the provided details.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**

### Query Parameters:
- `version` (string): The version of the pipeline. Changes are added with the provided version, which can be a new or existing version. **Required.**
- `category` (string): The category of the pipeline. *(Optional)*
- `usecase` (string): The use case associated with the pipeline. *(Optional)*
- `folder` (string): The folder name for the pipeline. *(Default: "Default")*
- `skip_verification` (bool): Whether to skip verification during pipeline updates. *(Default: `false`)*
- `publish` (bool): If set to `true`, the updated pipeline will be published immediately after a successful update. Otherwise, it will remain as a draft. *(Default: `false`)*
- `sites` (string): A regular expression to select a worker to run the pipeline. *(Default: "*")*

### Request Body:
The request body should contain the updated pipeline content in plain text format.

### Example Request:

Sample-1: The updated pipeline will be saved as Draft Pipeline after a successful update. (publish=false)
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/pipelines/pipeline/example_publish_pipeline?version=v1&category=api_test&usecase=postman_tests&folder=Default&skip_verification=false&publish=false&sites=*' \
--header 'Content-Type: text/plain' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QS2|Z0QB7' \
--data-raw '@c:timed-loop
        interval = 2080
    --> @exec:run-pipeline
            name = "aws-dependency-mapper-inner-pipeline" & ignore_failures = "no"'
```

### Output:
![edit_published_pipeline_draft_output](https://github.com/user-attachments/assets/5e29e3b7-843b-4959-8329-7b88bb1353ab)


Sample-2: The updated pipeline will be published immediately after a successful update. (publish=true)
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/pipelines/pipeline/example_publish_pipeline?version=2024_11_25_v2&category=api_test&usecase=postman_tests&folder=Default&skip_verification=false&publish=true&sites=*' \
--header 'Content-Type: text/plain' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QUe|Z0QB7' \
--data-raw '@c:timed-loop
        interval = 2080
    --> @exec:run-pipeline
            name = "aws-dependency-mapper-inner-pipeline" & ignore_failures = "no"'
```

### Output:
![edit_published_pipeline_publish_output](https://github.com/user-attachments/assets/5ca380be-9554-48d4-9567-d88d9935ec46)


## Edit a Draft Pipeline

### Endpoint:
PUT `/api/v2/pipelines/draft/{name}`

### Description:
Edit an existing draft pipeline. If the pipeline does not exist, it will be added with the provided details.

### Path Parameters:
- `name` (string): The name of the draft pipeline. **Required.**

### Query Parameters:
- `version` (string): The version of the pipeline. Changes are added with the provided version, which can be new or existing. **Required.**
- `category` (string): The category of the pipeline. *(Optional)*
- `usecase` (string): The use case associated with the pipeline. *(Optional)*
- `folder` (string): The folder name for the pipeline. *(Default: "Default")*
- `skip_verification` (bool): Whether to skip verification during pipeline updates. *(Default: `false`)*
- `publish` (bool): If set to `true`, the updated pipeline will be published immediately after a successful update. Otherwise, it will remain as a draft. *(Default: `false`)*
- `sites` (string): A regular expression to select a worker to run the pipeline. *(Default: "*")*

### Request Body:
The request body should contain the updated pipeline content in plain text format.

### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/pipelines/draft/example_draft_pipeline?version=2024_11_25_v1&category=api_test&usecase=postman_tests&folder=Default&skip_verification=false&publish=false&sites=*' \
--header 'Content-Type: text/plain' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QYM|Z0QB7' \
--data-raw '## Load dataset
@dm:recall
            name="example-sample-servicenow-incidents"
    --> @dm:head
            n=2
    --> @dm:eval
            recipient = "'\''jack.ryan@example.com'\''" &
            subject = "'\''eBonding from ServiceNow: '\'' + str(number) + '\'': '\'' + short_description" &
            message_mime_type = "'\''html'\''"
    --> @dm:apply-template-by-row
            template_name = "Email HTML Template" &
            output_col = "message_output"
    --> @dm:selectcolumns
            include="^message_output$"'
```

### Output:
![edit_draft_pipeline_draft_output](https://github.com/user-attachments/assets/c7370547-68a3-4e3e-8af1-3af502af1e06)


## Run a Draft Pipeline

### Endpoint:
POST `/api/v2/pipelines/draft/{name}/version/{version}/run`

### Description:
Run a draft pipeline with a specified version.

### Path Parameters:
- `name` (string): The name of the draft pipeline to run. **Required.**
- `version` (string): The version of the draft pipeline to run. **Required.**

### Query Parameters:
- `enable_tracing` (bool): Whether to enable trace viewing during the execution of the pipeline. *(Default: `true`)*
- `enable_logging` (bool): Whether to enable log viewing during the execution of the pipeline. *(Default: `true`)*
- `sites` (string): A regular expression to select the worker that will execute the pipeline. *(Default: "*")*

### Request Body:
- `data` (List of Dictionaries, Optional): Input data passed to the pipeline in a list of dictionary format.

### Example Request:
```shell cURL
curl --location --request POST 'https://10.95.125.95/api/v2/pipelines/draft/example_draft_pipeline/version/2024_11_25_v1/run?enable_tracing=true&enable_logging=true&sites=*' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QZ+|Z0QB7' \
--data ''
```

### Output:
![run_draft_pipeline_output](https://github.com/user-attachments/assets/c53724b7-269d-4e1e-8b0d-d92960369b27)


## Publish a Draft Pipeline

### Endpoint:
POST `/api/v2/pipelines/draft/{name}/version/{version}/publish`

### Description:
Publish a specified draft pipeline. Optionally, you can specify a new version or use the existing draft version for publishing.

### Path Parameters:
- `name` (string): The name of the draft pipeline to publish. **Required.**
- `version` (string): The version of the draft pipeline to publish. **Required.**

### Query Parameters:
- `folder` (string): The folder name where the pipeline will be published. *(Default: "Default")*
- `publish_version` (string): The version for the published pipeline. If not provided, the draft version will be used. *(Optional)*
- `skip_verification` (bool): Whether to skip verification of the pipeline before publishing. *(Default: `false`)*
- `sites` (string): A regular expression to select the worker to run the pipeline. *(Default: "*")*

### Example Request:
```shell cURL
curl --location --request POST 'https://10.95.125.95/api/v2/pipelines/draft/example_draft_pipeline/version/2024_11_25_v1/publish?folder=Default&publish_version=v3&skip_verification=false&sites=*' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0Qbz|Z0QB7'
```

### Output:
![publish_draft_pipeline_output](https://github.com/user-attachments/assets/86797535-5763-44b0-a2a6-8117b5755aba)


## Delete a Published Pipeline Version

### Endpoint:
DELETE `/api/v2/pipelines/pipeline/{name}/version/{version}`

### Description:
Delete a specific version of a published pipeline.

### Path Parameters:
- `name` (string): The name of the published pipeline to delete. **Required.**
- `version` (string): The version of the published pipeline to delete. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/pipeline/example_draft_pipeline/version/2024_11_25_v3' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0Qdb|Z0QB7'
```

### Output:
![delete_published_pipeline_version](https://github.com/user-attachments/assets/fd03fd0b-3528-4315-b7d4-869377a7f03d)


## Delete a Draft Pipeline Version

### Endpoint:
DELETE `/api/v2/pipelines/draft/{name}/version/{version}`

### Description:
Delete a specific version of a draft pipeline.

### Path Parameters:
- `name` (string): The name of the draft pipeline to delete. **Required.**
- `version` (string): The version of the draft pipeline to delete. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/draft/example_publish_pipeline/version/2024_11_25_v1' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0Qec|Z0QB7'
```

### Output:
![delete_draft_pipeline_version](https://github.com/user-attachments/assets/5f9b3be1-f518-4d3f-b3ed-7ec5f73567d4)


## Delete All Versions of a Published Pipeline

### Endpoint:
DELETE `/api/v2/pipelines/pipeline/{name}`

### Description:
Delete all versions of a published pipeline.

### Path Parameters:
- `name` (string): The name of the published pipeline to delete all versions of. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/pipeline/test_ad' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QfC|Z0QB7'
```

### Output:
**![delete_all_versions_pipelines](https://github.com/user-attachments/assets/6cc6341d-deaf-446d-a4ce-09fa65970467)


## Delete All Versions of a Draft Pipeline

### Endpoint:
DELETE `/api/v2/pipelines/draft/{name}`

### Description:
Delete all versions of a draft pipeline.

### Path Parameters:
- `name` (string): The name of the draft pipeline to delete all versions of. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/draft/test_ad_one' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QgU|Z0QB7'
```

### Output:
![delete_pipelines_all_versions](https://github.com/user-attachments/assets/55eb0501-0db1-4d6f-b717-f716be14ffca)


## Get Traces for Pipelines

### Endpoint:
GET `/api/v2/pipelines/traces`

### Description:
Retrieve traces for all pipelines.

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"status='success'"`

- `search` (string, optional):
  search across fields: ['pipeline_name', 'jobid', 'status_type', 'bot', 'query']

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp", "-status"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/traces?offset=0&limit=100&sort=-timestamp' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5eWK|Z5eNE'
```
### Output:
![get_traces](https://github.com/user-attachments/assets/7d6d1491-6deb-490e-887a-a6b4d6ff3b8c)


## Get Traces of a Pipeline

### Endpoint:
GET `/api/v2/pipelines/{name}/traces`

### Description:
Retrieve traces for a specific pipeline, with optional filtering and sorting capabilities.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"status='success'"`

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp", "-status"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/test_ad/traces' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=ab0ae6b5-5ce1-4b93-a19f-86770f802850; cfx_saas_session=4f5b60f8a3464131a7abec85209b3f75; rdafportal=rdaf-portal-1|Z5eW7|Z5eNE'
```
### Output:
![get_specific_traces](https://github.com/user-attachments/assets/ef0d7475-f39a-4c1d-a9b1-d6964473766c)


## Get Traces for a Specific Pipeline Version

### Endpoint:
GET `/api/v2/pipelines/{name}/version/{version}/traces`

### Description:
Retrieve execution traces for a specific version of a pipeline, with options for filtering, sorting, and pagination.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline. **Required.**

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"status='success'"`

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp", "-status"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results. Useful for pagination.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/test_ad/version/2025_01_24_1/traces' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=c167ed14-2ce7-43af-b108-49cc6d04cd68; cfx_saas_session=67cc97815b224271b0401b3385df9cf7; rdafportal=rdaf-portal-1|Z5eYw|Z5eNE'
```

### Output:
![get_pipeline_version_traces](https://github.com/user-attachments/assets/4920f3ec-c517-464b-ac21-22e74f449d1e)


## Get Logs for Pipelines

### Endpoint:
GET `/api/v2/pipelines/logs`

### Description:
Retrieve logs for all pipelines.

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"error='bot not found'"`

- `search` (string, optional):
  search across fields: ['pipeline_name', 'jobid', 'message']

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/logs' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=c167ed14-2ce7-43af-b108-49cc6d04cd68; cfx_saas_session=67cc97815b224271b0401b3385df9cf7; rdafportal=rdaf-portal-1|Z5eZg|Z5eNE'
```
### Output:
![get_logs](https://github.com/user-attachments/assets/c334b70a-b0af-44c2-8860-bd2878b78e01)


## Get Logs of a Pipeline

### Endpoint:
GET `/api/v2/pipelines/{name}/logs`

### Description:
Retrieve logs for a specific pipeline, with optional filtering and sorting capabilities.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"error='credential asset-discovery not found'"`

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp", "-status"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/test_ad/logs' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=c167ed14-2ce7-43af-b108-49cc6d04cd68; cfx_saas_session=67cc97815b224271b0401b3385df9cf7; rdafportal=rdaf-portal-1|Z5eaW|Z5eNE'
```
### Output:
![get_pipeline_logs](https://github.com/user-attachments/assets/258a310a-ae18-4f93-8b66-6e5bd8c19710)


## Get Logs for a Specific Pipeline Version

### Endpoint:
GET `/api/v2/pipelines/{name}/version/{version}/logs`

### Description:
Retrieve execution logs for a specific version of a pipeline, with options for filtering, sorting, and pagination.

### Path Parameters:
- `name` (string): The name of the pipeline. **Required.**
- `version` (string): The version of the pipeline. **Required.**

### Query Parameters:
- `cfxql_query` (string, optional):  
  Use CFXQL to filter the results.  
  Example: `"error='pstream query failed'"`

- `sort` (list of strings, optional):  
  Fields to sort the results by. Use `-` before the field name for descending order.  
  Example: `["timestamp", "-status"]`

- `offset` (integer, optional, default: 0):  
  The starting point for the results. Useful for pagination.

- `limit` (integer, optional, default: 100):  
  The maximum number of results to return. Must be 1 or greater.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pipelines/test_ad/version/2025_01_24_1/logs' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=c167ed14-2ce7-43af-b108-49cc6d04cd68; cfx_saas_session=67cc97815b224271b0401b3385df9cf7; rdafportal=rdaf-portal-1|Z5eaw|Z5eNE'
```

### Output:
![get_pipeline_version_logs](https://github.com/user-attachments/assets/2b024dcb-21ba-4735-b007-d0cecde75dec)
