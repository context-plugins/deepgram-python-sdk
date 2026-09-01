<!-- Generated file — do not edit; regenerated with the SDK. -->

# AgentV1SettingsThinkModels — operations

Accessor: `client.agent_v1_settings_think_models` · Source: `rest_api/apis/agent_v1_settings_think_models.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.agent_v1_settings_think_models.list_

- **Route**: `GET /v1/agent/settings/think/models`
- **Auth**: `api_key_auth`
- **Signature**: `def list_(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AgentThinkModelsV1Response`
- **Returns (raw)**: `ApiResult[AgentThinkModelsV1Response, ListErrorBody]`
- **Error**: `ListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AgentThinkModelsV1Response` | `rest_api/models/agent_think_models_v1_response.py` |
| `ListErrorBody` | `rest_api/errors/list_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

