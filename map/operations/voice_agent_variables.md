<!-- Generated file — do not edit; regenerated with the SDK. -->

# VoiceAgentVariables — operations

Accessor: `client.voice_agent_variables` · Source: `deepgram/apis/voice_agent_variables.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.voice_agent_variables.create2

- **Route**: `POST /v1/projects/{project_id}/agent-variables`
- **Auth**: `api_key_auth`
- **Signature**: `def create2(project_id: str, *, body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `body` — JSON body
- **Returns (parsed)**: `AgentVariableV1`
- **Returns (raw)**: `ApiResult[AgentVariableV1, Create2ErrorBody]`
- **Error**: `Create2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateAgentVariableV1Request` | `deepgram/models/create_agent_variable_v1_request.py` |
| `CreateAgentVariableV1RequestDict` | `deepgram/models/create_agent_variable_v1_request.py` |
| `AgentVariableV1` | `deepgram/models/agent_variable_v1.py` |
| `Create2ErrorBody` | `deepgram/errors/create2_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.voice_agent_variables.delete2

- **Route**: `DELETE /v1/projects/{project_id}/agent-variables/{variable_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def delete2(project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `variable_id`
- **Params**: `project_id` — path · `variable_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, Delete2ErrorBody]`
- **Error**: `Delete2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Delete2ErrorBody` | `deepgram/errors/delete2_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.voice_agent_variables.get2

- **Route**: `GET /v1/projects/{project_id}/agent-variables/{variable_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get2(project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `variable_id`
- **Params**: `project_id` — path · `variable_id` — path
- **Returns (parsed)**: `AgentVariableV1`
- **Returns (raw)**: `ApiResult[AgentVariableV1, Get2ErrorBody]`
- **Error**: `Get2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentVariableV1` | `deepgram/models/agent_variable_v1.py` |
| `Get2ErrorBody` | `deepgram/errors/get2_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.voice_agent_variables.list3

- **Route**: `GET /v1/projects/{project_id}/agent-variables`
- **Auth**: `api_key_auth`
- **Signature**: `def list3(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListAgentVariablesV1Response`
- **Returns (raw)**: `ApiResult[ListAgentVariablesV1Response, List3ErrorBody]`
- **Error**: `List3ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListAgentVariablesV1Response` | `deepgram/models/list_agent_variables_v1_response.py` |
| `List3ErrorBody` | `deepgram/errors/list3_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.voice_agent_variables.update2

- **Route**: `PATCH /v1/projects/{project_id}/agent-variables/{variable_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def update2(project_id: str, variable_id: str, *, body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `variable_id`
- **Params**: `project_id` — path · `variable_id` — path · `body` — JSON body
- **Returns (parsed)**: `AgentVariableV1`
- **Returns (raw)**: `ApiResult[AgentVariableV1, Update2ErrorBody]`
- **Error**: `Update2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateAgentVariableV1Request` | `deepgram/models/update_agent_variable_v1_request.py` |
| `UpdateAgentVariableV1RequestDict` | `deepgram/models/update_agent_variable_v1_request.py` |
| `AgentVariableV1` | `deepgram/models/agent_variable_v1.py` |
| `Update2ErrorBody` | `deepgram/errors/update2_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

