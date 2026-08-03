# Speak V2 Audio

```python
speak_v_2_audio_api = client.speak_v_2_audio
```

## Class Name

`SpeakV2AudioApi`


# Generate

Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API. Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up front and you don't need incremental playback or interruption.

:information_source: **Note** This endpoint does not require authentication.

```python
def generate(self,
            model,
            authorization,
            callback=None,
            callback_method="POST",
            mip_opt_out=False,
            tag=None,
            bit_rate=None,
            container=None,
            encoding=None,
            sample_rate=None,
            priority=None,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | `str` | Query, Required | Flux TTS model used to synthesize the submitted text, in the form `flux-{voice}-{language}` (for example, `flux-alexis-en`). Required; unlike the v1 (Aura) endpoint there is no default and only flux models are accepted. English-only at launch. |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `callback` | `str` | Query, Optional | URL to which we'll make the callback request |
| `callback_method` | [`V1ListenPostParametersCallbackMethod`](../../doc/models/v1-listen-post-parameters-callback-method.md) | Query, Optional | HTTP method by which the callback request will be made<br><br>**Default**: `"POST"` |
| `mip_opt_out` | `bool` | Query, Optional | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br><br>**Default**: `False` |
| `tag` | str \| List[str] \| None | Query, Optional | Label your requests for the purpose of identification during usage reporting |
| `bit_rate` | [V2SpeakPostParametersBitRate0](../../doc/models/v2-speak-post-parameters-bit-rate-0.md) \| int \| None | Query, Optional | This is a container for one-of cases. |
| `container` | [V2SpeakPostParametersContainer0](../../doc/models/v2-speak-post-parameters-container-0.md) \| [V2SpeakPostParametersContainer1](../../doc/models/v2-speak-post-parameters-container-1.md) \| [V2SpeakPostParametersContainer2](../../doc/models/v2-speak-post-parameters-container-2.md) \| [V2SpeakPostParametersContainer3](../../doc/models/v2-speak-post-parameters-container-3.md) \| [V2SpeakPostParametersContainer4](../../doc/models/v2-speak-post-parameters-container-4.md) \| None | Query, Optional | This is a container for one-of cases. |
| `encoding` | [V2SpeakPostParametersEncoding0](../../doc/models/v2-speak-post-parameters-encoding-0.md) \| [V2SpeakPostParametersEncoding1](../../doc/models/v2-speak-post-parameters-encoding-1.md) \| [V2SpeakPostParametersEncoding2](../../doc/models/v2-speak-post-parameters-encoding-2.md) \| [V2SpeakPostParametersEncoding3](../../doc/models/v2-speak-post-parameters-encoding-3.md) \| [V2SpeakPostParametersEncoding4](../../doc/models/v2-speak-post-parameters-encoding-4.md) \| [V2SpeakPostParametersEncoding5](../../doc/models/v2-speak-post-parameters-encoding-5.md) \| [V2SpeakPostParametersEncoding6](../../doc/models/v2-speak-post-parameters-encoding-6.md) \| None | Query, Optional | This is a container for one-of cases. |
| `sample_rate` | [V2SpeakPostParametersSampleRate0](../../doc/models/v2-speak-post-parameters-sample-rate-0.md) \| [V2SpeakPostParametersSampleRate1](../../doc/models/v2-speak-post-parameters-sample-rate-1.md) \| [V2SpeakPostParametersSampleRate2](../../doc/models/v2-speak-post-parameters-sample-rate-2.md) \| [V2SpeakPostParametersSampleRate3](../../doc/models/v2-speak-post-parameters-sample-rate-3.md) \| None | Query, Optional | This is a container for one-of cases. |
| `priority` | [`V2SpeakPostParametersPriority`](../../doc/models/v2-speak-post-parameters-priority.md) | Query, Optional | Processing priority for asynchronous (callback) requests. The only supported value is low. |
| `body` | [`SpeakV2Request`](../../doc/models/speak-v2-request.md) | Body, Optional | Transform text to speech |

## Response Type

**200**: Returns the synthesized audio in the requested encoding as a binary stream. When a `callback` URL is supplied, the request is processed asynchronously and the response body is instead a JSON acknowledgement (Content-Type `application/json`) of the form {"request_id": "..."}, with the audio delivered to the callback URL. Because this endpoint is typed as a binary audio stream, SDK callers that set `callback` receive this JSON acknowledgement through the audio byte iterator as raw bytes and must join the chunks and parse `request_id` themselves.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SpeakV2AcceptedResponse`](../../doc/models/speak-v2-accepted-response.md).

## Example Usage

```python
model = 'model2'

authorization = 'Authorization8'

callback_method = V1ListenPostParametersCallbackMethod.POST

mip_opt_out = False

result = speak_v_2_audio_api.generate(
    model,
    authorization,
    callback_method=callback_method,
    mip_opt_out=mip_opt_out
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

