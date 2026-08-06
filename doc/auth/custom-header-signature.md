
# Custom Header Signature



Documentation for accessing and setting credentials for ApiKeyAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| Authorization | `str` | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` | `authorization` |



**Note:** Auth credentials can be set using `ApiKeyAuthCredentials` object, passed in as named parameter `api_key_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from deepgram.deepgram_client import DeepgramClient
from deepgram.http.auth.api_key_auth import ApiKeyAuthCredentials

client = DeepgramClient(
    api_key_auth_credentials=ApiKeyAuthCredentials(
        authorization='Authorization'
    )
)
```


