<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1Projects — operations

Accessor: `client.manage_v1_projects` · Source: `deepgram/apis/manage_v1_projects.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects.delete3

- **Route**: `DELETE /v1/projects/{project_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete3(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `DeleteProjectV1Response`
- **Returns (raw)**: `ApiResult[DeleteProjectV1Response, Delete3ErrorBody]`
- **Error**: `Delete3ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteProjectV1Response` | `deepgram/models/delete_project_v1_response.py` |
| `Delete3ErrorBody` | `deepgram/errors/delete3_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects.get3

- **Route**: `GET /v1/projects/{project_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get3(project_id: str, *, limit: float | None = 10.0, page: float | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `limit` — query · `page` — query
- **Returns (parsed)**: `GetProjectV1Response`
- **Returns (raw)**: `ApiResult[GetProjectV1Response, Get3ErrorBody]`
- **Error**: `Get3ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectV1Response` | `deepgram/models/get_project_v1_response.py` |
| `Get3ErrorBody` | `deepgram/errors/get3_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects.leave

- **Route**: `DELETE /v1/projects/{project_id}/leave`
- **Auth**: `api_key_auth`
- **Signature**: `def leave(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `LeaveProjectV1Response`
- **Returns (raw)**: `ApiResult[LeaveProjectV1Response, LeaveErrorBody]`
- **Error**: `LeaveErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `LeaveProjectV1Response` | `deepgram/models/leave_project_v1_response.py` |
| `LeaveErrorBody` | `deepgram/errors/leave_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects.list4

- **Route**: `GET /v1/projects`
- **Auth**: `api_key_auth`
- **Signature**: `def list4(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ListProjectsV1Response`
- **Returns (raw)**: `ApiResult[ListProjectsV1Response, List4ErrorBody]`
- **Error**: `List4ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectsV1Response` | `deepgram/models/list_projects_v1_response.py` |
| `List4ErrorBody` | `deepgram/errors/list4_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects.update3

- **Route**: `PATCH /v1/projects/{project_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def update3(project_id: str, *, body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateProjectV1Response`
- **Returns (raw)**: `ApiResult[UpdateProjectV1Response, Update3ErrorBody]`
- **Error**: `Update3ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateProjectV1Request` | `deepgram/models/update_project_v1_request.py` |
| `UpdateProjectV1RequestDict` | `deepgram/models/update_project_v1_request.py` |
| `UpdateProjectV1Response` | `deepgram/models/update_project_v1_response.py` |
| `Update3ErrorBody` | `deepgram/errors/update3_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

