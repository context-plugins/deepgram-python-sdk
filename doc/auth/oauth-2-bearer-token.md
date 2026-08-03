
# OAuth 2 Bearer token



Documentation for accessing and setting credentials for JwtAuth.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| AccessToken | `str` | The OAuth 2.0 Access Token to use for API requests. | `access_token` |



**Note:** Auth credentials can be set using `JwtAuthCredentials` object, passed in as named parameter `jwt_auth_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
from restapi.http.auth.jwt_auth import JwtAuthCredentials
from restapi.restapi_client import RestapiClient

client = RestapiClient(
    jwt_auth_credentials=JwtAuthCredentials(
        access_token='AccessToken'
    )
)
```


