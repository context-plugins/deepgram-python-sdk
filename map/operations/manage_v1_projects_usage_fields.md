<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsUsageFields — operations

Accessor: `client.manage_v1_projects_usage_fields` · Source: `rest_api/apis/manage_v1_projects_usage_fields.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_usage_fields.list12

- **Route**: `GET /v1/projects/{project_id}/usage/fields`
- **Auth**: `api_key_auth`
- **Signature**: `def list12(project_id: str, *, start: Date | None = None, end: Date | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `start` — query · `end` — query
- **Returns (parsed)**: `UsageFieldsV1Response`
- **Returns (raw)**: `ApiResult[UsageFieldsV1Response, List12ErrorBody]`
- **Error**: `List12ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UsageFieldsV1Response` | `rest_api/models/usage_fields_v1_response.py` |
| `List12ErrorBody` | `rest_api/errors/list12_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

