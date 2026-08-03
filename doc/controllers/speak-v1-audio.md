# Speak V1 Audio

```python
speak_v_1_audio_api = client.speak_v_1_audio
```

## Class Name

`SpeakV1AudioApi`


# Generate

Convert text into natural-sounding speech using Deepgram's TTS REST API

:information_source: **Note** This endpoint does not require authentication.

```python
def generate(self,
            authorization,
            callback=None,
            callback_method="POST",
            mip_opt_out=False,
            tag=None,
            bit_rate=None,
            container=None,
            encoding=None,
            model="aura-asteria-en",
            sample_rate=None,
            speed=1,
            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `callback` | `str` | Query, Optional | URL to which we'll make the callback request |
| `callback_method` | [`V1ListenPostParametersCallbackMethod`](../../doc/models/v1-listen-post-parameters-callback-method.md) | Query, Optional | HTTP method by which the callback request will be made<br><br>**Default**: `"POST"` |
| `mip_opt_out` | `bool` | Query, Optional | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br><br>**Default**: `False` |
| `tag` | str \| List[str] \| None | Query, Optional | Label your requests for the purpose of identification during usage reporting |
| `bit_rate` | [V1SpeakPostParametersBitRate0](../../doc/models/v1-speak-post-parameters-bit-rate-0.md) \| float \| None | Query, Optional | This is a container for one-of cases. |
| `container` | [V1SpeakPostParametersContainer0](../../doc/models/v1-speak-post-parameters-container-0.md) \| [V1SpeakPostParametersContainer1](../../doc/models/v1-speak-post-parameters-container-1.md) \| [V1SpeakPostParametersContainer2](../../doc/models/v1-speak-post-parameters-container-2.md) \| [V1SpeakPostParametersContainer3](../../doc/models/v1-speak-post-parameters-container-3.md) \| [V1SpeakPostParametersContainer4](../../doc/models/v1-speak-post-parameters-container-4.md) \| None | Query, Optional | This is a container for one-of cases. |
| `encoding` | [V1SpeakPostParametersEncoding0](../../doc/models/v1-speak-post-parameters-encoding-0.md) \| [V1SpeakPostParametersEncoding1](../../doc/models/v1-speak-post-parameters-encoding-1.md) \| [V1SpeakPostParametersEncoding2](../../doc/models/v1-speak-post-parameters-encoding-2.md) \| [V1SpeakPostParametersEncoding3](../../doc/models/v1-speak-post-parameters-encoding-3.md) \| [V1SpeakPostParametersEncoding4](../../doc/models/v1-speak-post-parameters-encoding-4.md) \| [V1SpeakPostParametersEncoding5](../../doc/models/v1-speak-post-parameters-encoding-5.md) \| [V1SpeakPostParametersEncoding6](../../doc/models/v1-speak-post-parameters-encoding-6.md) \| None | Query, Optional | This is a container for one-of cases. |
| `model` | [`V1SpeakPostParametersModel`](../../doc/models/v1-speak-post-parameters-model.md) | Query, Optional | AI model used to process submitted text<br><br>**Default**: `"aura-asteria-en"` |
| `sample_rate` | [V1SpeakPostParametersSampleRate0](../../doc/models/v1-speak-post-parameters-sample-rate-0.md) \| [V1SpeakPostParametersSampleRate1](../../doc/models/v1-speak-post-parameters-sample-rate-1.md) \| [V1SpeakPostParametersSampleRate2](../../doc/models/v1-speak-post-parameters-sample-rate-2.md) \| [V1SpeakPostParametersSampleRate3](../../doc/models/v1-speak-post-parameters-sample-rate-3.md) \| [V1SpeakPostParametersSampleRate4](../../doc/models/v1-speak-post-parameters-sample-rate-4.md) \| None | Query, Optional | This is a container for one-of cases. |
| `speed` | `float` | Query, Optional | Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody and voice quality. Not yet supported in all languages.<br><br>**Default**: `1` |
| `body` | [`SpeakV1Request`](../../doc/models/speak-v1-request.md) | Body, Optional | Transform text to speech |

## Response Type

**200**: Successful text-to-speech transformation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
authorization = 'Authorization8'

callback_method = V1ListenPostParametersCallbackMethod.POST

mip_opt_out = False

model = V1SpeakPostParametersModel.AURAASTERIAEN

speed = 1

result = speak_v_1_audio_api.generate(
    authorization,
    callback_method=callback_method,
    mip_opt_out=mip_opt_out,
    model=model,
    speed=speed
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

