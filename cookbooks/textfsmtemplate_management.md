# TextFsmTemplate

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.

## Add a TextFsmTemplate

### Endpoint:
POST `/api/v2/textfsms`

### Description:
Add a textfsm template to the system.

### Request Body:
The body of the request should contain the textfsm in json format only.

### Example Request:
```shell cURL
curl --location --request POST 'https://10.95.125.95/api/v2/textfsms' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z649V|Z647s' \
--data '{
  "description": "Extracts email addresses from logs",
  "folder": "Default",
  "name": "EmailExtraction",
  "sample_input": "Email: john.doe@example.com\nEmail: alice.smith@company.org\nEmail: bob@subdomain.website.co.uk\nEmail: invalid-email@missingdotcom",
  "textfsm_template": "Value USERNAME (\\S+)\nValue DOMAIN (\\S+\\.\\S+)\n\nStart\n  ^Email: ${USERNAME}@${DOMAIN} -> Record"
}'
```
### Output:
![add_textfsmtemplate_output](<Screenshot 2025-02-14 001753.png>)


## Get a TextFsmTemplate

### Endpoint:
GET `/api/v2/textfsms/textfsm/{name}/view`

### Description:
This endpoint retrieves a specific textfsm template by it's name.

### Path Parameters:
- `name` (string): The name of the textfsm template. **Required.**

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/textfsms/textfsm/EmailExtraction/view' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z65AZ|Z647s'
```
### Output:
![get_a_specific_textfsmtemplate_output](<Screenshot 2025-02-14 005754.png>)


## Validate a TextFsmTemplate

### Endpoint:
POST `/api/v2/textfsms/validate_template`

### Description:
Validate a textfsm template.

### Request Body:
The body of the request should contain the textfsm in json format only.

### Example Request:
```shell cURL
curl --location --request POST 'https://10.95.125.95/api/v2/textfsms/validate_template' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z65IQ|Z65IQ' \
--data '{
  "sample_input": "Email: john.doe@example.com\nEmail: alice.smith@company.org\nEmail: bob@subdomain.website.co.uk\nEmail: invalid-email@missingdotcom",
  "textfsm_template": "Value USERNAME (\\S+)\nValue DOMAIN (\\S+\\.\\S+)\n\nStart\n  ^Email: ${USERNAME}@${DOMAIN} -> Record"
}'
```
### Output:

![validate_textfsmtemplate_output](<Screenshot 2025-02-14 010314.png>)


## Edit a TextFsmTemplate

### Endpoint:
PUT `/api/v2/textfsms/textfsm/{name}`

### Description:
Edit an existing textfsm template by updating description, folder, sample input and template details.

### Request Parameters:
- **name** (Path parameter): The name of the textfsm template to be edited or created if it does not exist.

### Example Request:
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/textfsms/textfsm/EmailExtraction' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z65ML|Z65IQ' \
--data '{
  "description": "Email address has been updated",
  "folder": "Default",
  "sample_input": "Email: john.doe@example.com\nEmail: alice.smith@company.org\nEmail: bob@subdomain.website.co.uk\nEmail: invalid-email@missingdotcom",
  "textfsm_template": "Value USERNAME (\\S+)\nValue DOMAIN (\\S+\\.\\S+)\n\nStart\n  ^Email: ${USERNAME}@${DOMAIN} -> Record"
}'
```

### Output:
![update_textfsmtemplate_output](<Screenshot 2025-02-14 012243.png>)


## Delete a TextFsmTemplate

### Endpoint:
DELETE `/api/v2/textfsms/textfsm/{name}`

### Description:
Delete a specified textfsm template from the system.

### Request Parameters:
- **name** (Path parameter): The name of the textfsm template to delete.

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/textfsms/textfsm/EmailExtraction' \
--header 'Accept: application/json' \
--header 'Authorization: {{apiKey}}' \
--header 'Cookie: __cfxsession=0cc6c274-df93-40c8-a782-d6ad0a8e0dcd; cfx_saas_session=9f9270b4ac37488fbd1dadf0dd2ee303; rdafportal=rdaf-portal-1|Z65ML|Z65IQ'
```

### Output:
![delete_textfsmtemplate_output](<Screenshot 2025-02-14 012359.png>)