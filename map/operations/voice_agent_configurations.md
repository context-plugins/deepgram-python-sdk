<!-- Generated file — do not edit; regenerated with the SDK. -->

# VoiceAgentConfigurations — operations

Accessor: `client.voice_agent_configurations` · Source: `rest_api/apis/voice_agent_configurations.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.voice_agent_configurations.create

- **Route**: `POST /v1/projects/{project_id}/agents`
- **Auth**: `api_key_auth`
- **Signature**: `def create(project_id: str, *, body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateAgentConfigurationV1Response`
- **Returns (raw)**: `ApiResult[CreateAgentConfigurationV1Response, CreateErrorBody]`
- **Error**: `CreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAgentConfigurationV1Request` | `rest_api/models/create_agent_configuration_v1_request.py` |
| `CreateAgentConfigurationV1RequestDict` | `rest_api/models/create_agent_configuration_v1_request.py` |
| `CreateAgentConfigurationV1Response` | `rest_api/models/create_agent_configuration_v1_response.py` |
| `CreateErrorBody` | `rest_api/errors/create_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.voice_agent_configurations.delete

- **Route**: `DELETE /v1/projects/{project_id}/agents/{agent_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete(project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `agent_id`
- **Params**: `project_id` — path · `agent_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DeleteErrorBody]`
- **Error**: `DeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteErrorBody` | `rest_api/errors/delete_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.voice_agent_configurations.get

- **Route**: `GET /v1/projects/{project_id}/agents/{agent_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get(project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `agent_id`
- **Params**: `project_id` — path · `agent_id` — path
- **Returns (parsed)**: `AgentConfigurationV1`
- **Returns (raw)**: `ApiResult[AgentConfigurationV1, GetErrorBody]`
- **Error**: `GetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentConfigurationV1` | `rest_api/models/agent_configuration_v1.py` |
| `GetErrorBody` | `rest_api/errors/get_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.voice_agent_configurations.list2

- **Route**: `GET /v1/projects/{project_id}/agents`
- **Auth**: `api_key_auth`
- **Signature**: `def list2(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListAgentConfigurationsV1Response`
- **Returns (raw)**: `ApiResult[ListAgentConfigurationsV1Response, List2ErrorBody]`
- **Error**: `List2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListAgentConfigurationsV1Response` | `rest_api/models/list_agent_configurations_v1_response.py` |
| `List2ErrorBody` | `rest_api/errors/list2_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

### client.voice_agent_configurations.update

- **Route**: `PUT /v1/projects/{project_id}/agents/{agent_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def update(project_id: str, agent_id: str, *, body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `agent_id`
- **Params**: `project_id` — path · `agent_id` — path · `body` — JSON body
- **Returns (parsed)**: `AgentConfigurationV1`
- **Returns (raw)**: `ApiResult[AgentConfigurationV1, UpdateErrorBody]`
- **Error**: `UpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateAgentMetadataV1Request` | `rest_api/models/update_agent_metadata_v1_request.py` |
| `UpdateAgentMetadataV1RequestDict` | `rest_api/models/update_agent_metadata_v1_request.py` |
| `AgentConfigurationV1` | `rest_api/models/agent_configuration_v1.py` |
| `UpdateErrorBody` | `rest_api/errors/update_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

