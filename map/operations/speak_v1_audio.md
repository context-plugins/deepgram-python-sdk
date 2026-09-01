<!-- Generated file — do not edit; regenerated with the SDK. -->

# SpeakV1Audio — operations

Accessor: `client.speak_v1_audio` · Source: `deepgram/apis/speak_v1_audio.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.speak_v1_audio.generate

- **Route**: `POST /v1/speak`
- **Auth**: `api_key_auth`
- **Signature**: `def generate(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, mip_opt_out: bool | None = False, tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None, bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None, container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None, encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None, model: V1SpeakPostParametersModelOrStr | None = None, sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None, speed: float | None = 1.0, body: SpeakV1Request | SpeakV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `callback` — query · `callback_method` — query · `mip_opt_out` — query · `tag` — query · `bit_rate` — query · `container` — query · `encoding` — query · `model` — query · `sample_rate` — query · `speed` — query · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GenerateErrorBody]`
- **Error**: `GenerateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListenPostParametersCallbackMethodOrStr` | `deepgram/models/enums/v1_listen_post_parameters_callback_method.py` |
| `V1SpeakPostParametersTag` | `deepgram/models/unions/v1_speak_post_parameters_tag.py` |
| `V1SpeakPostParametersTagDict` | `deepgram/models/unions/v1_speak_post_parameters_tag.py` |
| `V1SpeakPostParametersBitRate` | `deepgram/models/unions/v1_speak_post_parameters_bit_rate.py` |
| `V1SpeakPostParametersBitRateDict` | `deepgram/models/unions/v1_speak_post_parameters_bit_rate.py` |
| `V1SpeakPostParametersContainer` | `deepgram/models/unions/v1_speak_post_parameters_container.py` |
| `V1SpeakPostParametersContainerDict` | `deepgram/models/unions/v1_speak_post_parameters_container.py` |
| `V1SpeakPostParametersEncoding` | `deepgram/models/unions/v1_speak_post_parameters_encoding.py` |
| `V1SpeakPostParametersEncodingDict` | `deepgram/models/unions/v1_speak_post_parameters_encoding.py` |
| `V1SpeakPostParametersModelOrStr` | `deepgram/models/enums/v1_speak_post_parameters_model.py` |
| `V1SpeakPostParametersSampleRate` | `deepgram/models/unions/v1_speak_post_parameters_sample_rate.py` |
| `V1SpeakPostParametersSampleRateDict` | `deepgram/models/unions/v1_speak_post_parameters_sample_rate.py` |
| `SpeakV1Request` | `deepgram/models/speak_v1_request.py` |
| `SpeakV1RequestDict` | `deepgram/models/speak_v1_request.py` |
| `GenerateErrorBody` | `deepgram/errors/generate_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

