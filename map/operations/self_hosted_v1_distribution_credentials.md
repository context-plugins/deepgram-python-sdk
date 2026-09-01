<!-- Generated file — do not edit; regenerated with the SDK. -->

# SelfHostedV1DistributionCredentials — operations

Accessor: `client.self_hosted_v1_distribution_credentials` · Source: `deepgram/apis/self_hosted_v1_distribution_credentials.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.self_hosted_v1_distribution_credentials.create5

- **Route**: `POST /v1/projects/{project_id}/self-hosted/distribution/credentials`
- **Auth**: `api_key_auth`
- **Signature**: `def create5(project_id: str, *, scopes: list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None = None, provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None, body: CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `scopes` — query · `provider` — query · `body` — JSON body
- **Returns (parsed)**: `CreateProjectDistributionCredentialsV1Response`
- **Returns (raw)**: `ApiResult[CreateProjectDistributionCredentialsV1Response, Create5ErrorBody]`
- **Error**: `Create5ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr` | `deepgram/models/enums/v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_scopes_schema_items.py` |
| `V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr` | `deepgram/models/enums/v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_provider.py` |
| `CreateProjectDistributionCredentialsV1Request` | `deepgram/models/create_project_distribution_credentials_v1_request.py` |
| `CreateProjectDistributionCredentialsV1RequestDict` | `deepgram/models/create_project_distribution_credentials_v1_request.py` |
| `CreateProjectDistributionCredentialsV1Response` | `deepgram/models/create_project_distribution_credentials_v1_response.py` |
| `Create5ErrorBody` | `deepgram/errors/create5_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.self_hosted_v1_distribution_credentials.delete7

- **Route**: `DELETE /v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete7(project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `distribution_credentials_id`
- **Params**: `project_id` — path · `distribution_credentials_id` — path
- **Returns (parsed)**: `GetProjectDistributionCredentialsV1Response`
- **Returns (raw)**: `ApiResult[GetProjectDistributionCredentialsV1Response, Delete7ErrorBody]`
- **Error**: `Delete7ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectDistributionCredentialsV1Response` | `deepgram/models/get_project_distribution_credentials_v1_response.py` |
| `Delete7ErrorBody` | `deepgram/errors/delete7_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.self_hosted_v1_distribution_credentials.get11

- **Route**: `GET /v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get11(project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `distribution_credentials_id`
- **Params**: `project_id` — path · `distribution_credentials_id` — path
- **Returns (parsed)**: `GetProjectDistributionCredentialsV1Response`
- **Returns (raw)**: `ApiResult[GetProjectDistributionCredentialsV1Response, Get11ErrorBody]`
- **Error**: `Get11ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectDistributionCredentialsV1Response` | `deepgram/models/get_project_distribution_credentials_v1_response.py` |
| `Get11ErrorBody` | `deepgram/errors/get11_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.self_hosted_v1_distribution_credentials.list17

- **Route**: `GET /v1/projects/{project_id}/self-hosted/distribution/credentials`
- **Auth**: `api_key_auth`
- **Signature**: `def list17(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListProjectDistributionCredentialsV1Response`
- **Returns (raw)**: `ApiResult[ListProjectDistributionCredentialsV1Response, List17ErrorBody]`
- **Error**: `List17ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectDistributionCredentialsV1Response` | `deepgram/models/list_project_distribution_credentials_v1_response.py` |
| `List17ErrorBody` | `deepgram/errors/list17_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

