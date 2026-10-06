<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReadV1Text — operations

Accessor: `client.read_v1_text` · Source: `deepgram/apis/read_v1_text.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.read_v1_text.analyze

- **Route**: `POST /v1/read`
- **Auth**: `api_key_auth`
- **Signature**: `def analyze(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST, sentiment: bool | None = False, summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None, tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None, topics: bool | None = False, custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None, custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = V1ListenPostParametersCustomTopicMode.EXTENDED, intents: bool | None = False, custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None, custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = V1ListenPostParametersCustomTopicMode.EXTENDED, language: str | None = "en", body: ReadV1Request | ReadV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `callback` — query · `callback_method` — query · `sentiment` — query · `summarize` — query · `tag` — query · `topics` — query · `custom_topic` — query · `custom_topic_mode` — query · `intents` — query · `custom_intent` — query · `custom_intent_mode` — query · `language` — query · `body` — JSON body
- **Returns (parsed)**: `ReadV1Response`
- **Returns (raw)**: `ApiResult[ReadV1Response, AnalyzeErrorBody]`
- **Error**: `AnalyzeErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListenPostParametersCallbackMethodOrStr` | `deepgram/models/enums/v1_listen_post_parameters_callback_method.py` |
| `V1ReadPostParametersSummarize` | `deepgram/models/unions/v1_read_post_parameters_summarize.py` |
| `V1ReadPostParametersSummarizeDict` | `deepgram/models/unions/v1_read_post_parameters_summarize.py` |
| `V1ReadPostParametersTag` | `deepgram/models/unions/v1_read_post_parameters_tag.py` |
| `V1ReadPostParametersTagDict` | `deepgram/models/unions/v1_read_post_parameters_tag.py` |
| `V1ReadPostParametersCustomTopic` | `deepgram/models/unions/v1_read_post_parameters_custom_topic.py` |
| `V1ReadPostParametersCustomTopicDict` | `deepgram/models/unions/v1_read_post_parameters_custom_topic.py` |
| `V1ListenPostParametersCustomTopicModeOrStr` | `deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py` |
| `V1ReadPostParametersCustomIntent` | `deepgram/models/unions/v1_read_post_parameters_custom_intent.py` |
| `V1ReadPostParametersCustomIntentDict` | `deepgram/models/unions/v1_read_post_parameters_custom_intent.py` |
| `ReadV1Request` | `deepgram/models/unions/read_v1_request.py` |
| `ReadV1RequestDict` | `deepgram/models/unions/read_v1_request.py` |
| `ReadV1Response` | `deepgram/models/read_v1_response.py` |
| `AnalyzeErrorBody` | `deepgram/errors/analyze_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

