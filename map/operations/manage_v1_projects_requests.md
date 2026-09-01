<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsRequests — operations

Accessor: `client.manage_v1_projects_requests` · Source: `deepgram/apis/manage_v1_projects_requests.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_requests.get7

- **Route**: `GET /v1/projects/{project_id}/requests/{request_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get7(project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `request_id`
- **Params**: `project_id` — path · `request_id` — path
- **Returns (parsed)**: `GetProjectRequestV1Response`
- **Returns (raw)**: `ApiResult[GetProjectRequestV1Response, Get7ErrorBody]`
- **Error**: `Get7ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectRequestV1Response` | `deepgram/models/get_project_request_v1_response.py` |
| `Get7ErrorBody` | `deepgram/errors/get7_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_requests.list11

- **Route**: `GET /v1/projects/{project_id}/requests`
- **Auth**: `api_key_auth`
- **Signature**: `def list11(project_id: str, *, start: RFC3339DateTime | None = None, end: RFC3339DateTime | None = None, limit: float | None = 10.0, page: float | None = None, accessor: str | None = None, request_id: str | None = None, deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None, endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None, method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None, status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `start` — query · `end` — query · `limit` — query · `page` — query · `accessor` — query · `request_id` — query · `deployment` — query · `endpoint` — query · `method` — query · `status` — query
- **Returns (parsed)**: `ListProjectRequestsV1Response`
- **Returns (raw)**: `ApiResult[ListProjectRequestsV1Response, List11ErrorBody]`
- **Error**: `List11ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr` | `deepgram/models/enums/v1_projects_project_id_requests_get_parameters_deployment.py` |
| `V1ProjectsProjectIdRequestsGetParametersEndpointOrStr` | `deepgram/models/enums/v1_projects_project_id_requests_get_parameters_endpoint.py` |
| `V1ProjectsProjectIdRequestsGetParametersMethodOrStr` | `deepgram/models/enums/v1_projects_project_id_requests_get_parameters_method.py` |
| `V1ProjectsProjectIdRequestsGetParametersStatusOrStr` | `deepgram/models/enums/v1_projects_project_id_requests_get_parameters_status.py` |
| `ListProjectRequestsV1Response` | `deepgram/models/list_project_requests_v1_response.py` |
| `List11ErrorBody` | `deepgram/errors/list11_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

