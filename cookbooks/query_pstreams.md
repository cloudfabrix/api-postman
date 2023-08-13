# Query data from pstream
A simple query for getting data from pstream. This example gets the data with maximum 100 rows (By default descending order of timestamp)
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_datasets_meta/data' \
--header 'Cookie: __cfxsession=8d624dd5-4991-43b7-9eed-0130f2f8c3b6; cfx_saas_session=f4acbc07472a4eaebb5cfc09da532a75; rdafportal=rdaf-portal-1|ZNk5b|ZNkw/'
```
## Output
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/fa00a216-1ade-44ab-98a9-79c623523c28)

# Query data with query and sort
Get data from `rda_datasets_meta` and return only the items where `name` column contains test. Sort the results by `name` columns in descending order
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_datasets_meta/data?cfxql_query=name%20contains%20%27test%27&sort=-name' \
--header 'Cookie: __cfxsession=129d7532-a19e-43d3-b8cd-5951e7f3941f; cfx_saas_session=469c9c897cb94b54b7173f91da139afd; rdafportal=rdaf-portal-1|ZNkxD|ZNkw/'
```
## output
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/087de723-651d-4a6a-a8a8-1e358a05234d)

# Query data with multi sort
Get data from `rda_datasets_meta`. Sort the results by `folder` column. For the results that have the same folder, return the most recent first.
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_datasets_meta/data?sort=folder&sort=-timestamp' \
--header 'Cookie: __cfxsession=8d624dd5-4991-43b7-9eed-0130f2f8c3b6; cfx_saas_session=f4acbc07472a4eaebb5cfc09da532a75; rdafportal=rdaf-portal-1|ZNk8p|ZNkw/'
```
## output
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/f1e86814-b08a-46bb-9039-610e583e55d2)

# Query data with groupby and count
Get data from `rda_dashboards_meta`. Return number of dashboard grouped by type of dashboard
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_dashboards_meta/data?group_by=dashboard_type&agg_function=value_count&agg_column=count_' \
--header 'Cookie: __cfxsession=129d7532-a19e-43d3-b8cd-5951e7f3941f; cfx_saas_session=469c9c897cb94b54b7173f91da139afd; rdafportal=rdaf-portal-1|ZNkxl|ZNkw/'
```
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/7d3ed833-1a0e-40f8-a944-6c367b74bb1f)

# Group by and avg
Query `rda_microservice_traces` data and return average `duration` of a given and source and destination combination
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_microservice_traces/data?group_by=source&group_by=destination&agg_function=avg&agg_column=duration' \
--header 'Cookie: __cfxsession=129d7532-a19e-43d3-b8cd-5951e7f3941f; cfx_saas_session=469c9c897cb94b54b7173f91da139afd; rdafportal=rdaf-portal-1|ZNkzA|ZNkw/'
```
## Output
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/e6cdc7cd-c0b3-486e-8bd7-0ac05273cafb)

# Group by and count
Query `rda_microservice_traces` data and return number of entries where 'collector' is either source or destination
```shell Curl
curl -k --location 'https://10.95.125.190/api/v2/pstreams/pstream/rda_microservice_traces/data?group_by=source&group_by=destination&agg_function=value_count&agg_column=count_&cfxql_query=source%20is%20%27collector%27%20or%20destination%20is%20%27collector%27' \
--header 'Cookie: __cfxsession=8d624dd5-4991-43b7-9eed-0130f2f8c3b6; cfx_saas_session=f4acbc07472a4eaebb5cfc09da532a75; rdafportal=rdaf-portal-1|ZNk2b|ZNkw/'
```
## Output
![image](https://github.com/cloudfabrix/api-postman/assets/120137725/593809b0-79c6-4b79-a3e4-f2c6a67f9ef1)


```


