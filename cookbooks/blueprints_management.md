# Blueprints

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

## Add a Blueprint

### Endpoint:
POST `/api/v2/blueprints`

### Description:
Add a new blueprint to the system.

### Request Body:
The body of the request should contain the blueprint in json format only.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/blueprints' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QCn|Z0QB7' \
--data '{
    "name": "Sample Scheduled Blueprint",
    "id": "sample scheduled blueprint",
    "comment": "API tests",
    "version": "1",
    "category": "sample",
    "type": "Service",
    "provider": "CloudFabrix Software, Inc.",
    "service_pipelines": [],
    "scheduled_pipelines": [
        {
            "name": "sample-scheduled-pipeline-1",
            "label": "Sample scheduled pipeline 1",
            "version": "*",
            "site": "rda.*",
            "cron_expression": "0 12 * * *",
            "site_type": "regex"
        }
    ],
    "enabled": true
}'
```

### Output:
![add_blueprint_output](https://github.com/user-attachments/assets/66f4762b-292c-4190-b6eb-2071b33f4cdf)


## Edit an Existing Blueprint

### Endpoint:
PUT `/api/v2/blueprints/blueprint/{id}`

### Description:
Edit an existing blueprint. If the blueprint with the specified ID does not exist, it will be added to the system as a new blueprint.

### Path Parameters:
- `id` (string): The unique identifier of the blueprint to edit.

### Request Body:
The body of the request should contain the updated details for the blueprint.

### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/blueprints/blueprint/sample%20scheduled%20blueprint' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QCn|Z0QB7' \
--data '{
    "name": "Edited Sample Scheduled Blueprint",
    "id": "sample scheduled blueprint",
    "comment": "Edited API tests",
    "version": "1",
    "category": "sample",
    "type": "Service",
    "provider": "CloudFabrix Software, Inc.",
    "service_pipelines": [],
    "scheduled_pipelines": [
        {
            "name": "sample-scheduled-pipeline-1",
            "label": "Sample scheduled pipeline 1",
            "version": "*",
            "site": "rda.*",
            "cron_expression": "0 12 * * *",
            "site_type": "regex"
        }
    ],
    "enabled": true
}'
```

### Output:
![edit_blueprint_output](https://github.com/user-attachments/assets/ea45c266-5dbe-4448-b9ac-e68a67df869e)


## Enable/Disable an Existing Blueprint

### Endpoint:
PUT `/api/v2/blueprints/blueprint/{id}/status`

### Description:
Change the status of an existing blueprint by enabling or disabling it.

### Path Parameters:
- `id` (string): The unique identifier of the blueprint whose status needs to be updated.

### Query Parameters:
| Parameter        | Type   | Description                                                                  |
|------------------|--------|------------------------------------------------------------------------------|
| `status`         | Enum (Enable or Disable) | Choose (Enable/Disable) to change status of a blueprint    |

### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/blueprints/blueprint/sample%20scheduled%20blueprint/status?status=disable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QHH|Z0QB7'
```

### Output:
![change_blueprint_status_output](https://github.com/user-attachments/assets/a1f63189-1652-41ab-a365-cdace932343f)


## Delete a Specific Blueprint

### Endpoint:
DELETE `/api/v2/blueprints/blueprint/{id}`

### Description:
Delete a specific blueprint from the system using its unique identifier.

### Path Parameters:
- `id` (string): The unique identifier of the blueprint to delete.

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/blueprints/blueprint/sample%20scheduled%20blueprint' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=85cd76a0-c9c5-4d4b-905c-7ab6b250ed7e; cfx_saas_session=e5f90bb9a4a746e1b49d76f60d373ba1; rdafportal=rdaf-portal-1|Z0QI0|Z0QB7'
```

### Output:
![delete_blueprint_output](https://github.com/user-attachments/assets/52ab0113-700b-4e46-86fd-c67c112e7453)
