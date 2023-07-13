---
title: CloudFabrix RDA Platform API v3.2.2
language_tabs:
  - python: Python
  - java: java
language_clients:
  - python: ""
  - java: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="cloudfabrix-rda-platform-api">CloudFabrix RDA Platform API v3.2.2</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

CloudFabrix RDA Platform API

<h1 id="cloudfabrix-rda-platform-api-authentication">Authentication</h1>

## Login into api server. (Run this first)

<a id="opIdlogin"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v2/login', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/login");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`POST /api/v2/login`

Login into api server. (Run this first)

> Body parameter

```json
{
  "user": "string",
  "password": "string"
}
```

<h3 id="login-into-api-server.-(run-this-first)-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[LoginInput](#schemalogininput)|true|none|

> Example responses

> 200 Response

```json
{
  "authenticated": true,
  "company": "CloudFabrix",
  "first_name": "Acme",
  "firstname": "Acme",
  "id": "acme@cfx.com",
  "is_authenticated": true,
  "is_workspaceadmin": false,
  "is_workspacecreator": 0,
  "last_name": "Inc",
  "lastname": "Inc",
  "login-time": "2023-06-28T15:35:30.500255",
  "rdac_auth_token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiI4MGQ1MGI0ZS1lMWYyLTQ3ZGUtOGZmMC1hMzhjMTgwY2VmYmIifQ.4lE3Uzlh7PJwyuCJ8DdJ2xq6szMzF-B4PSTjomrOl8k",
  "remote_user": false,
  "reset_password": 0,
  "role": "TENANT_USERS",
  "session-id": "39030163f5eb4e30a713be9c9c4bab7f",
  "status": "ok",
  "tenantid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb",
  "user": "acme@cfx.com",
  "workspace": "ws80d50b",
  "workspaceid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb"
}
```

<h3 id="login-into-api-server.-(run-this-first)-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[UserDetails](#schemauserdetails)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-users">Users</h1>

## Get current logged in user details

<a id="opIdget_current_user"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/current_user', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/current_user");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/current_user`

Get the details of the current user

> Example responses

> 200 Response

```json
{
  "authenticated": true,
  "company": "CloudFabrix",
  "first_name": "Acme",
  "firstname": "Acme",
  "id": "acme@cfx.com",
  "is_authenticated": true,
  "is_workspaceadmin": false,
  "is_workspacecreator": 0,
  "last_name": "Inc",
  "lastname": "Inc",
  "login-time": "2023-06-28T15:35:30.500255",
  "rdac_auth_token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiI4MGQ1MGI0ZS1lMWYyLTQ3ZGUtOGZmMC1hMzhjMTgwY2VmYmIifQ.4lE3Uzlh7PJwyuCJ8DdJ2xq6szMzF-B4PSTjomrOl8k",
  "remote_user": false,
  "reset_password": 0,
  "role": "TENANT_USERS",
  "session-id": "39030163f5eb4e30a713be9c9c4bab7f",
  "status": "ok",
  "tenantid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb",
  "user": "acme@cfx.com",
  "workspace": "ws80d50b",
  "workspaceid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb"
}
```

<h3 id="get-current-logged-in-user-details-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[UserDetails](#schemauserdetails)|

<aside class="success">
This operation does not require authentication
</aside>

## Get all users

<a id="opIdget_tenant_users"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/users', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/users");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/users`

Get all the users belonging to the same tenant as the current user

> Example responses

> 200 Response

```json
{
  "is_first": true,
  "is_last": true,
  "num_items": 12,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "userId",
        "identifier": "userId",
        "key": true,
        "sortable": true,
        "title": "User ID",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Tenant Users"
  },
  "total_count": 112,
  "users": [
    {
      "contactNumber": "",
      "emailId": "acme@cfx.com",
      "firstName": "acme",
      "id": "user-dashboard-user-permissions",
      "lastName": "user",
      "localuser": "Yes",
      "loggedIn_user": true,
      "parentResourceId": "0d76cbf4-6234-483d-b11d-c00c209fa668",
      "profile": "msp-admin",
      "role": "msp-admin",
      "status": "Active",
      "userGroup": "msp-admin-group",
      "userId": "acme@cfx.com",
      "userType": "local"
    }
  ]
}
```

<h3 id="get-all-users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Users](#schemausers)|

<aside class="success">
This operation does not require authentication
</aside>

## Add user

<a id="opIdadd_tenant_user"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v2/users', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/users");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`POST /api/v2/users`

Add a user

> Body parameter

```json
{
  "remoteUser": false,
  "authenticationType": "ad",
  "group": "string",
  "firstname": "string",
  "lastname": "string",
  "id": "user@example.com"
}
```

<h3 id="add-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[UserAddModel](#schemauseraddmodel)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add-user-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Change User Activation Status

<a id="opIdchange_user_status"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('/api/v2/users/user/{id}/status', params={
  'activate': 'true'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/users/user/{id}/status?activate=true");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`PUT /api/v2/users/user/{id}/status`

Activate/Deactivate User. Deactivating currently logged in user is not allowed.

<h3 id="change-user-activation-status-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|ID of the user to be activated/deactivated|
|activate|query|boolean|true|Desired user status: Activate (True) or Deactivate(False)|

> Example responses

> 200 Response

```json
null
```

<h3 id="change-user-activation-status-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="change-user-activation-status-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Change User group

<a id="opIdchange_user_group"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.put('/api/v2/users/user/{id}/group', params={
  'group': 'string'
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/users/user/{id}/group?group=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`PUT /api/v2/users/user/{id}/group`

Change user group. Changing currently logged in user is not allowed.

<h3 id="change-user-group-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|ID of the user to be activated/deactivated|
|group|query|string|true|New group for the user.|

> Example responses

> 200 Response

```json
null
```

<h3 id="change-user-group-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="change-user-group-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-dashboards">Dashboards</h1>

## Fetch meta data for dashboards

<a id="opIdget_dashboards"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/dashboards', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/dashboards");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/dashboards`

Fetch meta data for dashboards

<h3 id="fetch-meta-data-for-dashboards-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'description', 'usecase', 'category', 'version']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-for-dashboards-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-datasets">Datasets</h1>

## Fetch meta data about datasets

<a id="opIdget_datasets"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/datasets', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/datasets`

Fetch meta data about datasets

<h3 id="fetch-meta-data-about-datasets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'schema']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-about-datasets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Add a dataset

<a id="opIdadd_dataset"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v2/datasets', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`POST /api/v2/datasets`

Add a dataset.

> Body parameter

```json
{
  "name": "string",
  "folder": "Default",
  "schema_name": "string",
  "tag": "string"
}
```

<h3 id="add-a-dataset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DatasetAddModel](#schemadatasetaddmodel)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add-a-dataset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add-a-dataset-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete a dataset

<a id="opIddelete_dataset"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/api/v2/datasets/dataset/{name}', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets/dataset/{name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`DELETE /api/v2/datasets/dataset/{name}`

Delete a dataset. Please note that all the data of the dataset will be deleted and can not be undone.

<h3 id="delete-a-dataset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Dataset name to be deleted.|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-a-dataset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-a-dataset-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Get data of a dataset

<a id="opIdget_dataset_data"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/datasets/dataset/{name}/data', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets/dataset/{name}/data");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/datasets/dataset/{name}/data`

Get data of a dataset

<h3 id="get-data-of-a-dataset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the dataset|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'comment']|
|sort|query|any|false|Sort the output based on given fields. Prepend '-' to sort descending|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="get-data-of-a-dataset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Update rows of a dataset

<a id="opIdupdate_dataset_data"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/v2/datasets/dataset/{name}/data', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets/dataset/{name}/data");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`PUT /api/v2/datasets/dataset/{name}/data`

Update (merge or replace) existing dataset data.
    This function currently does not support deleting rows.<br/>
    If replace is true, entire existing dataset data is replaced with the new data in input.<br/>
    If replace is false, <br/>
    <ul>
        <li>If keys are not given, the input data is appened to the existing dataset.
        <li>If keys are given then the following flow explains the operation<br/>
            For each row in the input data:
            <ul>
                <li>The rows with same values for all the keys are replaced with input row.
                <li>Other rows are appended to the existing dataset
            </ul>
        Error raised when:
            <ul>
                <li>If there are duplicate rows in input data with same key values
                <li>If any key passed in keys is not present as a column in the input data
            </ul>
    </ul>
    NOTE: This directly updates the dataset and all drafts are removed.

> Body parameter

```json
[
  {}
]
```

<h3 id="update-rows-of-a-dataset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the dataset|
|replace|query|any|false|If set to true, replace the existing data with new data|
|keys|query|any|false|Array of keys to match for updating rows|
|body|body|array[object]|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="update-rows-of-a-dataset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="update-rows-of-a-dataset-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete matching dataset rows

<a id="opIddelete_dataset_rows"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.delete('/api/v2/datasets/dataset/{name}/data', params={
  'keys': [
  "string"
]
}, headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets/dataset/{name}/data?keys=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`DELETE /api/v2/datasets/dataset/{name}/data`

Delete dataset rows matching the input data
    All the rows in existing dataset that match all the keys in input data are deleted.
    NOTE: This directly updates the dataset and all drafts are removed.

> Body parameter

```json
[
  {}
]
```

<h3 id="delete-matching-dataset-rows-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the dataset|
|keys|query|any|true|Array of keys to match for updating rows|
|body|body|array[object]|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-matching-dataset-rows-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-matching-dataset-rows-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete enitre data of a dataset

<a id="opIddelete_dataset_all_data"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/api/v2/datasets/dataset/{name}/data/all', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/datasets/dataset/{name}/data/all");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`DELETE /api/v2/datasets/dataset/{name}/data/all`

Delete entire data of a dataset

<h3 id="delete-enitre-data-of-a-dataset-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the dataset|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-enitre-data-of-a-dataset-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-enitre-data-of-a-dataset-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-persistent-streams">Persistent Streams</h1>

## Fetch meta data about pstreams

<a id="opIdget_pstreams"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/pstreams', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pstreams");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/pstreams`

Fetch meta data about pstreams

<h3 id="fetch-meta-data-about-pstreams-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-about-pstreams-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Add a pstream

<a id="opIdadd_pstream"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/api/v2/pstreams', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pstreams");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`POST /api/v2/pstreams`

Add a new pstream to the system

> Body parameter

```json
{
  "attributes": {
    "retention_days": 31,
    "unique_keys": [
      "key1",
      "key2"
    ]
  },
  "name": "example_pstream"
}
```

<h3 id="add-a-pstream-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[PstreamAddModel](#schemapstreamaddmodel)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="add-a-pstream-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="add-a-pstream-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Edit attributes of a pstream

<a id="opIdedit_pstream"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.put('/api/v2/pstreams/pstream/{name}', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pstreams/pstream/{name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`PUT /api/v2/pstreams/pstream/{name}`

Edit the attributes of a persistent stream

> Body parameter

```json
{
  "attributes": {
    "retention_days": 31,
    "unique_keys": [
      "key1",
      "key2"
    ]
  }
}
```

<h3 id="edit-attributes-of-a-pstream-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the pstream to be edited|
|body|body|[PstreamEditModel](#schemapstreameditmodel)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="edit-attributes-of-a-pstream-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="edit-attributes-of-a-pstream-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete a pstream.

<a id="opIddelete_pstream"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.delete('/api/v2/pstreams/pstream/{name}', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pstreams/pstream/{name}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`DELETE /api/v2/pstreams/pstream/{name}`

Delete a persistent stream.

<h3 id="delete-a-pstream.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the pstream to be deleted|
|delete_data|query|boolean|false|Delete data as well. If data is not deleted, adding the same pstream again will add the old data back.|

> Example responses

> 200 Response

```json
null
```

<h3 id="delete-a-pstream.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="delete-a-pstream.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Get data of a pstream

<a id="opIdget_pstream_data"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/pstreams/pstream/{name}/data', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pstreams/pstream/{name}/data");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/pstreams/pstream/{name}/data`

Get data of a persistent stream

<h3 id="get-data-of-a-pstream-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|name|path|string|true|Name of the pstream|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'comment']|
|sort|query|any|false|Sort the output based on given fields. Prepend '-' to sort descending|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="get-data-of-a-pstream-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-pipelines">Pipelines</h1>

## Fetch meta data about pipelines

<a id="opIdget_pipelines"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/pipelines', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pipelines");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/pipelines`

Fetch meta data about pipelines

<h3 id="fetch-meta-data-about-pipelines-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'description']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-about-pipelines-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

## Fetch meta data about draft pipelines

<a id="opIdget_draft_pipelines"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/pipelines/draft', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/pipelines/draft");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/pipelines/draft`

Fetch meta data about draft pipelines

<h3 id="fetch-meta-data-about-draft-pipelines-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'description']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-about-draft-pipelines-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="cloudfabrix-rda-platform-api-blueprints">Blueprints</h1>

## Fetch meta data about blueprints

<a id="opIdget_blueprints"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/api/v2/Blueprints', headers = headers)

print(r.json())

```

```java
URL obj = new URL("/api/v2/Blueprints");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

`GET /api/v2/Blueprints`

Fetch meta data about blueprints

<h3 id="fetch-meta-data-about-blueprints-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|cfxql_query|query|any|false|<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results|
|search|query|any|false|search across fields: ['name', 'comment']|
|offset|query|any|false|Offset to start the results from.|
|limit|query|any|false|Maximum number of results to return|
|sort|query|any|false|Sort the output based on given fields|

> Example responses

> 200 Response

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}
```

<h3 id="fetch-meta-data-about-blueprints-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[TableReportResponse](#schematablereportresponse)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AuthType">AuthType</h2>
<!-- backwards compatibility -->
<a id="schemaauthtype"></a>
<a id="schema_AuthType"></a>
<a id="tocSauthtype"></a>
<a id="tocsauthtype"></a>

```json
"ad"

```

AuthType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|AuthType|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|AuthType|ad|
|AuthType|sso|

<h2 id="tocS_DatasetAddModel">DatasetAddModel</h2>
<!-- backwards compatibility -->
<a id="schemadatasetaddmodel"></a>
<a id="schema_DatasetAddModel"></a>
<a id="tocSdatasetaddmodel"></a>
<a id="tocsdatasetaddmodel"></a>

```json
{
  "name": "string",
  "folder": "Default",
  "schema_name": "string",
  "tag": "string"
}

```

DatasetAddModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|folder|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|schema_name|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tag|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_LoginInput">LoginInput</h2>
<!-- backwards compatibility -->
<a id="schemalogininput"></a>
<a id="schema_LoginInput"></a>
<a id="tocSlogininput"></a>
<a id="tocslogininput"></a>

```json
{
  "user": "string",
  "password": "string"
}

```

LoginInput

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|user|string|true|none|none|
|password|string|true|none|none|

<h2 id="tocS_PstreamAddModel">PstreamAddModel</h2>
<!-- backwards compatibility -->
<a id="schemapstreamaddmodel"></a>
<a id="schema_PstreamAddModel"></a>
<a id="tocSpstreamaddmodel"></a>
<a id="tocspstreamaddmodel"></a>

```json
{
  "attributes": {
    "retention_days": 31,
    "unique_keys": [
      "key1",
      "key2"
    ]
  },
  "name": "example_pstream"
}

```

PstreamAddModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|attributes|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_PstreamEditModel">PstreamEditModel</h2>
<!-- backwards compatibility -->
<a id="schemapstreameditmodel"></a>
<a id="schema_PstreamEditModel"></a>
<a id="tocSpstreameditmodel"></a>
<a id="tocspstreameditmodel"></a>

```json
{
  "attributes": {
    "retention_days": 31,
    "unique_keys": [
      "key1",
      "key2"
    ]
  }
}

```

PstreamEditModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attributes|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_TableReportResponse">TableReportResponse</h2>
<!-- backwards compatibility -->
<a id="schematablereportresponse"></a>
<a id="schema_TableReportResponse"></a>
<a id="tocStablereportresponse"></a>
<a id="tocstablereportresponse"></a>

```json
{
  "is_first": false,
  "is_last": false,
  "last_sort_results": [
    "Authentication Servers",
    "9d74183bf12af49841f054467d25b1b6"
  ],
  "limit": 100,
  "num_items": 12,
  "offset": 100,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "name",
        "identifier": "name",
        "key": false,
        "sortable": true,
        "title": "name",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Dashboards"
  },
  "sort": [
    "-name"
  ],
  "total_count": 112
}

```

TableReportResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|last_sort_results|any|false|none|Last sort tags used for internal puposes|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reportMetaData|any|false|none|Meta information about the report, including columns and types etc|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offset|any|false|none|Starting offset in the filtered results|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|limit|any|false|none|Maximum number of results to be returned per page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sort|any|false|none|Sort order passed as part of request|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total_count|any|false|none|Total number of results that matched the query|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|num_items|any|false|none|Number of results returned in this page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_first|any|false|none|True if this page is first page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_last|any|false|none|True if this page is last page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_User">User</h2>
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "contactNumber": "string",
  "emailId": "string",
  "firstName": "string",
  "id": "string",
  "lastName": "string",
  "localuser": true,
  "loggedIn_user": true,
  "parentResourceId": "string",
  "profile": "string",
  "status": "string",
  "userGroup": "string",
  "userId": "string",
  "userType": "string",
  "validationStatus": "string",
  "role": "string"
}

```

User

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|contactNumber|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emailId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|firstName|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lastName|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|localuser|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loggedIn_user|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|parentResourceId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|profile|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userGroup|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userId|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|userType|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|validationStatus|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|role|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_UserAddModel">UserAddModel</h2>
<!-- backwards compatibility -->
<a id="schemauseraddmodel"></a>
<a id="schema_UserAddModel"></a>
<a id="tocSuseraddmodel"></a>
<a id="tocsuseraddmodel"></a>

```json
{
  "remoteUser": false,
  "authenticationType": "ad",
  "group": "string",
  "firstname": "string",
  "lastname": "string",
  "id": "user@example.com"
}

```

UserAddModel

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|remoteUser|boolean|false|none|none|
|authenticationType|any|false|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[AuthType](#schemaauthtype)|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|group|string|true|none|none|
|firstname|string|true|none|none|
|lastname|string|true|none|none|
|id|string(email)|true|none|none|

<h2 id="tocS_UserDetails">UserDetails</h2>
<!-- backwards compatibility -->
<a id="schemauserdetails"></a>
<a id="schema_UserDetails"></a>
<a id="tocSuserdetails"></a>
<a id="tocsuserdetails"></a>

```json
{
  "authenticated": true,
  "company": "CloudFabrix",
  "first_name": "Acme",
  "firstname": "Acme",
  "id": "acme@cfx.com",
  "is_authenticated": true,
  "is_workspaceadmin": false,
  "is_workspacecreator": 0,
  "last_name": "Inc",
  "lastname": "Inc",
  "login-time": "2023-06-28T15:35:30.500255",
  "rdac_auth_token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyLWlkIjoiYWNtZUBjZnguY29tIiwid29ya3NwYWNlaWQiOiI4MGQ1MGI0ZS1lMWYyLTQ3ZGUtOGZmMC1hMzhjMTgwY2VmYmIifQ.4lE3Uzlh7PJwyuCJ8DdJ2xq6szMzF-B4PSTjomrOl8k",
  "remote_user": false,
  "reset_password": 0,
  "role": "TENANT_USERS",
  "session-id": "39030163f5eb4e30a713be9c9c4bab7f",
  "status": "ok",
  "tenantid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb",
  "user": "acme@cfx.com",
  "workspace": "ws80d50b",
  "workspaceid": "80d50b4e-e1f2-47de-8ff0-a38c180cefbb"
}

```

UserDetails

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|authenticated|boolean|false|none|Whether user is authenticated|
|company|any|false|none|Company the user belongs to|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|first_name|any|false|none|First name|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|Id of the user (email address)|
|is_authenticated|boolean|false|none|Alias to 'authenticated'|
|is_workspaceadmin|boolean|false|none|Is the user a workspace admin|
|is_workspacecreator|boolean|false|none|Is the user a workspace creator|
|last_name|boolean|false|none|Last Name|
|lastname|boolean|false|none|Alias to last_name|
|login_time|string|false|none|Login time in ISO format|
|rdac_auth_token|string|false|none|Authentication Token|
|remote_user|boolean|false|none|Whether user is a remote user or a local user|
|role|string|false|none|User Role|
|session_id|string|false|none|Current session id|
|status|string|false|none|Current status of the user|
|tenantid|string|false|none|Tenant ID of the user|
|user|string|false|none|alias to 'id'|
|workspace|string|false|none|Name of the workspace|
|workspaceid|string|false|none|ID of the workspace|

<h2 id="tocS_Users">Users</h2>
<!-- backwards compatibility -->
<a id="schemausers"></a>
<a id="schema_Users"></a>
<a id="tocSusers"></a>
<a id="tocsusers"></a>

```json
{
  "is_first": true,
  "is_last": true,
  "num_items": 12,
  "properties": {},
  "reportMetaData": {
    "reportColumnDefinitionList": [
      {
        "hidden": false,
        "id": "userId",
        "identifier": "userId",
        "key": true,
        "sortable": true,
        "title": "User ID",
        "type": "TEXT",
        "visible": true
      }
    ],
    "title": "Tenant Users"
  },
  "total_count": 112,
  "users": [
    {
      "contactNumber": "",
      "emailId": "acme@cfx.com",
      "firstName": "acme",
      "id": "user-dashboard-user-permissions",
      "lastName": "user",
      "localuser": "Yes",
      "loggedIn_user": true,
      "parentResourceId": "0d76cbf4-6234-483d-b11d-c00c209fa668",
      "profile": "msp-admin",
      "role": "msp-admin",
      "status": "Active",
      "userGroup": "msp-admin-group",
      "userId": "acme@cfx.com",
      "userType": "local"
    }
  ]
}

```

Users

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|last_sort_results|any|false|none|Last sort tags used for internal puposes|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reportMetaData|any|false|none|Meta information about the report, including columns and types etc|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|object|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offset|any|false|none|Starting offset in the filtered results|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|limit|any|false|none|Maximum number of results to be returned per page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sort|any|false|none|Sort order passed as part of request|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[string]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|total_count|any|false|none|Total number of results that matched the query|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|num_items|any|false|none|Number of results returned in this page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_first|any|false|none|True if this page is first page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|is_last|any|false|none|True if this page is last page|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|boolean|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|users|any|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|[[User](#schemauser)]|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|null|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_blueprints_enum">blueprints_enum</h2>
<!-- backwards compatibility -->
<a id="schemablueprints_enum"></a>
<a id="schema_blueprints_enum"></a>
<a id="tocSblueprints_enum"></a>
<a id="tocsblueprints_enum"></a>

```json
"auto_deploy"

```

blueprints_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|blueprints_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|blueprints_enum|auto_deploy|
|blueprints_enum|-auto_deploy|
|blueprints_enum|category|
|blueprints_enum|-category|
|blueprints_enum|comment|
|blueprints_enum|-comment|
|blueprints_enum|enabled|
|blueprints_enum|-enabled|
|blueprints_enum|errors|
|blueprints_enum|-errors|
|blueprints_enum|id|
|blueprints_enum|-id|
|blueprints_enum|name|
|blueprints_enum|-name|
|blueprints_enum|saved_type|
|blueprints_enum|-saved_type|
|blueprints_enum|state|
|blueprints_enum|-state|
|blueprints_enum|timestamp|
|blueprints_enum|-timestamp|
|blueprints_enum|type|
|blueprints_enum|-type|
|blueprints_enum|version|
|blueprints_enum|-version|

<h2 id="tocS_dashboards_enum">dashboards_enum</h2>
<!-- backwards compatibility -->
<a id="schemadashboards_enum"></a>
<a id="schema_dashboards_enum"></a>
<a id="tocSdashboards_enum"></a>
<a id="tocsdashboards_enum"></a>

```json
"category"

```

dashboards_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|dashboards_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|dashboards_enum|category|
|dashboards_enum|-category|
|dashboards_enum|description|
|dashboards_enum|-description|
|dashboards_enum|folder|
|dashboards_enum|-folder|
|dashboards_enum|name|
|dashboards_enum|-name|
|dashboards_enum|saved_time|
|dashboards_enum|-saved_time|
|dashboards_enum|timestamp|
|dashboards_enum|-timestamp|
|dashboards_enum|usecase|
|dashboards_enum|-usecase|
|dashboards_enum|version|
|dashboards_enum|-version|
|dashboards_enum|versions_count|
|dashboards_enum|-versions_count|

<h2 id="tocS_datasets_enum">datasets_enum</h2>
<!-- backwards compatibility -->
<a id="schemadatasets_enum"></a>
<a id="schema_datasets_enum"></a>
<a id="tocSdatasets_enum"></a>
<a id="tocsdatasets_enum"></a>

```json
"folder"

```

datasets_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|datasets_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|datasets_enum|folder|
|datasets_enum|-folder|
|datasets_enum|format|
|datasets_enum|-format|
|datasets_enum|mem_size_mb|
|datasets_enum|-mem_size_mb|
|datasets_enum|name|
|datasets_enum|-name|
|datasets_enum|num_columns|
|datasets_enum|-num_columns|
|datasets_enum|num_rows|
|datasets_enum|-num_rows|
|datasets_enum|saved_time|
|datasets_enum|-saved_time|
|datasets_enum|schema|
|datasets_enum|-schema|
|datasets_enum|timestamp|
|datasets_enum|-timestamp|

<h2 id="tocS_draft_pipelines_enum">draft_pipelines_enum</h2>
<!-- backwards compatibility -->
<a id="schemadraft_pipelines_enum"></a>
<a id="schema_draft_pipelines_enum"></a>
<a id="tocSdraft_pipelines_enum"></a>
<a id="tocsdraft_pipelines_enum"></a>

```json
"category"

```

draft_pipelines_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|draft_pipelines_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|draft_pipelines_enum|category|
|draft_pipelines_enum|-category|
|draft_pipelines_enum|description|
|draft_pipelines_enum|-description|
|draft_pipelines_enum|folder|
|draft_pipelines_enum|-folder|
|draft_pipelines_enum|name|
|draft_pipelines_enum|-name|
|draft_pipelines_enum|saved_time|
|draft_pipelines_enum|-saved_time|
|draft_pipelines_enum|timestamp|
|draft_pipelines_enum|-timestamp|
|draft_pipelines_enum|usercase|
|draft_pipelines_enum|-usercase|
|draft_pipelines_enum|version|
|draft_pipelines_enum|-version|
|draft_pipelines_enum|version_count|
|draft_pipelines_enum|-version_count|

<h2 id="tocS_pipelines_enum">pipelines_enum</h2>
<!-- backwards compatibility -->
<a id="schemapipelines_enum"></a>
<a id="schema_pipelines_enum"></a>
<a id="tocSpipelines_enum"></a>
<a id="tocspipelines_enum"></a>

```json
"category"

```

pipelines_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pipelines_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|pipelines_enum|category|
|pipelines_enum|-category|
|pipelines_enum|description|
|pipelines_enum|-description|
|pipelines_enum|folder|
|pipelines_enum|-folder|
|pipelines_enum|name|
|pipelines_enum|-name|
|pipelines_enum|saved_time|
|pipelines_enum|-saved_time|
|pipelines_enum|timestamp|
|pipelines_enum|-timestamp|
|pipelines_enum|usercase|
|pipelines_enum|-usercase|
|pipelines_enum|version|
|pipelines_enum|-version|
|pipelines_enum|version_count|
|pipelines_enum|-version_count|

<h2 id="tocS_pstreams_enum">pstreams_enum</h2>
<!-- backwards compatibility -->
<a id="schemapstreams_enum"></a>
<a id="schema_pstreams_enum"></a>
<a id="tocSpstreams_enum"></a>
<a id="tocspstreams_enum"></a>

```json
"collection_status"

```

pstreams_enum

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pstreams_enum|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|pstreams_enum|collection_status|
|pstreams_enum|-collection_status|
|pstreams_enum|database|
|pstreams_enum|-database|
|pstreams_enum|datastore_type|
|pstreams_enum|-datastore_type|
|pstreams_enum|index_name|
|pstreams_enum|-index_name|
|pstreams_enum|name|
|pstreams_enum|-name|
|pstreams_enum|retention_days|
|pstreams_enum|-retention_days|
|pstreams_enum|saved_time|
|pstreams_enum|-saved_time|
|pstreams_enum|system_defined|
|pstreams_enum|-system_defined|
|pstreams_enum|timestamp|
|pstreams_enum|-timestamp|

