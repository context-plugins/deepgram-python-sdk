# Auth V1 Tokens

```python
auth_v_1_tokens_api = client.auth_v_1_tokens
```

## Class Name

`AuthV1TokensApi`


# Grant

Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint will not work with the Manage APIs.

```python
def grant(self,
         body=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GrantV1Request`](../../doc/models/grant-v1-request.md) | Body, Optional | Time to live settings |

## Response Type

**200**: Grant response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GrantV1Response`](../../doc/models/grant-v1-response.md).

## Example Usage

```python
result = auth_v_1_tokens_api.grant()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

