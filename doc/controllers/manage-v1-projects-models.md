# Manage V1 Projects Models

```python
manage_v_1_projects_models_api = client.manage_v_1_projects_models
```

## Class Name

`ManageV1ProjectsModelsApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-models.md#list)
* [Get](../../doc/controllers/manage-v1-projects-models.md#get)


# List

Returns metadata on all the latest models that a specific project has access to, including non-public models

```python
def list(self,
        project_id,
        include_outdated=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `include_outdated` | `bool` | Query, Optional | returns non-latest versions of models |

## Response Type

**200**: A list of models

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListModelsV1Response`](../../doc/models/list-models-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_models_api.list(project_id)

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

Returns metadata for a specific model

```python
def get(self,
       project_id,
       model_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `model_id` | `str` | Template, Required | The specific UUID of the model |

## Response Type

**200**: A model object that can be either STT or TTS

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `GetModelV1Response0 | GetModelV1Response1`.

## Example Usage

```python
project_id = 'project_id6'

model_id = 'model_id0'

result = manage_v_1_projects_models_api.get(
    project_id,
    model_id
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

