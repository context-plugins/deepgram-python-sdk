# Manage V1 Models

```python
manage_v_1_models_api = client.manage_v_1_models
```

## Class Name

`ManageV1ModelsApi`

## Methods

* [List](../../doc/controllers/manage-v1-models.md#list)
* [Get](../../doc/controllers/manage-v1-models.md#get)


# List

Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

```python
def list(self,
        include_outdated=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_outdated` | `bool` | Query, Optional | returns non-latest versions of models |

## Response Type

**200**: A list of models

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListModelsV1Response`](../../doc/models/list-models-v1-response.md).

## Example Usage

```python
result = manage_v_1_models_api.list()

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

Returns metadata for a specific public model

```python
def get(self,
       model_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_id` | `str` | Template, Required | The specific UUID of the model |

## Response Type

**200**: A model object that can be either STT or TTS

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `GetModelV1Response0 | GetModelV1Response1`.

## Example Usage

```python
model_id = 'model_id0'

result = manage_v_1_models_api.get(model_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

