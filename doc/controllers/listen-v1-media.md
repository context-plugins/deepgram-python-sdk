# Listen V1 Media

```python
listen_v_1_media_api = client.listen_v_1_media
```

## Class Name

`ListenV1MediaApi`


# Transcribe

Transcribe audio and video using Deepgram's speech-to-text REST API

:information_source: **Note** This endpoint does not require authentication.

```python
def transcribe(self,
              authorization,
              callback=None,
              callback_method="POST",
              extra=None,
              sentiment=False,
              summarize=None,
              tag=None,
              topics=False,
              custom_topic=None,
              custom_topic_mode="extended",
              intents=False,
              custom_intent=None,
              custom_intent_mode="extended",
              detect_entities=False,
              detect_language=None,
              diarize=False,
              diarize_model=None,
              dictation=False,
              encoding=None,
              filler_words=False,
              keyterm=None,
              keywords=None,
              language="en",
              measurements=False,
              model=None,
              multichannel=False,
              numerals=False,
              paragraphs=False,
              profanity_filter=False,
              punctuate=False,
              redact=None,
              replace=None,
              search=None,
              smart_format=False,
              utterances=False,
              utt_split=0.8,
              version=None,
              mip_opt_out=False,
              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `callback` | `str` | Query, Optional | URL to which we'll make the callback request |
| `callback_method` | [`V1ListenPostParametersCallbackMethod`](../../doc/models/v1-listen-post-parameters-callback-method.md) | Query, Optional | HTTP method by which the callback request will be made<br><br>**Default**: `"POST"` |
| `extra` | str \| List[str] \| None | Query, Optional | Arbitrary key-value pairs that are attached to the API response for usage in downstream processing |
| `sentiment` | `bool` | Query, Optional | Recognizes the sentiment throughout a transcript or text<br><br>**Default**: `False` |
| `summarize` | [V1ListenPostParametersSummarize0](../../doc/models/v1-listen-post-parameters-summarize-0.md) \| bool \| None | Query, Optional | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only. |
| `tag` | str \| List[str] \| None | Query, Optional | Label your requests for the purpose of identification during usage reporting |
| `topics` | `bool` | Query, Optional | Detect topics throughout a transcript or text<br><br>**Default**: `False` |
| `custom_topic` | str \| List[str] \| None | Query, Optional | Custom topics you want the model to detect within your input audio or text if present Submit up to `100`. |
| `custom_topic_mode` | [`V1ListenPostParametersCustomTopicMode`](../../doc/models/v1-listen-post-parameters-custom-topic-mode.md) | Query, Optional | Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param<br><br>**Default**: `"extended"` |
| `intents` | `bool` | Query, Optional | Recognizes speaker intent throughout a transcript or text<br><br>**Default**: `False` |
| `custom_intent` | str \| List[str] \| None | Query, Optional | Custom intents you want the model to detect within your input audio if present |
| `custom_intent_mode` | [`V1ListenPostParametersCustomTopicMode`](../../doc/models/v1-listen-post-parameters-custom-topic-mode.md) | Query, Optional | Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.<br><br>**Default**: `"extended"` |
| `detect_entities` | `bool` | Query, Optional | Identifies and extracts key entities from content in submitted audio<br><br>**Default**: `False` |
| `detect_language` | bool \| List[str] \| None | Query, Optional | Identifies the dominant language spoken in submitted audio |
| `diarize` | `bool` | Query, Optional | Deprecated: use `diarize_model` instead. Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0.<br><br>**Default**: `False` |
| `diarize_model` | [`V1ListenPostParametersDiarizeModel`](../../doc/models/v1-listen-post-parameters-diarize-model.md) | Query, Optional | Select and enable a specific diarization model version. Specifying this parameter enables diarization and selects the model — you do not need to also set the deprecated `diarize=true` parameter. For batch, supported values are `latest` (currently v2), `v1`, and `v2`. For streaming, supported values are `latest` (currently v1) and `v1`; `v2` returns a validation error on streaming requests. |
| `dictation` | `bool` | Query, Optional | Dictation mode for controlling formatting with dictated speech<br><br>**Default**: `False` |
| `encoding` | [`V1ListenPostParametersEncoding`](../../doc/models/v1-listen-post-parameters-encoding.md) | Query, Optional | Specify the expected encoding of your submitted audio |
| `filler_words` | `bool` | Query, Optional | Filler Words can help transcribe interruptions in your audio, like "uh" and "um"<br><br>**Default**: `False` |
| `keyterm` | `List[str]` | Query, Optional | Key term prompting improves recognition of specialized terminology and brands. Only compatible with Nova-3.<br><br>`keyterm` accepts plain terms only. Unlike the legacy `keywords` feature, it does not support weights or intensifiers. Appending one (for example, `keyterm=term:0.15`) is not rejected—the weight is silently ignored and the entire value is treated as a literal keyterm.<br><br>To boost multiple separate keyterms, repeat the `keyterm` parameter (for example, `keyterm=term1&keyterm=term2`). To boost one multi-word phrase as a single keyterm, join the words with `%20` or `+` (for example, `keyterm=customer%20service`). Do not separate keyterms with commas, semicolons, or line breaks. |
| `keywords` | str \| List[str] \| None | Query, Optional | Keywords can boost or suppress specialized terminology and brands |
| `language` | `str` | Query, Optional | The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available<br><br>**Default**: `"en"` |
| `measurements` | `bool` | Query, Optional | Spoken measurements will be converted to their corresponding abbreviations<br><br>**Default**: `False` |
| `model` | [V1ListenPostParametersModel0](../../doc/models/v1-listen-post-parameters-model-0.md) \| str \| None | Query, Optional | This is a container for one-of cases. |
| `multichannel` | `bool` | Query, Optional | Transcribe each audio channel independently<br><br>**Default**: `False` |
| `numerals` | `bool` | Query, Optional | Numerals converts numbers from written format to numerical format<br><br>**Default**: `False` |
| `paragraphs` | `bool` | Query, Optional | Splits audio into paragraphs to improve transcript readability<br><br>**Default**: `False` |
| `profanity_filter` | `bool` | Query, Optional | Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely<br><br>**Default**: `False` |
| `punctuate` | `bool` | Query, Optional | Add punctuation and capitalization to the transcript<br><br>**Default**: `False` |
| `redact` | str \| List[[V1ListenPostParametersRedactSchemaOneOf1Items](../../doc/models/v1-listen-post-parameters-redact-schema-one-of-1-items.md)] \| None | Query, Optional | This is a container for one-of cases. |
| `replace` | str \| List[str] \| None | Query, Optional | Search for terms or phrases in submitted audio and replaces them |
| `search` | str \| List[str] \| None | Query, Optional | Search for terms or phrases in submitted audio |
| `smart_format` | `bool` | Query, Optional | Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability<br><br>**Default**: `False` |
| `utterances` | `bool` | Query, Optional | Segments speech into meaningful semantic units<br><br>**Default**: `False` |
| `utt_split` | `float` | Query, Optional | Seconds to wait before detecting a pause between words in submitted audio<br><br>**Default**: `0.8` |
| `version` | [V1ListenPostParametersVersion0](../../doc/models/v1-listen-post-parameters-version-0.md) \| str \| None | Query, Optional | This is a container for one-of cases. |
| `mip_opt_out` | `bool` | Query, Optional | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br><br>**Default**: `False` |
| `body` | [`ListenV1RequestUrl`](../../doc/models/listen-v1-request-url.md) | Body, Optional | Transcribe an audio or video file |

## Response Type

**200**: Returns either transcription results, or a request_id when using a callback.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `ListenV1Response | ListenV1AcceptedResponse`.

## Example Usage

```python
authorization = 'Authorization8'

callback_method = V1ListenPostParametersCallbackMethod.POST

sentiment = False

summarize = False

topics = False

custom_topic_mode = V1ListenPostParametersCustomTopicMode.EXTENDED

intents = False

custom_intent_mode = V1ListenPostParametersCustomTopicMode.EXTENDED

detect_entities = False

detect_language = False

diarize = False

dictation = False

filler_words = False

language = 'en'

measurements = False

multichannel = False

numerals = False

paragraphs = False

profanity_filter = False

punctuate = False

smart_format = False

utterances = False

utt_split = 0.8

mip_opt_out = False

result = listen_v_1_media_api.transcribe(
    authorization,
    callback_method=callback_method,
    sentiment=sentiment,
    summarize=summarize,
    topics=topics,
    custom_topic_mode=custom_topic_mode,
    intents=intents,
    custom_intent_mode=custom_intent_mode,
    detect_entities=detect_entities,
    detect_language=detect_language,
    diarize=diarize,
    dictation=dictation,
    filler_words=filler_words,
    language=language,
    measurements=measurements,
    multichannel=multichannel,
    numerals=numerals,
    paragraphs=paragraphs,
    profanity_filter=profanity_filter,
    punctuate=punctuate,
    smart_format=smart_format,
    utterances=utterances,
    utt_split=utt_split,
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
| 400 | Invalid Request | [`ListenV1ResponseErrorException`](../../doc/models/listen-v1-response-error-exception.md) |

