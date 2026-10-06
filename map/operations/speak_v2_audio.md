<!-- Generated file — do not edit; regenerated with the SDK. -->

# SpeakV2Audio — operations

Accessor: `client.speak_v2_audio` · Source: `deepgram/apis/speak_v2_audio.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.speak_v2_audio.generate2

- **Route**: `POST /v2/speak`
- **Auth**: `api_key_auth`
- **Signature**: `def generate2(model: str, *, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST, mip_opt_out: bool | None = False, tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None, bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None, container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None, encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None, sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None, priority: V2SpeakPostParametersPriorityOrStr | None = None, body: SpeakV2Request | SpeakV2RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `model`
- **Params**: `model` — query · `callback` — query · `callback_method` — query · `mip_opt_out` — query · `tag` — query · `bit_rate` — query · `container` — query · `encoding` — query · `sample_rate` — query · `priority` — query · `body` — JSON body
- **Returns (parsed)**: `SpeakV2AcceptedResponse`
- **Returns (raw)**: `ApiResult[SpeakV2AcceptedResponse, Generate2ErrorBody]`
- **Error**: `Generate2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListenPostParametersCallbackMethodOrStr` | `deepgram/models/enums/v1_listen_post_parameters_callback_method.py` |
| `V2SpeakPostParametersTag` | `deepgram/models/unions/v2_speak_post_parameters_tag.py` |
| `V2SpeakPostParametersTagDict` | `deepgram/models/unions/v2_speak_post_parameters_tag.py` |
| `V2SpeakPostParametersBitRate` | `deepgram/models/unions/v2_speak_post_parameters_bit_rate.py` |
| `V2SpeakPostParametersBitRateDict` | `deepgram/models/unions/v2_speak_post_parameters_bit_rate.py` |
| `V2SpeakPostParametersContainer` | `deepgram/models/unions/v2_speak_post_parameters_container.py` |
| `V2SpeakPostParametersContainerDict` | `deepgram/models/unions/v2_speak_post_parameters_container.py` |
| `V2SpeakPostParametersEncoding` | `deepgram/models/unions/v2_speak_post_parameters_encoding.py` |
| `V2SpeakPostParametersEncodingDict` | `deepgram/models/unions/v2_speak_post_parameters_encoding.py` |
| `V2SpeakPostParametersSampleRate` | `deepgram/models/unions/v2_speak_post_parameters_sample_rate.py` |
| `V2SpeakPostParametersSampleRateDict` | `deepgram/models/unions/v2_speak_post_parameters_sample_rate.py` |
| `V2SpeakPostParametersPriorityOrStr` | `deepgram/models/enums/v2_speak_post_parameters_priority.py` |
| `SpeakV2Request` | `deepgram/models/speak_v2_request.py` |
| `SpeakV2RequestDict` | `deepgram/models/speak_v2_request.py` |
| `SpeakV2AcceptedResponse` | `deepgram/models/speak_v2_accepted_response.py` |
| `Generate2ErrorBody` | `deepgram/errors/generate2_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

