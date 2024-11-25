# Pipelines

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

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
DELETE `/api/v2/pipelines/pipeline/{name}/all_versions`

### Description:
Delete all versions of a published pipeline.

### Path Parameters:
- `name` (string): The name of the published pipeline to delete all versions of. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/pipeline/example_publish_pipeline/all_versions' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QfC|Z0QB7'
```

### Output:
![delete_all_versions_published_pipeline](https://github.com/user-attachments/assets/8fa04d15-5a9a-4d3a-b59c-ba5edf0d7da3)


## Delete All Versions of a Draft Pipeline

### Endpoint:
DELETE `/api/v2/pipelines/draft/{name}/all_versions`

### Description:
Delete all versions of a draft pipeline.

### Path Parameters:
- `name` (string): The name of the draft pipeline to delete all versions of. **Required.**

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pipelines/draft/example_draft_pipeline/all_versions' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QgU|Z0QB7'
```

### Output:
![delete_all_versions_draft_pipeline](https://github.com/user-attachments/assets/3cb0f85a-37c6-4b33-bb42-6b5c1d9876f3)
