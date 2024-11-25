# Persistent Streams

> [!NOTE]
> Access to the APIs listed below requires appropriate user role permissions. Please ensure you are logged in with the correct credentials to proceed.


## Add Data to a Persistent Stream

### Endpoint:
POST `/api/v2/pstreams/pstream/{name}/data`

### Description:
Add new data to an existing persistent stream (pstream), merging it with any previously existing data.

### Parameters:

#### Path Parameters:
| Parameter   | Type   | Description                   |
|-------------|--------|-------------------------------|
| `name`      | string | Name of the persistent stream.|

#### Request Body:
| Parameter    | Type        | Description                                       |
|--------------|-------------|---------------------------------------------------|
| `data`       | List[Dict]  | Array of data to append to the specified pstream. |

### Example Request Body:
```json
[
  {
    "key1": "value",
    "key2": "value"
  },
  {
    "key1": "value",
    "key2": "value"
  }
]
```

### Example Request
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pstreams/pstream/example_pstream/data' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0Ny4|Z0Nlr' \
--data '[
  {
    "name":"Jack Ryan", 
    "city": "Washington, DC", 
    "zip-code": 20006,
    "is_pet_owner": true,
    "gym_membership_uuid": "6c34f649-861e-4259-ac69-21b9dce86ca5",
    "last_gym_visit": "2024-11-20",
    "timestamp": "18:15:54.065585+00:00"
    }
]'
```
### Output:
![add_data_pstream_output](https://github.com/user-attachments/assets/6e288e90-357f-445c-969d-5fde02547dcc)



## Update Data in a Persistent Stream

### Endpoint:
PUT `/api/v2/pstreams/pstream/{name}/data`

### Description:
Update specific data within an existing persistent stream (pstream) based on a query.

### Parameters:

#### Path Parameters:
| Parameter | Type   | Description                  |
|-----------|--------|------------------------------|
| `name`    | string | Name of the persistent stream.|

#### Query Parameters:
| Parameter     | Type   | Description                                                                 |
|---------------|--------|-----------------------------------------------------------------------------|
| `cfxql_query` | string | CFXQL query to locate entries in the pstream and update them with the data. |
| `conflicts`   | string | Action to take when the update-by-query hits version conflicts. Defaults to `abort`. |

#### Request Body:
| Parameter | Type | Description                             |
|-----------|------|-----------------------------------------|
| `data`    | Dict | Data to be updated in the persistent stream.|

#### Example Request Body:
```json
{
  "key1": "updated_value",
  "key2": "updated_value"
}
```

### Example Request
```shell cURL
curl --location --request PUT 'https://10.95.125.95/api/v2/pstreams/pstream/example_pstream/data?cfxql_query=name%3D%27Jack%20Ryan%27&conflicts=abort' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0N09|Z0Nlr' \
--data '{"is_pet_owner": false}'
```
### Output:
![update_pstream_data_output](https://github.com/user-attachments/assets/d80b1853-1b89-437a-bc6f-c1c916e5c5a9)



## Delete Data from a Persistent Stream

### Endpoint:
DELETE `/api/v2/pstreams/pstream/{name}/data`

### Description:
Delete specific data from an existing persistent stream (pstream) based on a query.

### Parameters:

#### Path Parameters:
| Parameter | Type   | Description                  |
|-----------|--------|------------------------------|
| `name`    | string | Name of the persistent stream.|

#### Query Parameters:
| Parameter        | Type   | Description                                                                  |
|------------------|--------|------------------------------------------------------------------------------|
| `cfxql_query`    | string | CFXQL query to locate entries in the pstream and delete them.                |
| `conflicts`      | string | Action to take when the delete-by-query hits version conflicts. Defaults to `abort`. |
| `case_sensitive` | bool   | Enable or disable case-sensitive search. Defaults to `True`.                  |

### Example Request:
```shell cURL
curl --location --request DELETE 'https://10.95.125.95/api/v2/pstreams/pstream/example_pstream/data?cfxql_query=name%3D%27Jack%20Ryan%27&conflicts=abort&case_sensitive=true' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0N3Z|Z0Nlr'
```

### Output:
![delete_pstream_data_output](https://github.com/user-attachments/assets/f8c27aa0-9a2d-41a3-a62e-e061dcf16144)



## Get Metadata of a Persistent Stream

### Endpoint:
GET `/api/v2/pstreams/pstream/{name}/metadata`

### Description:
Retrieve metadata for a specific persistent stream.

### Parameters:

| Parameter   | Type    | Description                                 |
|-------------|---------|---------------------------------------------|
| `name`      | string  | Name of the persistent stream.              |
| `offset`    | integer | Offset to start the results from (default: 0). |
| `limit`     | integer | Maximum number of results to return (default: 100). |

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pstreams/pstream/example_pstream/metadata?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0Nlr|Z0Nlr'
```

### Output:
![get_metadata_of_a_pstream_output](https://github.com/user-attachments/assets/ff860832-b43e-40f1-83bb-396fd45b4b59)


## Get Stats of a Persistent Stream

### Endpoint:
GET `/api/v2/pstreams/pstream/{name}/stats`

### Description:
Retrieve stats for a specific persistent stream.

### Parameters:

| Parameter   | Type    | Description                                 |
|-------------|---------|---------------------------------------------|
| `name`      | string  | Name of the persistent stream.              |
| `offset`    | integer | Offset to start the results from (default: 0). |
| `limit`     | integer | Maximum number of results to return (default: 100). |

### Example Request:
```shell cURL
curl --location 'https://10.95.125.95/api/v2/pstreams/pstream/example_pstream/stats?offset=0&limit=100' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: __cfxsession=025611a1-c0b6-4c45-a4c7-63e8b377d982; cfx_saas_session=8a6d39e9245a408984962fdd883a958b; rdafportal=rdaf-portal-1|Z0Nsn|Z0Nlr'
```

### Output:
![get_stats_of_a_pstream_output](https://github.com/user-attachments/assets/08ef80b4-7a4a-48e4-a0d6-898a7f8322c1)
