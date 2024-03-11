# Add Dashboard Group

/api/v2/dashboard_groups Add dashboard group

Parameters

|Parameter      |Type     |Description                             |
|------------   |-------- |----------------------------------      |
|name           |string   |Name of the dashboard group             |
|label          |string   |Label for the dashboard group           |
|description    |string   |Description for the dashboard group     |
|enabled        |boolean  |true / false to enable or disable       |
|userGroups     |list     |User group names and tenant Id details in a JSON object|
|dashboardList  |list     |Dashboard names and ID details in a JSON object |



Example userGroups: 

    1. [{"name": "msp_admin", "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"}]

	2. [{"name": "msp_admin", "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"}, {"name": "tenant-admin", "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"}]

Example dashboardList:

	 1. [{"name": "oia-incidents-app", "id": "user-dashboard-oia-incidents-app"}]
	
	 2. [{"name": "oia-incidents-app", "id": "user-dashboard-oia-incidents-app"}, {"name": "oia-alerts-os", "id": "user-dashboard-oia-alerts-os"}]


tenantId can be retrieved from user login API output
![tenantId](https://github.com/cloudfabrix/api-postman/assets/121096522/a23f6cc4-9754-486a-818c-fba5c3cb021e)



## Sample Request to Create a Dashboard Group with a user group and assign a dashboard to it

This example will create a dashboard group named 'test' with 'msp_admin' users, and the 'oia-incidents-ap' dashboard will be assigned to it.

```shell Curl
curl --location 'https://10.95.108.94/api/v2/dashboard_groups' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "name": "test",
    "label": "test group",
    "description": "test group",
    "userGroups": [
        {
            "name": "msp_admin",
            "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
        }
    ],
    "dashboardList": [
        {
            "name": "oia-incidents-app",
            "id": "user-dashboard-oia-incidents-app"
        }
    ],
    "enabled": true
}'
```

## Output
![add_dashboard_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/459356f9-c62b-4793-acf7-a55eb81b5790)




## Sample Request to Create a Dashboard Group with multiple user groups and assign multiple dashboards to it

This example will create a dashboard group named 'test' with 'msp_admin' and 'tenant_admin' user groups, and dashboards ‘oia-incidents-app' and 'oia-alerts-os’ will be assigned to it.

```shell Curl
curl --location 'https://10.95.108.94/api/v2/dashboard_groups' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=949a3a8f-bf3e-4cb7-9536-3ea903ee9094; cfx_saas_session=49e6385cfd2e4ef9a1706c5bd2cf1066; rdafportal=rdaf-portal-1|Ze8E+|Ze8E3' \
--data '{
    "name": "test",
    "label": "test group",
    "description": "test group",
    "userGroups": [
        {
            "name": "msp_admin",
            "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
        },
        {
            "name": "tenant_admin",
            "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
        }
    ],
    "dashboardList": [
        {
            "name": "oia-incidents-app",
            "id": "user-dashboard-oia-incidents-app"
        },
        {
            "name": "oia-alerts-os",
            "id": "user-dashboard-oia-alerts-os"
        }
    ],
    "enabled": true
}'
```

## Output
![add_dashboard_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/36e9ea16-9b36-4c18-8d47-8dd5e92867f0)




# Edit Dashboard Group

/api/v2/dashboard_groups/dashboard_group/{name}  Edit dashboard group

Parameters

|Parameter      |Type     |Description                             |
|------------   |-------- |----------------------------------      |
|name           |string   |Name of the dashboard group             |
|label          |string   |Label for the dashboard group           |
|description    |string   |Description for the dashboard group     |
|enabled        |boolean  |true / false to enable or disable       |
|userGroups     |list     |User group names and tenant Id details in a JSON object|
|dashboardList  |list     |Dashboard names and ID details in a JSON object |


## Sample Request to Edit a Dashboard Group

This example will update the dashboard group named 'test' with ‘test-UserGroup’ user group, and dashboards ‘oia-my-incidents' and 'oia-alerts-os’ will be assigned to it.

```shell Curl
curl --location --request PUT 'https://10.95.108.94/api/v2/dashboard_groups/dashboard_group/test' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Cookie: __cfxsession=949a3a8f-bf3e-4cb7-9536-3ea903ee9094; cfx_saas_session=49e6385cfd2e4ef9a1706c5bd2cf1066; rdafportal=rdaf-portal-1|Ze8JK|Ze8E3' \
--data '{
    "name": "test",
    "label": "test group",
    "description": "test group",
    "userGroups": [
        {
            "name": "test-UserGroup",
            "tenantId": "41b4c17c-13f4-4514-9ea7-c21083728eeb"
        }
    ],
    "dashboardList": [
        {
            "name": "oia-my-incidents",
            "id": "user-dashboard-oia-incidents-app"
        },
        {
            "name": "oia-alerts-os",
            "id": "user-dashboard-oia-alerts-os"
        }
    ],
    "enabled": true
}'
```

## Output
![edit_dashboard_group_output](https://github.com/cloudfabrix/api-postman/assets/121096522/d159b886-5a85-4863-8be6-329b3a784c13)




