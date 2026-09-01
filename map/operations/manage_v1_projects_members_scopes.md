<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsMembersScopes — operations

Accessor: `client.manage_v1_projects_members_scopes` · Source: `deepgram/apis/manage_v1_projects_members_scopes.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_members_scopes.list9

- **Route**: `GET /v1/projects/{project_id}/members/{member_id}/scopes`
- **Auth**: `api_key_auth`
- **Signature**: `def list9(project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `member_id`
- **Params**: `project_id` — path · `member_id` — path
- **Returns (parsed)**: `ListProjectMemberScopesV1Response`
- **Returns (raw)**: `ApiResult[ListProjectMemberScopesV1Response, List9ErrorBody]`
- **Error**: `List9ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectMemberScopesV1Response` | `deepgram/models/list_project_member_scopes_v1_response.py` |
| `List9ErrorBody` | `deepgram/errors/list9_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_members_scopes.update4

- **Route**: `PUT /v1/projects/{project_id}/members/{member_id}/scopes`
- **Auth**: `api_key_auth`
- **Signature**: `def update4(project_id: str, member_id: str, *, body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `member_id`
- **Params**: `project_id` — path · `member_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateProjectMemberScopesV1Response`
- **Returns (raw)**: `ApiResult[UpdateProjectMemberScopesV1Response, Update4ErrorBody]`
- **Error**: `Update4ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateProjectMemberScopesV1Request` | `deepgram/models/update_project_member_scopes_v1_request.py` |
| `UpdateProjectMemberScopesV1RequestDict` | `deepgram/models/update_project_member_scopes_v1_request.py` |
| `UpdateProjectMemberScopesV1Response` | `deepgram/models/update_project_member_scopes_v1_response.py` |
| `Update4ErrorBody` | `deepgram/errors/update4_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

