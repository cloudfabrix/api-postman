# Rda-Packs

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

## Upload a Pack

### Endpoint:
POST `/api/v2/rda_packs/rda_pack/upload`

### Description:
Upload a new pack to the system.

### Request Body:
The body of the request should include a tar file for upload.

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/rda_packs/rda_pack/upload' \
--header 'Content-Type: multipart/form-data' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=10fca3a8-6134-4d5e-ada0-6793e004c1e3; cfx_saas_session=8d97e96c720945a4bbf5e432ce2cfe65; rdafportal=rdaf-portal-1|Z65VA|Z65Tn' \
--form 'file=@"Solutions Base Pack.tar.gz"'
```

### Output:

![upload_rda_packs_output](<Screenshot 2025-02-14 015656.png>)


## Activate a Rda-Pack

### Endpoint:
PUT `/api/v2/rda_packs/rda_pack/{name}/{version}/status`

### Description:
This endpoint activates a rda-packs.

### Path Parameters:
- `name` (string): The name of the rda pack. **Required.**
- `version` (string): The version of the rda pack. **Required.**
- `activate ` (bool): If set to `true`, the rda-pack will be activated. 

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/rda_packs/rda_pack/Solutions Base Pack/2.0.0/status?activate=true' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=10fca3a8-6134-4d5e-ada0-6793e004c1e3; cfx_saas_session=8d97e96c720945a4bbf5e432ce2cfe65; rdafportal=rdaf-portal-1|Z65YQ|Z65Tn'
```
### Output:
![activate_rda_pack_output](<Screenshot 2025-02-14 020943.png>)

## Deactivate a Rda-Pack

### Endpoint:
PUT `/api/v2/rda_packs/rda_pack/{name}/{version}/status`

### Description:
This endpoint deactivates a rda-packs.

### Path Parameters:
- `name` (string): The name of the rda pack. **Required.**
- `version` (string): The version of the rda pack. **Required.**
- `activate ` (bool): If set to `false`, the rda-pack will be deactivated. 

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/rda_packs/rda_pack/Solutions Base Pack/2.0.0/status?activate=false' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z65AZ|Z647s'
```
### Output:
![deactivate_rda_pack_output](<Screenshot 2025-02-14 021452.png>)


## Delete a Rda-Pack

### Endpoint:
DELETE `/api/v2/rda_packs/rda_pack/{name}/{version}/delete`

### Description:
This endpoint deletes a rda-packs.

### Path Parameters:
- `name` (string): The name of the rda pack. **Required.**
- `version` (string): The version of the rda pack. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/rda_packs/rda_pack/Solutions Base Pack/2.0.0/delete' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=10fca3a8-6134-4d5e-ada0-6793e004c1e3; cfx_saas_session=8d97e96c720945a4bbf5e432ce2cfe65; rdafportal=rdaf-portal-1|Z65aS|Z65Tn'
```
### Output:
![delete_rda_pack_output](<Screenshot 2025-02-14 021755.png>)