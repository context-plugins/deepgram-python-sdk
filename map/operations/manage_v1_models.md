<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1Models — operations

Accessor: `client.manage_v1_models` · Source: `deepgram/apis/manage_v1_models.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_models.get5

- **Route**: `GET /v1/models/{model_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get5(model_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `model_id`
- **Params**: `model_id` — path
- **Returns (parsed)**: `GetModelV1Response`
- **Returns (raw)**: `ApiResult[GetModelV1Response, Get5ErrorBody]`
- **Error**: `Get5ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetModelV1Response` | `deepgram/models/unions/get_model_v1_response.py` |
| `Get5ErrorBody` | `deepgram/errors/get5_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_models.list6

- **Route**: `GET /v1/models`
- **Auth**: `api_key_auth`
- **Signature**: `def list6(*, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_outdated` — query
- **Returns (parsed)**: `ListModelsV1Response`
- **Returns (raw)**: `ApiResult[ListModelsV1Response, List6ErrorBody]`
- **Error**: `List6ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListModelsV1Response` | `deepgram/models/list_models_v1_response.py` |
| `List6ErrorBody` | `deepgram/errors/list6_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

