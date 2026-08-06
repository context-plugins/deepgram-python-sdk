# Manage V1 Projects Keys

```python
manage_v_1_projects_keys_api = client.manage_v_1_projects_keys
```

## Class Name

`ManageV1ProjectsKeysApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-keys.md#list)
* [Create](../../doc/controllers/manage-v1-projects-keys.md#create)
* [Get](../../doc/controllers/manage-v1-projects-keys.md#get)
* [Delete](../../doc/controllers/manage-v1-projects-keys.md#delete)


# List

Retrieves all API keys associated with the specified project

```python
def list(self,
        project_id,
        status=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `status` | [`V1ProjectsProjectIdKeysGetParametersStatus`](../../doc/models/v1-projects-project-id-keys-get-parameters-status.md) | Query, Optional | Only return keys with a specific status |

## Response Type

**200**: A list of API keys

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectKeysV1Response`](../../doc/models/list-project-keys-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_keys_api.list(project_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Create

Creates a new API key with specified settings for the project

```python
def create(self,
          project_id,
          body=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `body` | Any \| None | Body, Optional | API key settings |

## Response Type

**200**: API key created successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateKeyV1Response`](../../doc/models/create-key-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_keys_api.create(project_id)

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

Retrieves information about a specified API key

```python
def get(self,
       project_id,
       key_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `key_id` | `str` | Template, Required | The unique identifier of the API key |

## Response Type

**200**: A specific API key

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectKeyV1Response`](../../doc/models/get-project-key-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

key_id = 'key_id4'

result = manage_v_1_projects_keys_api.get(
    project_id,
    key_id
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

Deletes an API key for a specific project

```python
def delete(self,
          project_id,
          key_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `key_id` | `str` | Template, Required | The unique identifier of the API key |

## Response Type

**200**: API key deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeleteProjectKeyV1Response`](../../doc/models/delete-project-key-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

key_id = 'key_id4'

result = manage_v_1_projects_keys_api.delete(
    project_id,
    key_id
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

