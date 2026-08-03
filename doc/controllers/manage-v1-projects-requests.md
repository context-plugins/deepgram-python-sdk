# Manage V1 Projects Requests

```python
manage_v_1_projects_requests_api = client.manage_v_1_projects_requests
```

## Class Name

`ManageV1ProjectsRequestsApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-requests.md#list)
* [Get](../../doc/controllers/manage-v1-projects-requests.md#get)


# List

Generates a list of requests for a specific project

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        project_id,
        authorization,
        start=None,
        end=None,
        limit=10,
        page=None,
        accessor=None,
        request_id=None,
        deployment=None,
        endpoint=None,
        method=None,
        status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `start` | `datetime` | Query, Optional | Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM |
| `end` | `datetime` | Query, Optional | End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM |
| `limit` | `float` | Query, Optional | Number of results to return per page. Default 10. Range [1,1000]<br><br>**Default**: `10` |
| `page` | `float` | Query, Optional | Navigate and return the results to retrieve specific portions of information of the response |
| `accessor` | `str` | Query, Optional | Filter for requests where a specific accessor was used |
| `request_id` | `str` | Query, Optional | Filter for a specific request id |
| `deployment` | [`V1ProjectsProjectIdRequestsGetParametersDeployment`](../../doc/models/v1-projects-project-id-requests-get-parameters-deployment.md) | Query, Optional | Filter for requests where a specific deployment was used |
| `endpoint` | [`V1ProjectsProjectIdRequestsGetParametersEndpoint`](../../doc/models/v1-projects-project-id-requests-get-parameters-endpoint.md) | Query, Optional | Filter for requests where a specific endpoint was used |
| `method` | [`V1ProjectsProjectIdRequestsGetParametersMethod`](../../doc/models/v1-projects-project-id-requests-get-parameters-method.md) | Query, Optional | Filter for requests where a specific method was used |
| `status` | [`V1ProjectsProjectIdRequestsGetParametersStatus`](../../doc/models/v1-projects-project-id-requests-get-parameters-status.md) | Query, Optional | Filter for requests that succeeded (status code < 300) or failed (status code >=400) |

## Response Type

**200**: A list of requests for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectRequestsV1Response`](../../doc/models/list-project-requests-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

limit = 10

result = manage_v_1_projects_requests_api.list(
    project_id,
    authorization,
    limit=limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Get

Retrieves a specific request for a specific project

:information_source: **Note** This endpoint does not require authentication.

```python
def get(self,
       project_id,
       request_id,
       authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `request_id` | `str` | Template, Required | The unique identifier of the request |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A specific request for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectRequestV1Response`](../../doc/models/get-project-request-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

request_id = 'request_id8'

authorization = 'Authorization8'

result = manage_v_1_projects_requests_api.get(
    project_id,
    request_id,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

