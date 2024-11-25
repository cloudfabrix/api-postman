# Credentials

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

## Get Credential Types

### Endpoint:
GET `/api/v2/credentials/types`

### Description:
Fetch all available credential types.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/credentials/types' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0ONa|Z0OHY'
```

### Output:
![get_all_cred_types](https://github.com/user-attachments/assets/7c7a17d0-ab47-48ac-942a-6518c7d40805)


## Get Credential Type Fields

### Endpoint:
GET `/api/v2/credentials/types/{type}`

### Description:
Fetch the fields required for a specific credential type.

### Path Parameter:
- `type` (string): The credential type for which the fields are being requested.

### Request Parameters:
This endpoint only requires the `type` path parameter.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/credentials/types/ssh-cred' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0ON7|Z0OHY'
```

### Output:
![get_fields_of_a_cred_type](https://github.com/user-attachments/assets/7290ae08-702f-43b9-96bc-f2bdc0dfbc61)



## Add a Credential

### Endpoint:
POST `/api/v2/credentials`

### Description:
Add a credential to the system.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/credentials' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0N/B|Z0N/B' \
--data '{
  "add_to_default_site_profile": true,
  "type": "ssh-cred",
  "host": "10.95.125.95",
  "name": "jack95_ssh_credential",
  "username": "jack95",
  "password": "xadqwhusnizmo-janygqwegdl",
  "port": 22,
  "sites": "*"
}'
```

### Output:
![add_credential_output](https://github.com/user-attachments/assets/392d4082-cea8-4e9a-b7f9-7380dbc83864)



## Edit a Credential

### Endpoint:
PUT `/api/v2/credentials/credential/{name}`

### Description:
Edit an existing credential by updating its configuration or authentication details. If the credential does not exist, it will be added to the system.

### Request Parameters:
- **name** (Path parameter): The name of the credential to be edited or created if it does not exist.

### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/credentials/credential/jack95_ssh_credential' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0OHr|Z0OHY' \
--data '{
  "add_to_default_site_profile": false,
  "type": "ssh-cred",
  "host": "10.95.125.96",
  "username": "jack96",
  "password": "xadqwhusnizmo-janygqwegdl",
  "port": 21,
  "sites": "*"
}'
```

### Output:
![edit_credential_output](https://github.com/user-attachments/assets/95eede14-be02-4bf8-b3c3-fd6db1571d1d)



## Verify Connectivity and Credential Validity

### Endpoint:
POST `/api/v2/credentials/credential/{name}/verify`

### Description:
Check connectivity and verify the credentials, ensuring that connectivity is established and credentials are valid.

### Request Parameters:
- **name** (Path parameter): The name of the credential to verify.
- **sites** (Query parameter, optional): A regular expression used to select worker sites. Defaults to `*` if not provided.

### Example Request:
```shell cURL
curl --location --request POST 'https://10.95.125.95/api/v2/credentials/credential/jack95_ssh_credential/verify?sites=*' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0OJH|Z0OHY'
```

### Output:
![verify_cred_failed_output](https://github.com/user-attachments/assets/a2b46e4d-28c2-4da8-9997-e7825f7bbb1b)



Updated again with valid credential & verified check connectivity (Below Output).

![verify_cred_OK_output](https://github.com/user-attachments/assets/8fa77606-b168-45d3-bc6b-ba9026da5912)



## Delete a Credential

### Endpoint:
DELETE `/api/v2/credentials/credential/{name}`

### Description:
Delete a specified credential from the system.

### Request Parameters:
- **name** (Path parameter): The name of the credential to delete.

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/credentials/credential/jack95_ssh_credential' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0OLy|Z0OHY'
```

### Output:
![delete_credential_output](https://github.com/user-attachments/assets/ea0335b7-bae2-431d-a5fc-af1b212d3d82)
