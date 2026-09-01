<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsMembersInvites — operations

Accessor: `client.manage_v1_projects_members_invites` · Source: `rest_api/apis/manage_v1_projects_members_invites.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_members_invites.create4

- **Route**: `POST /v1/projects/{project_id}/invites`
- **Auth**: `api_key_auth`
- **Signature**: `def create4(project_id: str, *, body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateProjectInviteV1Response`
- **Returns (raw)**: `ApiResult[CreateProjectInviteV1Response, Create4ErrorBody]`
- **Error**: `Create4ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateProjectInviteV1Request` | `rest_api/models/create_project_invite_v1_request.py` |
| `CreateProjectInviteV1RequestDict` | `rest_api/models/create_project_invite_v1_request.py` |
| `CreateProjectInviteV1Response` | `rest_api/models/create_project_invite_v1_response.py` |
| `Create4ErrorBody` | `rest_api/errors/create4_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.manage_v1_projects_members_invites.delete6

- **Route**: `DELETE /v1/projects/{project_id}/invites/{email}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete6(project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `email`
- **Params**: `project_id` — path · `email` — path
- **Returns (parsed)**: `DeleteProjectInviteV1Response`
- **Returns (raw)**: `ApiResult[DeleteProjectInviteV1Response, Delete6ErrorBody]`
- **Error**: `Delete6ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteProjectInviteV1Response` | `rest_api/models/delete_project_invite_v1_response.py` |
| `Delete6ErrorBody` | `rest_api/errors/delete6_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.manage_v1_projects_members_invites.list10

- **Route**: `GET /v1/projects/{project_id}/invites`
- **Auth**: `api_key_auth`
- **Signature**: `def list10(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListProjectInvitesV1Response`
- **Returns (raw)**: `ApiResult[ListProjectInvitesV1Response, List10ErrorBody]`
- **Error**: `List10ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectInvitesV1Response` | `rest_api/models/list_project_invites_v1_response.py` |
| `List10ErrorBody` | `rest_api/errors/list10_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

