# Organizations Management

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

## Get Organizations

### Endpoint:
GET `/api/v2/organizations`

### Description:
Retrieve a list of all organizations available to the current user.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/565ba823-9d14-42e4-8463-6ce5c689b61e" />

---

## Event Endpoints Management - Alerts

### Get All Alert Endpoints of an Organization

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/alerts/endpoints`

#### Description:
Retrieve all alert endpoints configured for a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Query Parameters:
| Parameter | Type    | Description                                    |
|-----------|---------|------------------------------------------------|
| `offset`  | integer | Offset to start the results from (default: 0)  |
| `limit`   | integer | Maximum number of results to return (default: 100) |

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/endpoints?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/376c3d9b-5077-4822-85b3-84a81d3ffd8f" />


### Get All Endpoint Types

#### Endpoint:
GET `/api/v2/organizations/configuration/endpoints/types`

#### Description:
Fetch all available endpoint types in the system.

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/types' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/5337cada-5837-4959-a3ca-c8d26a5dde70" />

### Get Fields for a Specific Endpoint Type

#### Endpoint:
GET `/api/v2/organizations/configuration/endpoints/types/{type}`

#### Description:
Fetch the fields required for a specific endpoint type. This is useful for understanding what parameters are needed when adding/creating endpoints of a particular type.

#### Path Parameters:
- `type` (string): Type of the endpoint (e.g., "webhook-basic", "csv", "email"). **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/types/webhook-basic' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/f75dbb26-6914-4bc4-8054-c7d1414c377e" />

### Add an Alert Endpoint in an Organization

#### Endpoint:
POST `/api/v2/organizations/organization/{id}/configuration/alerts/endpoints`

#### Description:
Add a new alert endpoint to a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Request Body Parameters:
| Parameter                  | Type    | Description                                    |
|----------------------------|---------|------------------------------------------------|
| `customerId`               | string  | Customer ID (required)                         |
| `name`                     | string  | Endpoint name (required)                       |
| `endpointType`             | string  | Type of endpoint (required)                    |
| `endpointRole`             | string  | Role of endpoint (default: 'source') [Options: 'source', 'target', 'mixed']          |
| `description`              | string  | Endpoint description (optional)                |
| `attributes`               | object  | Additional attributes (optional)               |
| `enabled`                  | string  | Enable status: "Yes" or "No" (default: "No")  |
| `publishToStreamFlag`      | boolean | Publish to stream flag (default: false)       |
| `publishStreamType`        | string  | Stream type (default: "NATS") [Options: 'NATS' & 'Kafka']                 |
| `publishToStreamOnlyFlag` | boolean | Publish to stream only flag (default: false) |

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/endpoints' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session' \
--data '{
  "customerId": "0a40637055e84074b606cf50119d7c6d",
  "name": "test_alert_ep",
  "endpointType": "webhook-basic",
  "endpointRole": "source",
  "description": "test_ep_webhook_api",
  "attributes": {},
  "enabled": "No",
  "publishToStreamFlag": false,
  "publishStreamType": "NATS",
  "publishToStreamOnlyFlag": false
}'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/1c141d8c-889c-4561-862a-1ea66473acb9" />

### Update an Alert Endpoint of an Organization

#### Endpoint:
PUT `/api/v2/organizations/organization/{id}/configuration/alerts/endpoints/{endpoint_id}`

#### Description:
Update an existing alert endpoint in a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**
- `endpoint_id` (string): ID of the endpoint. **Required.**

#### Request Body Parameters:
Same as Add Alert Endpoint (see above table).

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/endpoints/ed2010d5-b7c3-41cf-9025-585ebfc77c79' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session' \
--data '{
  "customerId": "0a40637055e84074b606cf50119d7c6d",
  "name": "test_alert_ep",
  "endpointType": "webhook-basic",
  "endpointRole": "source",
  "description": "test_EDIT_ep_webhook_api",
  "attributes": {},
  "enabled": "Yes",
  "publishToStreamFlag": false,
  "publishStreamType": "NATS",
  "publishToStreamOnlyFlag": false
}'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/09091567-785b-43ab-84b4-4aca1a19e23a" />

---
## Common Configuration Management

### Get a specific Endpoint using endpoint_id

#### Endpoint:
GET `/api/v2/organizations/configuration/endpoints/{endpoint_id}`

#### Description:
Retrieve details of a specific event endpoint.

#### Path Parameters:
- `endpoint_id` (string): ID of the endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/ed2010d5-b7c3-41cf-9025-585ebfc77c79' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1497" height="878" alt="image" src="https://github.com/user-attachments/assets/58b4b5f3-9058-4418-8773-125780105c12" />

### Enable an Existing Endpoint

#### Endpoint:
PUT `/api/v2/organizations/configuration/endpoints/{endpoint_id}/enable`

#### Description:
Enable an existing configuration event endpoint.

#### Path Parameters:
- `endpoint_id` (string): ID of the endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/ed2010d5-b7c3-41cf-9025-585ebfc77c79/enable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1501" height="523" alt="image" src="https://github.com/user-attachments/assets/099929df-a75d-4931-808a-b80bfa5fbacb" />

### Disable an Existing Endpoint

#### Endpoint:
PUT `/api/v2/organizations/configuration/endpoints/{endpoint_id}/disable`

#### Description:
Disable an existing configuration event endpoint.

#### Path Parameters:
- `endpoint_id` (string): ID of the endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/ed2010d5-b7c3-41cf-9025-585ebfc77c79/disable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1501" height="523" alt="image" src="https://github.com/user-attachments/assets/e3b77e1b-8bc6-47f2-a469-3a313aa028ac" />

### Delete a specific Endpoint using endpoint_id

#### Endpoint:
DELETE `/api/v2/organizations/configuration/endpoints/{endpoint_id}`

#### Description:
Delete a specific event endpoint from the system.

#### Path Parameters:
- `endpoint_id` (string): ID of the endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/organizations/configuration/endpoints/ed2010d5-b7c3-41cf-9025-585ebfc77c79' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1501" height="523" alt="image" src="https://github.com/user-attachments/assets/79703b69-d229-4dab-a4ee-d953c5b530ad" />

---

## Usage Notes

> [!IMPORTANT]
> The APIs for incident & message endpoints follow the same pattern as the alert endpoints documented. You can use these examples as a template for incident and message endpoint management by replacing "alerts" with "incidents" or "messages" in the endpoint URLs and following the same request/response structure.

### For Incident Endpoints
To manage incident endpoints, use the same API structure but replace "alerts" with "incidents" in the URLs:
- `GET /api/v2/organizations/organization/{id}/configuration/incidents/endpoints`
- `POST /api/v2/organizations/organization/{id}/configuration/incidents/endpoints`
- `PUT /api/v2/organizations/organization/{id}/configuration/incidents/endpoints/{endpoint_id}`

### For Message Endpoints
To manage message endpoints, use the same API structure but replace "alerts" with "messages" in the URLs:
- `GET /api/v2/organizations/organization/{id}/configuration/messages/endpoints`
- `POST /api/v2/organizations/organization/{id}/configuration/messages/endpoints`
- `PUT /api/v2/organizations/organization/{id}/configuration/messages/endpoints/{endpoint_id}`

### Authentication
All endpoints require proper authentication.

### Error Handling
All endpoints return appropriate HTTP status codes and error messages for various scenarios such as:
- Invalid organization ID
- Invalid endpoint ID
- Missing required parameters
- Authentication failures
