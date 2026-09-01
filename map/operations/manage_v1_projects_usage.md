<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsUsage — operations

Accessor: `client.manage_v1_projects_usage` · Source: `rest_api/apis/manage_v1_projects_usage.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_usage.get8

- **Route**: `GET /v1/projects/{project_id}/usage`
- **Auth**: `api_key_auth`
- **Signature**: `def get8(project_id: str, *, start: Date | None = None, end: Date | None = None, accessor: str | None = None, alternatives: bool | None = None, callback_method: bool | None = None, callback: bool | None = None, channels: bool | None = None, custom_intent_mode: bool | None = None, custom_intent: bool | None = None, custom_topic_mode: bool | None = None, custom_topic: bool | None = None, deployment: V1ProjectsProjectIdUsageGetParametersDeploymentOrStr | None = None, detect_entities: bool | None = None, detect_language: bool | None = None, diarize: bool | None = None, dictation: bool | None = None, encoding: bool | None = None, endpoint: V1ProjectsProjectIdUsageGetParametersEndpointOrStr | None = None, extra: bool | None = None, filler_words: bool | None = None, intents: bool | None = None, keyterm: bool | None = None, keywords: bool | None = None, language: bool | None = None, measurements: bool | None = None, method: V1ProjectsProjectIdUsageGetParametersMethodOrStr | None = None, model: str | None = None, multichannel: bool | None = None, numerals: bool | None = None, paragraphs: bool | None = None, profanity_filter: bool | None = None, punctuate: bool | None = None, redact: bool | None = None, replace: bool | None = None, sample_rate: bool | None = None, search: bool | None = None, sentiment: bool | None = None, smart_format: bool | None = None, summarize: bool | None = None, tag: str | None = None, topics: bool | None = None, utt_split: bool | None = None, utterances: bool | None = None, version: bool | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `start` — query · `end` — query · `accessor` — query · `alternatives` — query · `callback_method` — query · `callback` — query · `channels` — query · `custom_intent_mode` — query · `custom_intent` — query · `custom_topic_mode` — query · `custom_topic` — query · `deployment` — query · `detect_entities` — query · `detect_language` — query · `diarize` — query · `dictation` — query · `encoding` — query · `endpoint` — query · `extra` — query · `filler_words` — query · `intents` — query · `keyterm` — query · `keywords` — query · `language` — query · `measurements` — query · `method` — query · `model` — query · `multichannel` — query · `numerals` — query · `paragraphs` — query · `profanity_filter` — query · `punctuate` — query · `redact` — query · `replace` — query · `sample_rate` — query · `search` — query · `sentiment` — query · `smart_format` — query · `summarize` — query · `tag` — query · `topics` — query · `utt_split` — query · `utterances` — query · `version` — query
- **Returns (parsed)**: `UsageV1Response`
- **Returns (raw)**: `ApiResult[UsageV1Response, Get8ErrorBody]`
- **Error**: `Get8ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ProjectsProjectIdUsageGetParametersDeploymentOrStr` | `rest_api/models/enums/v1_projects_project_id_usage_get_parameters_deployment.py` |
| `V1ProjectsProjectIdUsageGetParametersEndpointOrStr` | `rest_api/models/enums/v1_projects_project_id_usage_get_parameters_endpoint.py` |
| `V1ProjectsProjectIdUsageGetParametersMethodOrStr` | `rest_api/models/enums/v1_projects_project_id_usage_get_parameters_method.py` |
| `UsageV1Response` | `rest_api/models/usage_v1_response.py` |
| `Get8ErrorBody` | `rest_api/errors/get8_error.py` |
| `ErrorResponse` | `rest_api/models/unions/error_response.py` |

