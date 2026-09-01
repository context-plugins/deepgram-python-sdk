<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsKeys — operations

Accessor: `client.manage_v1_projects_keys` · Source: `deepgram/apis/manage_v1_projects_keys.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_keys.create3

- **Route**: `POST /v1/projects/{project_id}/keys`
- **Auth**: `api_key_auth`
- **Signature**: `def create3(project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateKeyV1Response`
- **Returns (raw)**: `ApiResult[CreateKeyV1Response, Create3ErrorBody]`
- **Error**: `Create3ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateKeyV1Response` | `deepgram/models/create_key_v1_response.py` |
| `Create3ErrorBody` | `deepgram/errors/create3_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_keys.delete4

- **Route**: `DELETE /v1/projects/{project_id}/keys/{key_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete4(project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `key_id`
- **Params**: `project_id` — path · `key_id` — path
- **Returns (parsed)**: `DeleteProjectKeyV1Response`
- **Returns (raw)**: `ApiResult[DeleteProjectKeyV1Response, Delete4ErrorBody]`
- **Error**: `Delete4ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteProjectKeyV1Response` | `deepgram/models/delete_project_key_v1_response.py` |
| `Delete4ErrorBody` | `deepgram/errors/delete4_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_keys.get6

- **Route**: `GET /v1/projects/{project_id}/keys/{key_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get6(project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `key_id`
- **Params**: `project_id` — path · `key_id` — path
- **Returns (parsed)**: `GetProjectKeyV1Response`
- **Returns (raw)**: `ApiResult[GetProjectKeyV1Response, Get6ErrorBody]`
- **Error**: `Get6ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectKeyV1Response` | `deepgram/models/get_project_key_v1_response.py` |
| `Get6ErrorBody` | `deepgram/errors/get6_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_keys.list7

- **Route**: `GET /v1/projects/{project_id}/keys`
- **Auth**: `api_key_auth`
- **Signature**: `def list7(project_id: str, *, status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `status` — query
- **Returns (parsed)**: `ListProjectKeysV1Response`
- **Returns (raw)**: `ApiResult[ListProjectKeysV1Response, List7ErrorBody]`
- **Error**: `List7ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ProjectsProjectIdKeysGetParametersStatusOrStr` | `deepgram/models/enums/v1_projects_project_id_keys_get_parameters_status.py` |
| `ListProjectKeysV1Response` | `deepgram/models/list_project_keys_v1_response.py` |
| `List7ErrorBody` | `deepgram/errors/list7_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

