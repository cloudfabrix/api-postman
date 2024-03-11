# Add User Group
/api/v2/user_groups Add user group

#### Parameters

|Parameter      |Type     |Description                       |
|------------   |-------- |----------------------------------|
|name           |string   |Name of the user group            |
|profile        |string   |Profile for role of the user group|
|selection_type |string   |cfxql_filter / tabular_report     |
|project_cfxql  |string   |cfxql filter to get Organizations |
|projects       |list     |Organization names and ID details in a JSON object|



#### Profile details for each role

|Profile               |Label                             |
|------------          |----------------------------------|
|msp-admin             |MSP Administrator                 |
|msp-user              |MSP User                          |
|msp-user-read-only    |MSP Read Only User                |
|tenant-admin-profile  |Organization Administrator        |
|tenant-user-profile   |Organization User                 |
|tenant-user-read-only |Organization User Read Only       |
|l3-user               |L3 User                           |
|l1-user               |L1 User                           |

selection_type is either project_cfxql or tabular_report

Organizations details can be retrieved using the /api/v2/organizations (Get Organizations) API

project_cfxql: Organizations can be filtered by name using 'customerName'.

Example project_cfxql:

    1. customerName is 'CloudFabrix'
    2. customerName in ['CloudFabrix','Acme']

projects: List of organization names and IDs as 'customerName' and 'customerId' in JSON object.

Example projects:

    1. [{"customerName": "‘CloudFabrix’","customerId":"67deec38-9ac8-11ee-8514-0242ac120005"}]
	
    2. [{"customerName": "‘CloudFabrix’","customerId":"67deec38-9ac8-11ee-8514-0242ac120005"}, {"customerName": "Acme","customerId":"64374b96-a66e-11ee-9eda-0242ac12000a"} ]



## Sample Request to Create a User Group with MSP Administrator Role and assign multiple Organizations to it

This example will create a user group named "test-UserGroup" with the role of msp-admin (MSP Administrator), and Organizations CloudFabrix and Acme will be assigned to it.

using cfxql_filter as selection_type

```shell Curl
curl --location 'https://10.95.108.94/api/v2/user_groups' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=92f7e108-703a-40cd-a8c8-80b4737fa041; cfx_saas_session=3d0b10538c944bd38acd11a9da256721; rdafportal=rdaf-portal-1|Zeq80|Zeq8u' \
--data '{"name": "test1-UserGroup",
"profile": "msp-admin",
"selection_type": "cfxql_filter",
"project_cfxql": "customerName in ['\''CloudFabrix'\'', '\''Acme'\'']"
}'
```

using tabular_report as selection_type

```shell Curl
curl --location 'https://10.95.108.94/api/v2/user_groups' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=92f7e108-703a-40cd-a8c8-80b4737fa041; cfx_saas_session=3d0b10538c944bd38acd11a9da256721; rdafportal=rdaf-portal-1|Zeq80|Zeq8u' \
--data '{"name": "test1-UserGroup",
"profile": "msp-admin",
"selection_type": "tabular_report",
"projects": [{"customerName": "‘CloudFabrix’","customerId":"67deec38-9ac8-11ee-8514-0242ac120005"}]
}'
```

## Output
![add_user_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/1325c7a9-9f12-4162-8c4f-cd5986698985)


## Sample Request to Create a User Group with Organization Administrator Role

This example will create a user group named "test-UserGroup" with the role of tenant-admin (Organization Administrator), and Organization "CloudFabrix" will be assigned to it.

using cfxql_filter as selection_type

```shell Curl
curl --location 'https://10.95.108.90/api/v2/user_groups' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=0d561b1a-d06e-41ef-b0e3-710b1d861661; cfx_saas_session=8379937699c546cbadf054fb999aff03; rdafportal=rdaf-portal-1|Zeqtm|ZeqsD' \
--data '{"name": "test-UserGroup",
"profile": "tenant-admin-profile",
"selection_type": "cfxql_filter",
"project_cfxql": "customerName is '\''CloudFabrix
'\''"
}'
```

## Output
![add_user_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/56705ecd-9241-4a29-a2f2-396878da30e9)


# Edit User Group

/api/v2/user_groups/user_group/{name} Edit user group

#### Parameters

|Parameter      |Type     |Description                       |
|------------   |-------- |----------------------------------|
|name           |string   |Name of the user group            |
|profile        |string   |Profile for role of the user group|
|selection_type |string   |cfxql_filter / tabular_report     |
|project_cfxql  |string   |cfxql filter to get Organizations |
|tenantId       |string   |Tenant ID associated for the user |
|projects       |list     |Organization names and ID details in a JSON object|

tenantId can be retrieved from user login API output

#### tenantId

![tenantId](https://github.com/cloudfabrix/api-postman/assets/121096522/3b7a6166-de70-482d-b74a-dacf561c8fe3)



## Sample Request to edit User Group
This example will edit a user group named "test-UserGroup" with the role of tenant-user (Organization User Read Only), and Organization "Acme" will be assigned to it.

using cfxql_filter as selection_type

```shell Curl
curl --location --request PUT 'https://10.95.108.94/api/v2/user_groups/user_group/test-UserGroup' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=92f7e108-703a-40cd-a8c8-80b4737fa041; cfx_saas_session=3d0b10538c944bd38acd11a9da256721; rdafportal=rdaf-portal-1|Zeq80|Zeq8u' \
--data '{
"profile": "tenant-user-read-only",
"selection_type": "cfxql_filter",
"project_cfxql": "customerName is '\''Acme'\''",
"tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
}'
```

using tabular_report as selection_type

```shell Curl
curl --location --request PUT 'https://10.95.108.94/api/v2/user_groups/user_group/test-UserGroup' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=92f7e108-703a-40cd-a8c8-80b4737fa041; cfx_saas_session=3d0b10538c944bd38acd11a9da256721; rdafportal=rdaf-portal-1|Zeq80|Zeq8u' \
--data '{
"profile": "tenant-user-read-only",
"selection_type": "tabular_report",
"projects": [{"customerName": "‘Acme’","customerId":"64374b96-a66e-11ee-9eda-0242ac12000a"}],
"tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
}'
```

## Output
![edit_user_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/8b2c7c90-2a10-4f72-b21e-3db10da609e9)

