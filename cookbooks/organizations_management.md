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
---

## Alert Mappings Management

### Get All Alert Mappings of an Organization

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/alerts/mappings`

#### Description:
Retrieve all alert mappings configured for a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Query Parameters:
| Parameter | Type    | Description                                    |
|-----------|---------|------------------------------------------------|
| `offset`  | integer | Offset to start the results from (default: 0)  |
| `limit`   | integer | Maximum number of results to return (default: 100) |

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/mappings?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/2ee9c00d-b0f5-40de-bf2a-36dd1bc1057c" />

### Add an Alert Mapping in an Organization

#### Endpoint:
POST `/api/v2/organizations/organization/{id}/configuration/alerts/mappings`

#### Description:
Add a new alert mapping to a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Request Body Parameters:
| Parameter                  | Type    | Description                                    |
|----------------------------|---------|------------------------------------------------|
| `customerId`               | string  | Customer ID (required)                         |
| `name`                     | string  | Mapping name (required)                         |
| `description`              | string  | Mapping description (optional)                 |
| `enabled`                  | boolean | Enable status (default: true)                 |
| `sourceId`                 | string  | Source endpoint ID (required)                  |
| `targetId`                 | string  | Target endpoint ID (required)                 |
| `sourcemapper`             | array   | Array of source mappers (required)            |
| `sourcepipeline`           | array   | Array of source pipelines (required)          |
| `mappingtype`              | string  | Type of mapping (optional)                     |
| `mappingscript`            | string  | Mapping script (optional)                      |

#### Important Notes:
- **SourceId and TargetId**: Use the `GET /api/v2/organizations/organization/{id}/configuration/alerts/endpoints` API to get endpoint IDs. Use `endpointId` where `endpointRole==source` as `sourceId` and `endpointId` where `endpointRole==target` as `targetId`.
- **Sourcemappers**: Use `GET /api/v2/organizations/configuration/sourcemappers/{source_id}` to fetch available mappers for the source endpoint.
- **Sourcepipelines**: Use `GET /api/v2/organizations/configuration/sourcepipelines/{source_id}` to fetch available pipelines for the source endpoint.

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/mappings' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session' \
--data '{
  "name": "api-added-mapper-name",
  "customerId": "90cfaf66242f4976a7dd3b598c71c2fb",
  "description": "api-added-mapper-desciption",
  "enabled": true,
  "sourceId": "99efd89b-1a7c-4aa6-b9e1-d7d715419b0f",
  "targetId": "eaa09c94-972e-4f38-88d6-00c14b2648fe",
  "sourcemapper": [
    {
      "name": "default.mapper-cfxpulse-json",
      "bundle_name": "default",
      "artifact": "cfxpulse_json.json"
    }
  ],
  "sourcepipeline": [
    {
      "name": "default.pipeline-default",
      "bundle_name": "default"
    }
  ]
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/62203b30-feaf-4247-83ee-64827d6fd3be" />

### Update an Alert Mapping of an Organization

#### Endpoint:
PUT `/api/v2/organizations/organization/{id}/configuration/alerts/mappings/{mapping_id}`

#### Description:
Update an existing alert mapping in a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**
- `mapping_id` (string): ID of the mapping. **Required.**

#### Request Body Parameters:
Same as Add Alert Mapping (see above table).

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/alerts/mappings/mapping-uuid-here' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session' \
--data '{
  "name": "api-added-mapper-name",
  "customerId": "90cfaf66242f4976a7dd3b598c71c2fb",
  "description": "api-added-mapper-desciption-updated",
  "enabled": false,
  "sourceId": "99efd89b-1a7c-4aa6-b9e1-d7d715419b0f",
  "targetId": "eaa09c94-972e-4f38-88d6-00c14b2648fe",
  "sourcemapper": [
    {
      "name": "default.mapper-cfxpulse-json",
      "bundle_name": "default",
      "artifact": "cfxpulse_json.json"
    }
  ],
  "sourcepipeline": [
    {
      "name": "default.pipeline-default",
      "bundle_name": "default"
    }
  ]
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/db4e0519-51b3-4943-8bc8-da5628c58e6f" />

---

## Usage Notes for Mappings

> [!IMPORTANT]
> The APIs for incident & message mappings follow the same pattern as the alert mappings documented above. You can use these examples as a template for incident and message mapping management by replacing "alerts" with "incidents" or "messages" in the endpoint URLs and following the same request/response structure.

### For Incident Mappings
To manage incident mappings, use the same API structure but replace "alerts" with "incidents" in the URLs:
- `GET /api/v2/organizations/organization/{id}/configuration/incidents/mappings`
- `POST /api/v2/organizations/organization/{id}/configuration/incidents/mappings`
- `PUT /api/v2/organizations/organization/{id}/configuration/incidents/mappings/{mapping_id}`

### For Message Mappings
To manage message mappings, use the same API structure but replace "alerts" with "messages" in the URLs:
- `GET /api/v2/organizations/organization/{id}/configuration/messages/mappings`
- `POST /api/v2/organizations/organization/{id}/configuration/messages/mappings`
- `PUT /api/v2/organizations/organization/{id}/configuration/messages/mappings/{mapping_id}`

---

## Additional Configuration APIs

### Get Source Mappers for a Source Endpoint

#### Endpoint:
GET `/api/v2/organizations/configuration/eventmappers/{source_id}`

#### Description:
Fetch available source mappers for a specific source endpoint. This is useful for understanding what mappers are available when creating mappings.

#### Path Parameters:
- `source_id` (string): ID of the source endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/eventmappers/99efd89b-1a7c-4aa6-b9e1-d7d715419b0f' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/4087987c-c5d5-425c-ab03-81cb38062591" />

### Get Source Pipelines for a Source Endpoint

#### Endpoint:
GET `/api/v2/organizations/configuration/eventpipelines/{source_id}`

#### Description:
Fetch available source pipelines for a specific source endpoint. This is useful for understanding what pipelines are available when creating mappings.

#### Path Parameters:
- `source_id` (string): ID of the source endpoint. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/eventpipelines/99efd89b-1a7c-4aa6-b9e1-d7d715419b0f' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/fb1070c6-4abb-428c-819c-79aff3551110" />

---

## Common Configuration Management

### Get a specific Mapping using mapping_id

#### Endpoint:
GET `/api/v2/organizations/configuration/mappings/{mapping_id}`

#### Description:
Retrieve details of a specific mapping.

#### Path Parameters:
- `mapping_id` (string): ID of the mapping. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/mappings/mapping-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/21be99b1-8baa-4b3d-9ede-cd67d812388f" />

### Enable an Existing Mapping

#### Endpoint:
PUT `/api/v2/organizations/configuration/mappings/{mapping_id}/enable`

#### Description:
Enable an existing configuration mapping.

#### Path Parameters:
- `mapping_id` (string): ID of the mapping. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/mappings/mapping-uuid-here/enable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/374f29f1-a388-4584-bbc1-670e8119619d" />

### Disable an Existing Mapping

#### Endpoint:
PUT `/api/v2/organizations/configuration/mappings/{mapping_id}/disable`

#### Description:
Disable an existing configuration mapping.

#### Path Parameters:
- `mapping_id` (string): ID of the mapping. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/mappings/mapping-uuid-here/disable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/d4164dde-a386-4d10-a59d-7195897633db" />

### Delete a specific Mapping using mapping_id

#### Endpoint:
DELETE `/api/v2/organizations/configuration/mappings/{mapping_id}`

#### Description:
Delete a specific mapping from the system.

#### Path Parameters:
- `mapping_id` (string): ID of the mapping. **Required.**

#### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/organizations/configuration/mappings/mapping-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/853a252a-8f45-4da8-94ea-6f6cf66c46c9" />

---

## Correlation Policies Management

### Get All Correlation Policies of an Organization

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/policies/correlation`

#### Description:
Retrieve all correlation policies configured for a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Query Parameters:
| Parameter | Type    | Description                                    |
|-----------|---------|------------------------------------------------|
| `offset`  | integer | Offset to start the results from (default: 0)  |
| `limit`   | integer | Maximum number of results to return (default: 100) |

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/policies/correlation?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/74503399-df51-416d-82cd-c5714399f73a" />

### Add a Correlation Policy in an Organization

#### Endpoint:
POST `/api/v2/organizations/organization/{id}/configuration/policies/correlation`

#### Description:
Add a new correlation policy to a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Request Body Parameters:
| Parameter                          | Type    | Description                                    |
|------------------------------------|---------|------------------------------------------------|
| `customerId`                       | string  | Customer ID (required)                         |
| `name`                             | string  | Policy name (required)                         |
| `description`                      | string  | Policy description (optional)                 |
| `enabled`                          | boolean | Enable status (default: true)                 |
| `policytype`                       | string  | Type of correlation policy (required)         |
| `precedence`                       | integer | Policy precedence (required)                   |
| `filterType`                       | string  | Filter type: "Basic" or "Advanced" (required)   |
| `groupExpiry`                      | integer | Group expiry time in minutes (optional)       |
| `groupMaximumSeverity`             | string  | Maximum severity for group (optional)         |
| `grouplimit`                       | integer | Group limit (optional)                        |
| `autoClearafterLastUpdate`         | integer | Auto clear after last update (optional)       |
| `autoResolveIncidentWhenAlertsCleared` | boolean | Auto resolve incident when alerts cleared (optional) |
| `groupBy`                          | array   | Array of fields to group by (optional)        |
| `filter`                           | string  | Advanced filter expression (optional)         |
| `selectionCriteria`                | array   | Selection criteria array (optional)           |
| `relationshipmap`                  | string  | Relationship map name (for topology correlation) |
| `graph`                            | array   | Graph configuration (for topology correlation) |

#### Policy Types:
- `CORRELATE_BURST`: Correlation burst policy
- `TOPOLOGY_CORRELATION`: Topology-based correlation policy
- `CORRELATE_GROUP`: Correlation group policy

#### Important Notes:
- **Alert Attributes**: Use `GET /api/v2/organizations/organization/{id}/configuration/policies/correlation/alert-attributes` to fetch available alert attributes for use in `groupBy` fields.
- **Selection Criteria**: Used for filtering alerts based on specific conditions.

#### Example Request (Correlate Burst):
```shell cURL
curl --location --globoff '{{baseUrl}}/api/v2/organizations/organization/{{projectId}}/configuration/policies/correlation' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "autoClearafterLastUpdate": 0,
  "autoResolveIncidentWhenAlertsCleared": true,
  "customerId": "{{customerId}}",
  "description": "desc_CBP",
  "enabled": true,
  "filter": "data~'\''alertType'\''",
  "filterType": "Advanced",
  "groupBy": [
    "sourcemechanism"
  ],
  "groupExpiry": 5,
  "groupMaximumSeverity": "CRITICAL",
  "grouplimit": 0,
  "name": "test_CBP",
  "policytype": "CORRELATE_BURST",
  "precedence": 4001,
  "selectionCriteria": []
}'
```

#### Example Request (Topology Correlation):
```shell cURL
curl --location --globoff '{{baseUrl}}/api/v2/organizations/organization/{{projectId}}/configuration/policies/correlation' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "autoClearafterLastUpdate": 0,
  "autoResolveIncidentWhenAlertsCleared": true,
  "customerId": "{{customerId}}",
  "description": "desc_CTP",
  "enabled": true,
  "filterType": "Basic",
  "groupExpiry": 5,
  "groupMaximumSeverity": "MAJOR",
  "grouplimit": 0,
  "name": "test_CTP",
  "policytype": "TOPOLOGY_CORRELATION",
  "precedence": 4000,
  "relationshipmap": "rdaf_topology_relationships",
  "graph": [
      {
          "graph_name": "cfx_rdaf_topology_graph",
          "db_name": "cfx_rdaf_topology",
          "edge_collection": "cfx_rdaf_topology_edges",
          "node_collection": "cfx_rdaf_topology_nodes"
      }
  ]
}'
```
#### Example Request (Correlate Group):
```shell cURL
curl --location --globoff '{{baseUrl}}/api/v2/organizations/organization/{{projectId}}/configuration/policies/correlation' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "autoClearafterLastUpdate": 0,
  "autoResolveIncidentWhenAlertsCleared": true,
  "customerId": "{{customerId}}",
  "description": "desc_CGP",
  "enabled": true,
  "filterType": "Basic",
  "groupBy": [
    "componentname"
  ],
  "groupExpiry": 5,
  "groupMaximumSeverity": "MAJOR",
  "grouplimit": 0,
  "name": "test_CGP",
  "policytype": "CORRELATE_GROUP",
  "precedence": 3999,
  "selectionCriteria": []
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/e6b94363-9beb-4681-9b78-004d874dab4d" />
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/65e05ecb-a520-46c0-a4a6-dda81ad17ca1" />
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/4f4c5a5d-dde4-4118-9354-4385291e5394" />

### Update a Correlation Policy of an Organization

#### Endpoint:
PUT `/api/v2/organizations/organization/{id}/configuration/policies/correlation/{policy_id}`

#### Description:
Update an existing correlation policy in a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**
- `policy_id` (string): ID of the policy. **Required.**

#### Request Body Parameters:
Same as Add Correlation Policy (see above table).

#### Example Request:
```shell cURL
curl --location --globoff --request PUT '{{baseUrl}}/api/v2/organizations/organization/string/configuration/policies/correlation/string' \
--header 'Authorization: <token>' \
--header 'Accept: application/json' \
--data '{
  "autoClearafterLastUpdate": 0,
  "autoResolveIncidentWhenAlertsCleared": true,
  "customerId": "0a4609dd6f634d44a55d6293de70181a",
  "description": "desc_CBP",
  "enabled": true,
  "filter": "data~'\''alertType'\''",
  "filterType": "Advanced",
  "groupBy": [
    "sourcemechanism"
  ],
  "groupExpiry": 5,
  "groupMaximumSeverity": "CRITICAL",
  "grouplimit": 0,
  "name": "test_CBP",
  "policytype": "CORRELATE_BURST",
  "precedence": 250,
  "selectionCriteria": [
    {
      "column-id": "assetname",
      "column-label": "Asset Name",
      "column-type": "TEXT",
      "condition": "contains",
      "description": "Contains",
      "label": "testLabel",
      "values": [
        "ciscomeraki"
      ]
    }
  ]
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/02ae5fa6-df29-4708-abc8-cd35dcce2a3d" />

### Get Alert Attributes for Correlation Policies

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/policies/correlation/alert-attributes`

#### Description:
Fetch available alert attributes that can be used in correlation policy `groupBy` fields.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/policies/correlation/alert-attributes' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/ed89a49f-962e-4354-8ca5-61d06f227167" />

### Get a specific Correlation Policy using policy_id

#### Endpoint:
GET `/api/v2/organizations/configuration/policies/correlation/{policy_id}`

#### Description:
Retrieve details of a specific correlation policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/policies/correlation/policy-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/d7e991ef-1e38-4a9a-a3f0-e5ac3f6ea47c" />
  
### Enable an Existing Correlation Policy

#### Endpoint:
PUT `/api/v2/organizations/configuration/policies/correlation/{policy_id}/enable`

#### Description:
Enable an existing correlation policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/policies/correlation/policy-uuid-here/enable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/1a4300e6-5f4e-4a43-9cfd-a73341084a66" />

### Disable an Existing Correlation Policy

#### Endpoint:
PUT `/api/v2/organizations/configuration/policies/correlation/{policy_id}/disable`

#### Description:
Disable an existing correlation policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/policies/correlation/policy-uuid-here/disable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/c035c913-dccf-4b3d-a6ab-973dc1bfcee4" />

### Delete a specific Correlation Policy using policy_id

#### Endpoint:
DELETE `/api/v2/organizations/configuration/policies/correlation/{policy_id}`

#### Description:
Delete a specific correlation policy from the system.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/organizations/configuration/policies/correlation/policy-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/9b1813e0-389e-4c3d-aa1e-7ce8bdff7f22" />

---

## Suppression Policies Management

### Get All Suppression Policies of an Organization

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/policies/suppression`

#### Description:
Retrieve all suppression policies configured for a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Query Parameters:
| Parameter | Type    | Description                                    |
|-----------|---------|------------------------------------------------|
| `offset`  | integer | Offset to start the results from (default: 0)  |
| `limit`   | integer | Maximum number of results to return (default: 100) |

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/policies/suppression?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/cb55ee9d-0b70-49c0-b00b-701a1ce9c684" />

### Add a Suppression Policy in an Organization

#### Endpoint:
POST `/api/v2/organizations/organization/{id}/configuration/policies/suppression`

#### Description:
Add a new suppression policy to a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Request Body Parameters:
| Parameter                          | Type    | Description                                    |
|------------------------------------|---------|------------------------------------------------|
| `customerId`                       | string  | Customer ID (required)                         |
| `name`                             | string  | Policy name (required)                         |
| `description`                      | string  | Policy description (optional)                 |
| `enabled`                          | boolean | Enable status (default: true)                 |
| `policytype`                       | string  | Type of suppression policy (required)         |
| `precedence`                       | integer | Policy precedence (required)                   |
| `filterType`                       | string  | Filter type: "Basic" or "Advanced" (required)   |
| `raisecount`                       | integer | Raise count threshold (optional)              |
| `raiserateseconds`                 | integer | Raise rate in seconds (optional)               |
| `revivesuppressedalerts`           | string  | Revive suppressed alerts setting (optional)    |
| `datasetfilter`                    | string  | Dataset filter type (optional)                 |
| `selecteddataset`                  | string  | Selected dataset name (optional: Based on filter type)               |
| `pstreamname`                      | string  | PStream name (optional: Based on filter type)                        |
| `autoResolveIncidentWhenAlertsCleared` | boolean | Auto resolve incident when alerts cleared (optional) |
| `groupExpiry`                      | integer | Group expiry time in minutes (optional)         |
| `autoClearafterLastUpdate`         | integer | Auto clear after last update (optional)        |
| `selectionCriteria`                | array   | Selection criteria array (optional)           |
| `flappingcount`                    | integer | Flapping count threshold (for flapping policies) |
| `flappingrateseconds`              | integer | Flapping rate in seconds (for flapping policies) |
| `schedule`                         | object  | Schedule configuration (for suppress policies)             |

#### Policy Types:
- `SUPPRESS_FLAPPING`: Suppress flapping alerts
- `SUPPRESS`: Suppress alerts based on schedule

#### Example Request (Suppress):
```
curl --location --globoff '{{baseUrl}}/api/v2/organizations/organization/{{projectId}}/configuration/policies/suppression' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "customerId": "{{customerId}}",
  "name": "test_SUP",
  "precedence": 10000,
  "description": "test_SUP_desc",
  "raisecount": 0,
  "raiserateseconds": 0,
  "revivesuppressedalerts": "revive",
  "datasetfilter": "NONE",
  "autoResolveIncidentWhenAlertsCleared": true,
  "groupExpiry": 5,
  "autoClearafterLastUpdate": 0,
  "filterType": "Basic",
  "selectionCriteria": [
    {
        "column-id": "componentname",
        "column-label": "Component Name",
        "condition": "==",
        "description": "Equals",
        "label": "testLabel",
        "column-type": "TEXT",
        "values": [
            "Processor"
        ]
    }
  ],
  "enabled": true,
  "policytype": "SUPPRESS",
  "schedule": {
        "scheduleType": "Once",
        "jobType": "duration",
        "scheduleTime": {
            "startDate": 1758469362417,
            "startTime": 1758469362417,
            "enableEnd": false,
            "enableDuration": true,
            "endDate": null
        },
        "timeZone": "Asia/Calcutta",
        "Minutes": {
            "minutesApart": 1
        },
        "Hourly": {
            "selector": "every_hour",
            "hoursApart": 1
        },
        "Daily": {
            "selector": "every_day",
            "daysApart": 1
        },
        "Weekly": {
            "days": [],
            "weeksApart": 1
        },
        "Monthly": {
            "selector": "choice_day_month",
            "choice_day": 1,
            "choice_month": 1,
            "rank": 1,
            "day": "MON",
            "monthcount": 1,
            "hourPart": 12,
            "minutePart": 0
        },
        "Yearly": {
            "selector": "choice_day_month",
            "month": 1,
            "month_2": 1,
            "rank": 1,
            "weekday": "MON",
            "day": 1,
            "monthcount": 1,
            "hourPart": 12,
            "minutePart": 0
        },
        "duration": {
            "duration_days": null,
            "duration_hours": "24",
            "duration_minutes": null
        }
    }
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/daf9bc80-9a3a-46e4-9b18-6d877f8b632f" />

### Update a Suppression Policy of an Organization

#### Endpoint:
PUT `/api/v2/organizations/organization/{id}/configuration/policies/suppression/{policy_id}`

#### Description:
Update an existing suppression policy in a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**
- `policy_id` (string): ID of the policy. **Required.**

#### Request Body Parameters:
Same as Add Suppression Policy (see above table).

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.94/api/v2/organizations/organization/e2ac5af6-96f5-11f0-82d5-0242ac160011/configuration/policies/suppression/f4af4e6d-6e9a-4ad2-a320-69020fc7cd82' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Cookie: __cfxsession=f6ab2107-afbf-4725-b075-bfb5e10b879b; rdafswagger=rdaf-swagger-1|aNBQt|aNBN9' \
--data '{
  "customerId": "90cfaf66242f4976a7dd3b598c71c2fb",
  "name": "test_SUP",
  "precedence": 10000,
  "description": "test_SUP_desc_edited",
  "raisecount": 0,
  "raiserateseconds": 0,
  "revivesuppressedalerts": "revive",
  "datasetfilter": "NONE",
  "autoResolveIncidentWhenAlertsCleared": true,
  "groupExpiry": 5,
  "autoClearafterLastUpdate": 0,
  "filterType": "Basic",
  "selectionCriteria": [
    {
        "column-id": "componentname",
        "column-label": "Component Name",
        "condition": "==",
        "description": "Equals",
        "label": "testLabelEdited",
        "column-type": "TEXT",
        "values": [
            "Processor"
        ]
    }
  ],
  "enabled": false,
  "policytype": "SUPPRESS",
  "schedule": {
        "scheduleType": "Once",
        "jobType": "duration",
        "scheduleTime": {
            "startDate": 1758469362417,
            "startTime": 1758469362417,
            "enableEnd": false,
            "enableDuration": true,
            "endDate": null
        },
        "timeZone": "Asia/Calcutta",
        "Minutes": {
            "minutesApart": 1
        },
        "Hourly": {
            "selector": "every_hour",
            "hoursApart": 1
        },
        "Daily": {
            "selector": "every_day",
            "daysApart": 1
        },
        "Weekly": {
            "days": [],
            "weeksApart": 1
        },
        "Monthly": {
            "selector": "choice_day_month",
            "choice_day": 1,
            "choice_month": 1,
            "rank": 1,
            "day": "MON",
            "monthcount": 1,
            "hourPart": 12,
            "minutePart": 0
        },
        "Yearly": {
            "selector": "choice_day_month",
            "month": 1,
            "month_2": 1,
            "rank": 1,
            "weekday": "MON",
            "day": 1,
            "monthcount": 1,
            "hourPart": 12,
            "minutePart": 0
        },
        "duration": {
            "duration_days": null,
            "duration_hours": "24",
            "duration_minutes": null
        }
    }
}'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/14d6fe64-fa04-40bb-ab13-c51a3fdb39e6" />

### Get a specific Suppression Policy using policy_id

#### Endpoint:
GET `/api/v2/organizations/configuration/policies/suppression/{policy_id}`

#### Description:
Retrieve details of a specific suppression policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/configuration/policies/suppression/policy-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/f9ae5a8c-3f79-4c50-b6cd-ccd08717de76" />

### Enable an Existing Suppression Policy

#### Endpoint:
PUT `/api/v2/organizations/configuration/policies/suppression/{policy_id}/enable`

#### Description:
Enable an existing suppression policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/policies/suppression/policy-uuid-here/enable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/102ab401-2eb0-4801-9250-fd398f2799b6" />

### Disable an Existing Suppression Policy

#### Endpoint:
PUT `/api/v2/organizations/configuration/policies/suppression/{policy_id}/disable`

#### Description:
Disable an existing suppression policy.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/organizations/configuration/policies/suppression/policy-uuid-here/disable' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/9e36788c-dc93-48aa-b982-3924be752f78" />

### Delete a specific Suppression Policy using policy_id

#### Endpoint:
DELETE `/api/v2/organizations/configuration/policies/suppression/{policy_id}`

#### Description:
Delete a specific suppression policy from the system.

#### Path Parameters:
- `policy_id` (string): ID of the policy. **Required.**

#### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/organizations/configuration/policies/suppression/policy-uuid-here' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/7ce78c28-c5aa-4567-9f32-8cb3bfb3d678" />

---

## Enriched Attributes Management

### Get Enriched Attributes of an Organization

#### Endpoint:
GET `/api/v2/organizations/organization/{id}/configuration/enriched_attributes`

#### Description:
Retrieve enriched attributes configuration for a specific organization.

#### Path Parameters:
- `id` (string): ID of the organization. **Required.**

#### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/organizations/organization/dcc5c8e8-92b1-11f0-857d-0242ac120006/configuration/enriched_attributes' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=your_session_id; cfx_saas_session=your_saas_session; rdafportal=rdaf-portal-1|your_portal_session'
```

#### Output:
<img width="1500" height="878" alt="image" src="https://github.com/user-attachments/assets/825c32f1-f588-43d8-aaf9-6014c8b4304a" />


---
