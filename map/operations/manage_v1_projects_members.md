<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsMembers — operations

Accessor: `client.manage_v1_projects_members` · Source: `rest_api/apis/manage_v1_projects_members.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_members.delete5

- **Route**: `DELETE /v1/projects/{project_id}/members/{member_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete5(project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `member_id`
- **Params**: `project_id` — path · `member_id` — path
- **Returns (parsed)**: `DeleteProjectMemberV1Response`
- **Returns (raw)**: `ApiResult[DeleteProjectMemberV1Response, Delete5ErrorBody]`
- **Error**: `Delete5ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteProjectMemberV1Response` | `rest_api/models/delete_project_member_v1_response.py` |
| `Delete5ErrorBody` | `rest_api/errors/delete5_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.manage_v1_projects_members.list8

- **Route**: `GET /v1/projects/{project_id}/members`
- **Auth**: `api_key_auth`
- **Signature**: `def list8(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListProjectMembersV1Response`
- **Returns (raw)**: `ApiResult[ListProjectMembersV1Response, List8ErrorBody]`
- **Error**: `List8ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectMembersV1Response` | `rest_api/models/list_project_members_v1_response.py` |
| `List8ErrorBody` | `rest_api/errors/list8_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

