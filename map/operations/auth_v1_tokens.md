<!-- Generated file — do not edit; regenerated with the SDK. -->

# AuthV1Tokens — operations

Accessor: `client.auth_v1_tokens` · Source: `rest_api/apis/auth_v1_tokens.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.auth_v1_tokens.grant

- **Route**: `POST /v1/auth/grant`
- **Auth**: `api_key_auth`
- **Signature**: `def grant(*, body: GrantV1Request | GrantV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GrantV1Response`
- **Returns (raw)**: `ApiResult[GrantV1Response, GrantErrorBody]`
- **Error**: `GrantErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantV1Request` | `rest_api/models/grant_v1_request.py` |
| `GrantV1RequestDict` | `rest_api/models/grant_v1_request.py` |
| `GrantV1Response` | `rest_api/models/grant_v1_response.py` |
| `GrantErrorBody` | `rest_api/errors/grant_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

