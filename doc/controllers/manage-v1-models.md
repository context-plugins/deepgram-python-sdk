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

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        authorization,
        include_outdated=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `include_outdated` | `bool` | Query, Optional | returns non-latest versions of models |

## Response Type

**200**: A list of models

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListModelsV1Response`](../../doc/models/list-models-v1-response.md).

## Example Usage

```python
authorization = 'Authorization8'

result = manage_v_1_models_api.list(authorization)

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

:information_source: **Note** This endpoint does not require authentication.

```python
def get(self,
       model_id,
       authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_id` | `str` | Template, Required | The specific UUID of the model |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A model object that can be either STT or TTS

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `GetModelV1Response0 | GetModelV1Response1`.

## Example Usage

```python
model_id = 'model_id0'

authorization = 'Authorization8'

result = manage_v_1_models_api.get(
    model_id,
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

