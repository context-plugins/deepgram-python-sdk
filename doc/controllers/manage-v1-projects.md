# Manage V1 Projects

```python
manage_v_1_projects_api = client.manage_v_1_projects
```

## Class Name

`ManageV1ProjectsApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects.md#list)
* [Get](../../doc/controllers/manage-v1-projects.md#get)
* [Update](../../doc/controllers/manage-v1-projects.md#update)
* [Delete](../../doc/controllers/manage-v1-projects.md#delete)
* [Leave](../../doc/controllers/manage-v1-projects.md#leave)


# List

Retrieves basic information about the projects associated with the API key

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A list of projects

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectsV1Response`](../../doc/models/list-projects-v1-response.md).

## Example Usage

```python
authorization = 'Authorization8'

result = manage_v_1_projects_api.list(authorization)

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

Retrieves information about the specified project

:information_source: **Note** This endpoint does not require authentication.

```python
def get(self,
       project_id,
       authorization,
       limit=10,
       page=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `limit` | `float` | Query, Optional | Number of results to return per page. Default 10. Range [1,1000]<br><br>**Default**: `10` |
| `page` | `float` | Query, Optional | Navigate and return the results to retrieve specific portions of information of the response |

## Response Type

**200**: A project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectV1Response`](../../doc/models/get-project-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

limit = 10

result = manage_v_1_projects_api.get(
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


# Update

Updates the name or other properties of an existing project

:information_source: **Note** This endpoint does not require authentication.

```python
def update(self,
          project_id,
          authorization,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`UpdateProjectV1Request`](../../doc/models/update-project-v1-request.md) | Body, Optional | The name of the project |

## Response Type

**200**: A project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateProjectV1Response`](../../doc/models/update-project-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = manage_v_1_projects_api.update(
    project_id,
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


# Delete

Deletes the specified project

:information_source: **Note** This endpoint does not require authentication.

```python
def delete(self,
          project_id,
          authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeleteProjectV1Response`](../../doc/models/delete-project-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = manage_v_1_projects_api.delete(
    project_id,
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


# Leave

Removes the authenticated account from the specific project

:information_source: **Note** This endpoint does not require authentication.

```python
def leave(self,
         project_id,
         authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: Successfully removed account from project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`LeaveProjectV1Response`](../../doc/models/leave-project-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = manage_v_1_projects_api.leave(
    project_id,
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

