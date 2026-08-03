# Auth V1 Tokens

```python
auth_v_1_tokens_api = client.auth_v_1_tokens
```

## Class Name

`AuthV1TokensApi`


# Grant

Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint will not work with the Manage APIs.

:information_source: **Note** This endpoint does not require authentication.

```python
def grant(self,
         authorization,
         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`GrantV1Request`](../../doc/models/grant-v1-request.md) | Body, Optional | Time to live settings |

## Response Type

**200**: Grant response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GrantV1Response`](../../doc/models/grant-v1-response.md).

## Example Usage

```python
authorization = 'Authorization8'

result = auth_v_1_tokens_api.grant(authorization)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

