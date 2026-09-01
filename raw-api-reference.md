# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [DeepgramClient](deepgram/client.py)

## AgentV1SettingsThinkModels

> Source: [AgentV1SettingsThinkModels](deepgram/apis/agent_v1_settings_think_models.py)

<details>
<summary><code>def list_(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentThinkModelsV1Response, ListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the available think models that can be used for AI agent processing

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.agent_v1_settings_think_models.with_raw_response.list_()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentThinkModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListErrorBody
```

**Async**

```python
result = await async_client.agent_v1_settings_think_models.with_raw_response.list_()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentThinkModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentThinkModelsV1Response](deepgram/models/agent_think_models_v1_response.py), [ListErrorBody](deepgram/errors/list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentThinkModelsV1Response](deepgram/models/agent_think_models_v1_response.py)</code> -- List of available think models

**On `Failure`**: `error` is <code>[ListErrorBody](deepgram/errors/list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AuthV1Tokens

> Source: [AuthV1Tokens](deepgram/apis/auth_v1_tokens.py)

<details>
<summary><code>def grant(*, body: GrantV1Request | GrantV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GrantV1Response, GrantErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint will not work with the Manage APIs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.auth_v1_tokens.with_raw_response.grant()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GrantV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GrantErrorBody
```

**Async**

```python
result = await async_client.auth_v1_tokens.with_raw_response.grant()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GrantV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GrantErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GrantV1Request](deepgram/models/grant_v1_request.py) \| [GrantV1RequestDict](deepgram/models/grant_v1_request.py) \| None</code> | Time to live settings<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GrantV1Response](deepgram/models/grant_v1_response.py), [GrantErrorBody](deepgram/errors/grant_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GrantV1Response](deepgram/models/grant_v1_response.py)</code> -- Grant response

**On `Failure`**: `error` is <code>[GrantErrorBody](deepgram/errors/grant_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ListenV1Media

> Source: [ListenV1Media](deepgram/apis/listen_v1_media.py)

<details>
<summary><code>def transcribe(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None, sentiment: bool | None = False, summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None, tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None, topics: bool | None = False, custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None, custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, intents: bool | None = False, custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None, custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, detect_entities: bool | None = False, detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None, diarize: bool | None = False, diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None, dictation: bool | None = False, encoding: V1ListenPostParametersEncodingOrStr | None = None, filler_words: bool | None = False, keyterm: list[str] | None = None, keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None, language: str | None = "en", measurements: bool | None = False, model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None, multichannel: bool | None = False, numerals: bool | None = False, paragraphs: bool | None = False, profanity_filter: bool | None = False, punctuate: bool | None = False, redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None, replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None, search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None, smart_format: bool | None = False, utterances: bool | None = False, utt_split: float | None = 0.8, version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None, mip_opt_out: bool | None = False, body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListenV1MediaTranscribeResponse200, TranscribeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transcribe audio and video using Deepgram's speech-to-text REST API

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.listen_v1_media.with_raw_response.transcribe()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListenV1MediaTranscribeResponse200
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TranscribeErrorBody
```

**Async**

```python
result = await async_client.listen_v1_media.with_raw_response.transcribe()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListenV1MediaTranscribeResponse200
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type TranscribeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>callback</code> | <code>str \| None</code> | URL to which we'll make the callback request<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>[V1ListenPostParametersCallbackMethodOrStr](deepgram/models/enums/v1_listen_post_parameters_callback_method.py) \| None</code> | HTTP method by which the callback request will be made<br>**Default**: <code>None</code> |
| <code>extra</code> | <code>[V1ListenPostParametersExtra](deepgram/models/unions/v1_listen_post_parameters_extra.py) \| [V1ListenPostParametersExtraDict](deepgram/models/unions/v1_listen_post_parameters_extra.py) \| None</code> | Arbitrary key-value pairs that are attached to the API response for usage in downstream processing<br>**Default**: <code>None</code> |
| <code>sentiment</code> | <code>bool \| None</code> | Recognizes the sentiment throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>summarize</code> | <code>[V1ListenPostParametersSummarize](deepgram/models/unions/v1_listen_post_parameters_summarize.py) \| [V1ListenPostParametersSummarizeDict](deepgram/models/unions/v1_listen_post_parameters_summarize.py) \| None</code> | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only.<br>**Default**: <code>None</code> |
| <code>tag</code> | <code>[V1ListenPostParametersTag](deepgram/models/unions/v1_listen_post_parameters_tag.py) \| [V1ListenPostParametersTagDict](deepgram/models/unions/v1_listen_post_parameters_tag.py) \| None</code> | Label your requests for the purpose of identification during usage reporting<br>**Default**: <code>None</code> |
| <code>topics</code> | <code>bool \| None</code> | Detect topics throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>custom_topic</code> | <code>[V1ListenPostParametersCustomTopic](deepgram/models/unions/v1_listen_post_parameters_custom_topic.py) \| [V1ListenPostParametersCustomTopicDict](deepgram/models/unions/v1_listen_post_parameters_custom_topic.py) \| None</code> | Custom topics you want the model to detect within your input audio or text if present Submit up to `100`.<br>**Default**: <code>None</code> |
| <code>custom_topic_mode</code> | <code>[V1ListenPostParametersCustomTopicModeOrStr](deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py) \| None</code> | Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param<br>**Default**: <code>None</code> |
| <code>intents</code> | <code>bool \| None</code> | Recognizes speaker intent throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>custom_intent</code> | <code>[V1ListenPostParametersCustomIntent](deepgram/models/unions/v1_listen_post_parameters_custom_intent.py) \| [V1ListenPostParametersCustomIntentDict](deepgram/models/unions/v1_listen_post_parameters_custom_intent.py) \| None</code> | Custom intents you want the model to detect within your input audio if present<br>**Default**: <code>None</code> |
| <code>custom_intent_mode</code> | <code>[V1ListenPostParametersCustomTopicModeOrStr](deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py) \| None</code> | Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.<br>**Default**: <code>None</code> |
| <code>detect_entities</code> | <code>bool \| None</code> | Identifies and extracts key entities from content in submitted audio<br>**Default**: <code>False</code> |
| <code>detect_language</code> | <code>[V1ListenPostParametersDetectLanguage](deepgram/models/unions/v1_listen_post_parameters_detect_language.py) \| [V1ListenPostParametersDetectLanguageDict](deepgram/models/unions/v1_listen_post_parameters_detect_language.py) \| None</code> | Identifies the dominant language spoken in submitted audio<br>**Default**: <code>None</code> |
| <code>diarize</code> | <code>bool \| None</code> | Deprecated: use `diarize_model` instead. Recognize speaker changes. Each word in the transcript will be assigned a speaker number starting at 0.<br>**Default**: <code>False</code> |
| <code>diarize_model</code> | <code>[V1ListenPostParametersDiarizeModelOrStr](deepgram/models/enums/v1_listen_post_parameters_diarize_model.py) \| None</code> | Select and enable a specific diarization model version. Specifying this parameter enables diarization and selects the model — you do not need to also set the deprecated `diarize=true` parameter. For batch, supported values are `latest` (currently v2), `v1`, and `v2`. For streaming, supported values are `latest` (currently v1) and `v1`; `v2` returns a validation error on streaming requests.<br>**Default**: <code>None</code> |
| <code>dictation</code> | <code>bool \| None</code> | Dictation mode for controlling formatting with dictated speech<br>**Default**: <code>False</code> |
| <code>encoding</code> | <code>[V1ListenPostParametersEncodingOrStr](deepgram/models/enums/v1_listen_post_parameters_encoding.py) \| None</code> | Specify the expected encoding of your submitted audio<br>**Default**: <code>None</code> |
| <code>filler_words</code> | <code>bool \| None</code> | Filler Words can help transcribe interruptions in your audio, like "uh" and "um"<br>**Default**: <code>False</code> |
| <code>keyterm</code> | <code>list&#91;str&#93; \| None</code> | Key term prompting improves recognition of specialized terminology and brands. Only compatible with Nova-3.<br><br>`keyterm` accepts plain terms only. Unlike the legacy `keywords` feature, it does not support weights or intensifiers. Appending one (for example, `keyterm=term:0.15`) is not rejected—the weight is silently ignored and the entire value is treated as a literal keyterm.<br><br>To boost multiple separate keyterms, repeat the `keyterm` parameter (for example, `keyterm=term1&keyterm=term2`). To boost one multi-word phrase as a single keyterm, join the words with `%20` or `+` (for example, `keyterm=customer%20service`). Do not separate keyterms with commas, semicolons, or line breaks.<br>**Default**: <code>None</code> |
| <code>keywords</code> | <code>[V1ListenPostParametersKeywords](deepgram/models/unions/v1_listen_post_parameters_keywords.py) \| [V1ListenPostParametersKeywordsDict](deepgram/models/unions/v1_listen_post_parameters_keywords.py) \| None</code> | Keywords can boost or suppress specialized terminology and brands<br>**Default**: <code>None</code> |
| <code>language</code> | <code>str \| None</code> | The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available<br>**Default**: <code>"en"</code> |
| <code>measurements</code> | <code>bool \| None</code> | Spoken measurements will be converted to their corresponding abbreviations<br>**Default**: <code>False</code> |
| <code>model</code> | <code>[V1ListenPostParametersModel](deepgram/models/unions/v1_listen_post_parameters_model.py) \| [V1ListenPostParametersModelDict](deepgram/models/unions/v1_listen_post_parameters_model.py) \| None</code> | AI model used to process submitted audio<br>**Default**: <code>None</code> |
| <code>multichannel</code> | <code>bool \| None</code> | Transcribe each audio channel independently<br>**Default**: <code>False</code> |
| <code>numerals</code> | <code>bool \| None</code> | Numerals converts numbers from written format to numerical format<br>**Default**: <code>False</code> |
| <code>paragraphs</code> | <code>bool \| None</code> | Splits audio into paragraphs to improve transcript readability<br>**Default**: <code>False</code> |
| <code>profanity_filter</code> | <code>bool \| None</code> | Profanity Filter looks for recognized profanity and converts it to the nearest recognized non-profane word or removes it from the transcript completely<br>**Default**: <code>False</code> |
| <code>punctuate</code> | <code>bool \| None</code> | Add punctuation and capitalization to the transcript<br>**Default**: <code>False</code> |
| <code>redact</code> | <code>[V1ListenPostParametersRedact](deepgram/models/unions/v1_listen_post_parameters_redact.py) \| [V1ListenPostParametersRedactDict](deepgram/models/unions/v1_listen_post_parameters_redact.py) \| None</code> | Redaction removes sensitive information from your transcripts<br>**Default**: <code>None</code> |
| <code>replace</code> | <code>[V1ListenPostParametersReplace](deepgram/models/unions/v1_listen_post_parameters_replace.py) \| [V1ListenPostParametersReplaceDict](deepgram/models/unions/v1_listen_post_parameters_replace.py) \| None</code> | Search for terms or phrases in submitted audio and replaces them<br>**Default**: <code>None</code> |
| <code>search</code> | <code>[V1ListenPostParametersSearch](deepgram/models/unions/v1_listen_post_parameters_search.py) \| [V1ListenPostParametersSearchDict](deepgram/models/unions/v1_listen_post_parameters_search.py) \| None</code> | Search for terms or phrases in submitted audio<br>**Default**: <code>None</code> |
| <code>smart_format</code> | <code>bool \| None</code> | Apply formatting to transcript output. When set to true, additional formatting will be applied to transcripts to improve readability<br>**Default**: <code>False</code> |
| <code>utterances</code> | <code>bool \| None</code> | Segments speech into meaningful semantic units<br>**Default**: <code>False</code> |
| <code>utt_split</code> | <code>float \| None</code> | Seconds to wait before detecting a pause between words in submitted audio<br>**Default**: <code>0.8</code> |
| <code>version</code> | <code>[V1ListenPostParametersVersion](deepgram/models/unions/v1_listen_post_parameters_version.py) \| [V1ListenPostParametersVersionDict](deepgram/models/unions/v1_listen_post_parameters_version.py) \| None</code> | Version of an AI model to use<br>**Default**: <code>None</code> |
| <code>mip_opt_out</code> | <code>bool \| None</code> | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br>**Default**: <code>False</code> |
| <code>body</code> | <code>[ListenV1RequestUrl](deepgram/models/listen_v1_request_url.py) \| [ListenV1RequestUrlDict](deepgram/models/listen_v1_request_url.py) \| None</code> | Transcribe an audio or video file<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListenV1MediaTranscribeResponse200](deepgram/models/unions/listen_v1_media_transcribe_response200.py), [TranscribeErrorBody](deepgram/errors/transcribe_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListenV1MediaTranscribeResponse200](deepgram/models/unions/listen_v1_media_transcribe_response200.py)</code> -- Returns either transcription results, or a request_id when using a callback.

**On `Failure`**: `error` is <code>[TranscribeErrorBody](deepgram/errors/transcribe_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ListenV1Response](deepgram/models/listen_v1_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1Models

> Source: [ManageV1Models](deepgram/apis/manage_v1_models.py)

<details>
<summary><code>def get5(model_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetModelV1Response, Get5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns metadata for a specific public model

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_models.with_raw_response.get5(model_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetModelV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get5ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_models.with_raw_response.get5(model_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetModelV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>model_id</code> | <code>str</code> | The specific UUID of the model |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetModelV1Response](deepgram/models/unions/get_model_v1_response.py), [Get5ErrorBody](deepgram/errors/get5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetModelV1Response](deepgram/models/unions/get_model_v1_response.py)</code> -- A model object that can be either STT or TTS

**On `Failure`**: `error` is <code>[Get5ErrorBody](deepgram/errors/get5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list6(*, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListModelsV1Response, List6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_models.with_raw_response.list6()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List6ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_models.with_raw_response.list6()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_outdated</code> | <code>bool \| None</code> | returns non-latest versions of models<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListModelsV1Response](deepgram/models/list_models_v1_response.py), [List6ErrorBody](deepgram/errors/list6_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListModelsV1Response](deepgram/models/list_models_v1_response.py)</code> -- A list of models

**On `Failure`**: `error` is <code>[List6ErrorBody](deepgram/errors/list6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1Projects

> Source: [ManageV1Projects](deepgram/apis/manage_v1_projects.py)

<details>
<summary><code>def delete3(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteProjectV1Response, Delete3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects.with_raw_response.delete3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete3ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects.with_raw_response.delete3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[DeleteProjectV1Response](deepgram/models/delete_project_v1_response.py), [Delete3ErrorBody](deepgram/errors/delete3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteProjectV1Response](deepgram/models/delete_project_v1_response.py)</code> -- A project

**On `Failure`**: `error` is <code>[Delete3ErrorBody](deepgram/errors/delete3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get3(project_id: str, *, limit: float | None = 10.0, page: float | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectV1Response, Get3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves information about the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects.with_raw_response.get3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get3ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects.with_raw_response.get3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>limit</code> | <code>float \| None</code> | Number of results to return per page. Default 10. Range [1,1000]<br>**Default**: <code>10.0</code> |
| <code>page</code> | <code>float \| None</code> | Navigate and return the results to retrieve specific portions of information of the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectV1Response](deepgram/models/get_project_v1_response.py), [Get3ErrorBody](deepgram/errors/get3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectV1Response](deepgram/models/get_project_v1_response.py)</code> -- A project

**On `Failure`**: `error` is <code>[Get3ErrorBody](deepgram/errors/get3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def leave(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LeaveProjectV1Response, LeaveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes the authenticated account from the specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects.with_raw_response.leave(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LeaveProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LeaveErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects.with_raw_response.leave(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LeaveProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type LeaveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[LeaveProjectV1Response](deepgram/models/leave_project_v1_response.py), [LeaveErrorBody](deepgram/errors/leave_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LeaveProjectV1Response](deepgram/models/leave_project_v1_response.py)</code> -- Successfully removed account from project

**On `Failure`**: `error` is <code>[LeaveErrorBody](deepgram/errors/leave_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list4(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectsV1Response, List4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves basic information about the projects associated with the API key

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects.with_raw_response.list4()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List4ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects.with_raw_response.list4()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectsV1Response](deepgram/models/list_projects_v1_response.py), [List4ErrorBody](deepgram/errors/list4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectsV1Response](deepgram/models/list_projects_v1_response.py)</code> -- A list of projects

**On `Failure`**: `error` is <code>[List4ErrorBody](deepgram/errors/list4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update3(project_id: str, *, body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateProjectV1Response, Update3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the name or other properties of an existing project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects.with_raw_response.update3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update3ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects.with_raw_response.update3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateProjectV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>body</code> | <code>[UpdateProjectV1Request](deepgram/models/update_project_v1_request.py) \| [UpdateProjectV1RequestDict](deepgram/models/update_project_v1_request.py) \| None</code> | The name of the project<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[UpdateProjectV1Response](deepgram/models/update_project_v1_response.py), [Update3ErrorBody](deepgram/errors/update3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateProjectV1Response](deepgram/models/update_project_v1_response.py)</code> -- A project

**On `Failure`**: `error` is <code>[Update3ErrorBody](deepgram/errors/update3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsBillingBalances

> Source: [ManageV1ProjectsBillingBalances](deepgram/apis/manage_v1_projects_billing_balances.py)

<details>
<summary><code>def get10(project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectBalanceV1Response, Get10ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details about the specified balance

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_billing_balances.with_raw_response.get10(project_id, balance_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectBalanceV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get10ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_billing_balances.with_raw_response.get10(project_id, balance_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectBalanceV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get10ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>balance_id</code> | <code>str</code> | The unique identifier of the balance |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectBalanceV1Response](deepgram/models/get_project_balance_v1_response.py), [Get10ErrorBody](deepgram/errors/get10_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectBalanceV1Response](deepgram/models/get_project_balance_v1_response.py)</code> -- A specific balance

**On `Failure`**: `error` is <code>[Get10ErrorBody](deepgram/errors/get10_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list13(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectBalancesV1Response, List13ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates a list of outstanding balances for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_billing_balances.with_raw_response.list13(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectBalancesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List13ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_billing_balances.with_raw_response.list13(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectBalancesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List13ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectBalancesV1Response](deepgram/models/list_project_balances_v1_response.py), [List13ErrorBody](deepgram/errors/list13_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectBalancesV1Response](deepgram/models/list_project_balances_v1_response.py)</code> -- A list of outstanding balances

**On `Failure`**: `error` is <code>[List13ErrorBody](deepgram/errors/list13_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsBillingBreakdown

> Source: [ManageV1ProjectsBillingBreakdown](deepgram/apis/manage_v1_projects_billing_breakdown.py)

<details>
<summary><code>def list14(project_id: str, *, start: Date | None = None, end: Date | None = None, accessor: str | None = None, deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None, tag: str | None = None, line_item: str | None = None, grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BillingBreakdownV1Response, List14ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the billing summary for a specific project, with various filter options or by grouping options.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_billing_breakdown.with_raw_response.list14(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BillingBreakdownV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List14ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_billing_breakdown.with_raw_response.list14(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BillingBreakdownV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List14ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>Date \| None</code> | Start date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>end</code> | <code>Date \| None</code> | End date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>accessor</code> | <code>str \| None</code> | Filter for requests where a specific accessor was used<br>**Default**: <code>None</code> |
| <code>deployment</code> | <code>[V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr](deepgram/models/enums/v1_projects_project_id_billing_breakdown_get_parameters_deployment.py) \| None</code> | Filter for requests where a specific deployment was used<br>**Default**: <code>None</code> |
| <code>tag</code> | <code>str \| None</code> | Filter for requests where a specific tag was used<br>**Default**: <code>None</code> |
| <code>line_item</code> | <code>str \| None</code> | Filter requests by line item (e.g. streaming::nova-3)<br>**Default**: <code>None</code> |
| <code>grouping</code> | <code>list&#91;[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr](deepgram/models/enums/v1_projects_project_id_billing_breakdown_get_parameters_grouping_schema_items.py)&#93; \| None</code> | Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[BillingBreakdownV1Response](deepgram/models/billing_breakdown_v1_response.py), [List14ErrorBody](deepgram/errors/list14_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BillingBreakdownV1Response](deepgram/models/billing_breakdown_v1_response.py)</code> -- Billing breakdown response

**On `Failure`**: `error` is <code>[List14ErrorBody](deepgram/errors/list14_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsBillingFields

> Source: [ManageV1ProjectsBillingFields](deepgram/apis/manage_v1_projects_billing_fields.py)

<details>
<summary><code>def list15(project_id: str, *, start: Date | None = None, end: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBillingFieldsV1Response, List15ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the accessors, deployment types, tags, and line items used for billing data in the specified time period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to know what filters are available.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_billing_fields.with_raw_response.list15(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBillingFieldsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List15ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_billing_fields.with_raw_response.list15(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBillingFieldsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List15ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>Date \| None</code> | Start date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>end</code> | <code>Date \| None</code> | End date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListBillingFieldsV1Response](deepgram/models/list_billing_fields_v1_response.py), [List15ErrorBody](deepgram/errors/list15_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBillingFieldsV1Response](deepgram/models/list_billing_fields_v1_response.py)</code> -- A list of billing fields for a specific project

**On `Failure`**: `error` is <code>[List15ErrorBody](deepgram/errors/list15_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsBillingPurchases

> Source: [ManageV1ProjectsBillingPurchases](deepgram/apis/manage_v1_projects_billing_purchases.py)

<details>
<summary><code>def list16(project_id: str, *, limit: float | None = 10.0, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectPurchasesV1Response, List16ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the original purchased amount on an order transaction

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_billing_purchases.with_raw_response.list16(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectPurchasesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List16ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_billing_purchases.with_raw_response.list16(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectPurchasesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List16ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>limit</code> | <code>float \| None</code> | Number of results to return per page. Default 10. Range [1,1000]<br>**Default**: <code>10.0</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectPurchasesV1Response](deepgram/models/list_project_purchases_v1_response.py), [List16ErrorBody](deepgram/errors/list16_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectPurchasesV1Response](deepgram/models/list_project_purchases_v1_response.py)</code> -- A list of purchases for a specific project

**On `Failure`**: `error` is <code>[List16ErrorBody](deepgram/errors/list16_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsKeys

> Source: [ManageV1ProjectsKeys](deepgram/apis/manage_v1_projects_keys.py)

<details>
<summary><code>def create3(project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateKeyV1Response, Create3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new API key with specified settings for the project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_keys.with_raw_response.create3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create3ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_keys.with_raw_response.create3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>body</code> | <code>Any \| None</code> | API key settings<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[CreateKeyV1Response](deepgram/models/create_key_v1_response.py), [Create3ErrorBody](deepgram/errors/create3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateKeyV1Response](deepgram/models/create_key_v1_response.py)</code> -- API key created successfully

**On `Failure`**: `error` is <code>[Create3ErrorBody](deepgram/errors/create3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete4(project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteProjectKeyV1Response, Delete4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an API key for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_keys.with_raw_response.delete4(project_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete4ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_keys.with_raw_response.delete4(project_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>key_id</code> | <code>str</code> | The unique identifier of the API key |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[DeleteProjectKeyV1Response](deepgram/models/delete_project_key_v1_response.py), [Delete4ErrorBody](deepgram/errors/delete4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteProjectKeyV1Response](deepgram/models/delete_project_key_v1_response.py)</code> -- API key deleted

**On `Failure`**: `error` is <code>[Delete4ErrorBody](deepgram/errors/delete4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get6(project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectKeyV1Response, Get6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves information about a specified API key

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_keys.with_raw_response.get6(project_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get6ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_keys.with_raw_response.get6(project_id, key_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectKeyV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>key_id</code> | <code>str</code> | The unique identifier of the API key |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectKeyV1Response](deepgram/models/get_project_key_v1_response.py), [Get6ErrorBody](deepgram/errors/get6_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectKeyV1Response](deepgram/models/get_project_key_v1_response.py)</code> -- A specific API key

**On `Failure`**: `error` is <code>[Get6ErrorBody](deepgram/errors/get6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list7(project_id: str, *, status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectKeysV1Response, List7ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all API keys associated with the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_keys.with_raw_response.list7(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectKeysV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List7ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_keys.with_raw_response.list7(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectKeysV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List7ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>status</code> | <code>[V1ProjectsProjectIdKeysGetParametersStatusOrStr](deepgram/models/enums/v1_projects_project_id_keys_get_parameters_status.py) \| None</code> | Only return keys with a specific status<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectKeysV1Response](deepgram/models/list_project_keys_v1_response.py), [List7ErrorBody](deepgram/errors/list7_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectKeysV1Response](deepgram/models/list_project_keys_v1_response.py)</code> -- A list of API keys

**On `Failure`**: `error` is <code>[List7ErrorBody](deepgram/errors/list7_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsMembers

> Source: [ManageV1ProjectsMembers](deepgram/apis/manage_v1_projects_members.py)

<details>
<summary><code>def delete5(project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteProjectMemberV1Response, Delete5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a member from the project using their unique member ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members.with_raw_response.delete5(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectMemberV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete5ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members.with_raw_response.delete5(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectMemberV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>member_id</code> | <code>str</code> | The unique identifier of the Member |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[DeleteProjectMemberV1Response](deepgram/models/delete_project_member_v1_response.py), [Delete5ErrorBody](deepgram/errors/delete5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteProjectMemberV1Response](deepgram/models/delete_project_member_v1_response.py)</code> -- Delete the specific member from the project

**On `Failure`**: `error` is <code>[Delete5ErrorBody](deepgram/errors/delete5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list8(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectMembersV1Response, List8ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of members for a given project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members.with_raw_response.list8(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectMembersV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List8ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members.with_raw_response.list8(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectMembersV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List8ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectMembersV1Response](deepgram/models/list_project_members_v1_response.py), [List8ErrorBody](deepgram/errors/list8_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectMembersV1Response](deepgram/models/list_project_members_v1_response.py)</code> -- A list of members for a given project

**On `Failure`**: `error` is <code>[List8ErrorBody](deepgram/errors/list8_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsMembersInvites

> Source: [ManageV1ProjectsMembersInvites](deepgram/apis/manage_v1_projects_members_invites.py)

<details>
<summary><code>def create4(project_id: str, *, body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateProjectInviteV1Response, Create4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates an invite for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members_invites.with_raw_response.create4(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateProjectInviteV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create4ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members_invites.with_raw_response.create4(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateProjectInviteV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>body</code> | <code>[CreateProjectInviteV1Request](deepgram/models/create_project_invite_v1_request.py) \| [CreateProjectInviteV1RequestDict](deepgram/models/create_project_invite_v1_request.py) \| None</code> | email to invite to the project<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[CreateProjectInviteV1Response](deepgram/models/create_project_invite_v1_response.py), [Create4ErrorBody](deepgram/errors/create4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateProjectInviteV1Response](deepgram/models/create_project_invite_v1_response.py)</code> -- The invite was successfully generated

**On `Failure`**: `error` is <code>[Create4ErrorBody](deepgram/errors/create4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete6(project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteProjectInviteV1Response, Delete6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an invite for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members_invites.with_raw_response.delete6(project_id, email)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectInviteV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete6ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members_invites.with_raw_response.delete6(project_id, email)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteProjectInviteV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>email</code> | <code>str</code> | The email address of the member |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[DeleteProjectInviteV1Response](deepgram/models/delete_project_invite_v1_response.py), [Delete6ErrorBody](deepgram/errors/delete6_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteProjectInviteV1Response](deepgram/models/delete_project_invite_v1_response.py)</code> -- The invite was successfully deleted

**On `Failure`**: `error` is <code>[Delete6ErrorBody](deepgram/errors/delete6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list10(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectInvitesV1Response, List10ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates a list of invites for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members_invites.with_raw_response.list10(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectInvitesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List10ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members_invites.with_raw_response.list10(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectInvitesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List10ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectInvitesV1Response](deepgram/models/list_project_invites_v1_response.py), [List10ErrorBody](deepgram/errors/list10_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectInvitesV1Response](deepgram/models/list_project_invites_v1_response.py)</code> -- A list of invites for a specific project

**On `Failure`**: `error` is <code>[List10ErrorBody](deepgram/errors/list10_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsMembersScopes

> Source: [ManageV1ProjectsMembersScopes](deepgram/apis/manage_v1_projects_members_scopes.py)

<details>
<summary><code>def list9(project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectMemberScopesV1Response, List9ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of scopes for a specific member

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members_scopes.with_raw_response.list9(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectMemberScopesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List9ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members_scopes.with_raw_response.list9(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectMemberScopesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List9ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>member_id</code> | <code>str</code> | The unique identifier of the Member |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectMemberScopesV1Response](deepgram/models/list_project_member_scopes_v1_response.py), [List9ErrorBody](deepgram/errors/list9_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectMemberScopesV1Response](deepgram/models/list_project_member_scopes_v1_response.py)</code> -- A list of scopes for a specific member

**On `Failure`**: `error` is <code>[List9ErrorBody](deepgram/errors/list9_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update4(project_id: str, member_id: str, *, body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateProjectMemberScopesV1Response, Update4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the scopes for a specific member

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_members_scopes.with_raw_response.update4(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateProjectMemberScopesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update4ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_members_scopes.with_raw_response.update4(project_id, member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateProjectMemberScopesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>member_id</code> | <code>str</code> | The unique identifier of the Member |
| <code>body</code> | <code>[UpdateProjectMemberScopesV1Request](deepgram/models/update_project_member_scopes_v1_request.py) \| [UpdateProjectMemberScopesV1RequestDict](deepgram/models/update_project_member_scopes_v1_request.py) \| None</code> | A scope to update<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[UpdateProjectMemberScopesV1Response](deepgram/models/update_project_member_scopes_v1_response.py), [Update4ErrorBody](deepgram/errors/update4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateProjectMemberScopesV1Response](deepgram/models/update_project_member_scopes_v1_response.py)</code> -- Updated the scopes for a specific member

**On `Failure`**: `error` is <code>[Update4ErrorBody](deepgram/errors/update4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsModels

> Source: [ManageV1ProjectsModels](deepgram/apis/manage_v1_projects_models.py)

<details>
<summary><code>def get4(project_id: str, model_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetModelV1Response, Get4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns metadata for a specific model

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_models.with_raw_response.get4(project_id, model_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetModelV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get4ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_models.with_raw_response.get4(project_id, model_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetModelV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>model_id</code> | <code>str</code> | The specific UUID of the model |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetModelV1Response](deepgram/models/unions/get_model_v1_response.py), [Get4ErrorBody](deepgram/errors/get4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetModelV1Response](deepgram/models/unions/get_model_v1_response.py)</code> -- A model object that can be either STT or TTS

**On `Failure`**: `error` is <code>[Get4ErrorBody](deepgram/errors/get4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list5(project_id: str, *, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListModelsV1Response, List5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns metadata on all the latest models that a specific project has access to, including non-public models

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_models.with_raw_response.list5(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List5ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_models.with_raw_response.list5(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListModelsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>include_outdated</code> | <code>bool \| None</code> | returns non-latest versions of models<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListModelsV1Response](deepgram/models/list_models_v1_response.py), [List5ErrorBody](deepgram/errors/list5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListModelsV1Response](deepgram/models/list_models_v1_response.py)</code> -- A list of models

**On `Failure`**: `error` is <code>[List5ErrorBody](deepgram/errors/list5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsRequests

> Source: [ManageV1ProjectsRequests](deepgram/apis/manage_v1_projects_requests.py)

<details>
<summary><code>def get7(project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectRequestV1Response, Get7ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific request for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_requests.with_raw_response.get7(project_id, request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectRequestV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get7ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_requests.with_raw_response.get7(project_id, request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectRequestV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get7ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_id</code> | <code>str</code> | The unique identifier of the request |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectRequestV1Response](deepgram/models/get_project_request_v1_response.py), [Get7ErrorBody](deepgram/errors/get7_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectRequestV1Response](deepgram/models/get_project_request_v1_response.py)</code> -- A specific request for a specific project

**On `Failure`**: `error` is <code>[Get7ErrorBody](deepgram/errors/get7_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list11(project_id: str, *, start: RFC3339DateTime | None = None, end: RFC3339DateTime | None = None, limit: float | None = 10.0, page: float | None = None, accessor: str | None = None, request_id: str | None = None, deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None, endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None, method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None, status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectRequestsV1Response, List11ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generates a list of requests for a specific project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_requests.with_raw_response.list11(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectRequestsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List11ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_requests.with_raw_response.list11(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectRequestsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List11ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>RFC3339DateTime \| None</code> | Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM<br>**Default**: <code>None</code> |
| <code>end</code> | <code>RFC3339DateTime \| None</code> | End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or YYYY-MM-DDTHH:MM:SS+HH:MM<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>float \| None</code> | Number of results to return per page. Default 10. Range [1,1000]<br>**Default**: <code>10.0</code> |
| <code>page</code> | <code>float \| None</code> | Navigate and return the results to retrieve specific portions of information of the response<br>**Default**: <code>None</code> |
| <code>accessor</code> | <code>str \| None</code> | Filter for requests where a specific accessor was used<br>**Default**: <code>None</code> |
| <code>request_id</code> | <code>str \| None</code> | Filter for a specific request id<br>**Default**: <code>None</code> |
| <code>deployment</code> | <code>[V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr](deepgram/models/enums/v1_projects_project_id_requests_get_parameters_deployment.py) \| None</code> | Filter for requests where a specific deployment was used<br>**Default**: <code>None</code> |
| <code>endpoint</code> | <code>[V1ProjectsProjectIdRequestsGetParametersEndpointOrStr](deepgram/models/enums/v1_projects_project_id_requests_get_parameters_endpoint.py) \| None</code> | Filter for requests where a specific endpoint was used<br>**Default**: <code>None</code> |
| <code>method</code> | <code>[V1ProjectsProjectIdRequestsGetParametersMethodOrStr](deepgram/models/enums/v1_projects_project_id_requests_get_parameters_method.py) \| None</code> | Filter for requests where a specific method was used<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[V1ProjectsProjectIdRequestsGetParametersStatusOrStr](deepgram/models/enums/v1_projects_project_id_requests_get_parameters_status.py) \| None</code> | Filter for requests that succeeded (status code < 300) or failed (status code >=400)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectRequestsV1Response](deepgram/models/list_project_requests_v1_response.py), [List11ErrorBody](deepgram/errors/list11_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectRequestsV1Response](deepgram/models/list_project_requests_v1_response.py)</code> -- A list of requests for a specific project

**On `Failure`**: `error` is <code>[List11ErrorBody](deepgram/errors/list11_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsUsage

> Source: [ManageV1ProjectsUsage](deepgram/apis/manage_v1_projects_usage.py)

<details>
<summary><code>def get8(project_id: str, *, start: Date | None = None, end: Date | None = None, accessor: str | None = None, alternatives: bool | None = None, callback_method: bool | None = None, callback: bool | None = None, channels: bool | None = None, custom_intent_mode: bool | None = None, custom_intent: bool | None = None, custom_topic_mode: bool | None = None, custom_topic: bool | None = None, deployment: V1ProjectsProjectIdUsageGetParametersDeploymentOrStr | None = None, detect_entities: bool | None = None, detect_language: bool | None = None, diarize: bool | None = None, dictation: bool | None = None, encoding: bool | None = None, endpoint: V1ProjectsProjectIdUsageGetParametersEndpointOrStr | None = None, extra: bool | None = None, filler_words: bool | None = None, intents: bool | None = None, keyterm: bool | None = None, keywords: bool | None = None, language: bool | None = None, measurements: bool | None = None, method: V1ProjectsProjectIdUsageGetParametersMethodOrStr | None = None, model: str | None = None, multichannel: bool | None = None, numerals: bool | None = None, paragraphs: bool | None = None, profanity_filter: bool | None = None, punctuate: bool | None = None, redact: bool | None = None, replace: bool | None = None, sample_rate: bool | None = None, search: bool | None = None, sentiment: bool | None = None, smart_format: bool | None = None, summarize: bool | None = None, tag: str | None = None, topics: bool | None = None, utt_split: bool | None = None, utterances: bool | None = None, version: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageV1Response, Get8ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the usage for a specific project. Use Get Project Usage Breakdown for a more comprehensive usage summary.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_usage.with_raw_response.get8(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get8ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_usage.with_raw_response.get8(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get8ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>Date \| None</code> | Start date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>end</code> | <code>Date \| None</code> | End date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>accessor</code> | <code>str \| None</code> | Filter for requests where a specific accessor was used<br>**Default**: <code>None</code> |
| <code>alternatives</code> | <code>bool \| None</code> | Filter for requests where alternatives were used<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>bool \| None</code> | Filter for requests where callback method was used<br>**Default**: <code>None</code> |
| <code>callback</code> | <code>bool \| None</code> | Filter for requests where callback was used<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>bool \| None</code> | Filter for requests where channels were used<br>**Default**: <code>None</code> |
| <code>custom_intent_mode</code> | <code>bool \| None</code> | Filter for requests where custom intent mode was used<br>**Default**: <code>None</code> |
| <code>custom_intent</code> | <code>bool \| None</code> | Filter for requests where custom intent was used<br>**Default**: <code>None</code> |
| <code>custom_topic_mode</code> | <code>bool \| None</code> | Filter for requests where custom topic mode was used<br>**Default**: <code>None</code> |
| <code>custom_topic</code> | <code>bool \| None</code> | Filter for requests where custom topic was used<br>**Default**: <code>None</code> |
| <code>deployment</code> | <code>[V1ProjectsProjectIdUsageGetParametersDeploymentOrStr](deepgram/models/enums/v1_projects_project_id_usage_get_parameters_deployment.py) \| None</code> | Filter for requests where a specific deployment was used<br>**Default**: <code>None</code> |
| <code>detect_entities</code> | <code>bool \| None</code> | Filter for requests where detect entities was used<br>**Default**: <code>None</code> |
| <code>detect_language</code> | <code>bool \| None</code> | Filter for requests where detect language was used<br>**Default**: <code>None</code> |
| <code>diarize</code> | <code>bool \| None</code> | Filter for requests where diarize was used<br>**Default**: <code>None</code> |
| <code>dictation</code> | <code>bool \| None</code> | Filter for requests where dictation was used<br>**Default**: <code>None</code> |
| <code>encoding</code> | <code>bool \| None</code> | Filter for requests where encoding was used<br>**Default**: <code>None</code> |
| <code>endpoint</code> | <code>[V1ProjectsProjectIdUsageGetParametersEndpointOrStr](deepgram/models/enums/v1_projects_project_id_usage_get_parameters_endpoint.py) \| None</code> | Filter for requests where a specific endpoint was used<br>**Default**: <code>None</code> |
| <code>extra</code> | <code>bool \| None</code> | Filter for requests where extra was used<br>**Default**: <code>None</code> |
| <code>filler_words</code> | <code>bool \| None</code> | Filter for requests where filler words was used<br>**Default**: <code>None</code> |
| <code>intents</code> | <code>bool \| None</code> | Filter for requests where intents was used<br>**Default**: <code>None</code> |
| <code>keyterm</code> | <code>bool \| None</code> | Filter for requests where keyterm was used<br>**Default**: <code>None</code> |
| <code>keywords</code> | <code>bool \| None</code> | Filter for requests where keywords was used<br>**Default**: <code>None</code> |
| <code>language</code> | <code>bool \| None</code> | Filter for requests where language was used<br>**Default**: <code>None</code> |
| <code>measurements</code> | <code>bool \| None</code> | Filter for requests where measurements were used<br>**Default**: <code>None</code> |
| <code>method</code> | <code>[V1ProjectsProjectIdUsageGetParametersMethodOrStr](deepgram/models/enums/v1_projects_project_id_usage_get_parameters_method.py) \| None</code> | Filter for requests where a specific method was used<br>**Default**: <code>None</code> |
| <code>model</code> | <code>str \| None</code> | Filter for requests where a specific model uuid was used<br>**Default**: <code>None</code> |
| <code>multichannel</code> | <code>bool \| None</code> | Filter for requests where multichannel was used<br>**Default**: <code>None</code> |
| <code>numerals</code> | <code>bool \| None</code> | Filter for requests where numerals were used<br>**Default**: <code>None</code> |
| <code>paragraphs</code> | <code>bool \| None</code> | Filter for requests where paragraphs were used<br>**Default**: <code>None</code> |
| <code>profanity_filter</code> | <code>bool \| None</code> | Filter for requests where profanity filter was used<br>**Default**: <code>None</code> |
| <code>punctuate</code> | <code>bool \| None</code> | Filter for requests where punctuate was used<br>**Default**: <code>None</code> |
| <code>redact</code> | <code>bool \| None</code> | Filter for requests where redact was used<br>**Default**: <code>None</code> |
| <code>replace</code> | <code>bool \| None</code> | Filter for requests where replace was used<br>**Default**: <code>None</code> |
| <code>sample_rate</code> | <code>bool \| None</code> | Filter for requests where sample rate was used<br>**Default**: <code>None</code> |
| <code>search</code> | <code>bool \| None</code> | Filter for requests where search was used<br>**Default**: <code>None</code> |
| <code>sentiment</code> | <code>bool \| None</code> | Filter for requests where sentiment was used<br>**Default**: <code>None</code> |
| <code>smart_format</code> | <code>bool \| None</code> | Filter for requests where smart format was used<br>**Default**: <code>None</code> |
| <code>summarize</code> | <code>bool \| None</code> | Filter for requests where summarize was used<br>**Default**: <code>None</code> |
| <code>tag</code> | <code>str \| None</code> | Filter for requests where a specific tag was used<br>**Default**: <code>None</code> |
| <code>topics</code> | <code>bool \| None</code> | Filter for requests where topics was used<br>**Default**: <code>None</code> |
| <code>utt_split</code> | <code>bool \| None</code> | Filter for requests where utt split was used<br>**Default**: <code>None</code> |
| <code>utterances</code> | <code>bool \| None</code> | Filter for requests where utterances was used<br>**Default**: <code>None</code> |
| <code>version</code> | <code>bool \| None</code> | Filter for requests where version was used<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[UsageV1Response](deepgram/models/usage_v1_response.py), [Get8ErrorBody](deepgram/errors/get8_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageV1Response](deepgram/models/usage_v1_response.py)</code> -- A specific request for a specific project

**On `Failure`**: `error` is <code>[Get8ErrorBody](deepgram/errors/get8_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsUsageBreakdown

> Source: [ManageV1ProjectsUsageBreakdown](deepgram/apis/manage_v1_projects_usage_breakdown.py)

<details>
<summary><code>def get9(project_id: str, *, start: Date | None = None, end: Date | None = None, grouping: V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None = None, accessor: str | None = None, alternatives: bool | None = None, callback_method: bool | None = None, callback: bool | None = None, channels: bool | None = None, custom_intent_mode: bool | None = None, custom_intent: bool | None = None, custom_topic_mode: bool | None = None, custom_topic: bool | None = None, deployment: V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None = None, detect_entities: bool | None = None, detect_language: bool | None = None, diarize: bool | None = None, dictation: bool | None = None, encoding: bool | None = None, endpoint: V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None = None, extra: bool | None = None, filler_words: bool | None = None, intents: bool | None = None, keyterm: bool | None = None, keywords: bool | None = None, language: bool | None = None, measurements: bool | None = None, method: V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None = None, model: str | None = None, multichannel: bool | None = None, numerals: bool | None = None, paragraphs: bool | None = None, profanity_filter: bool | None = None, punctuate: bool | None = None, redact: bool | None = None, replace: bool | None = None, sample_rate: bool | None = None, search: bool | None = None, sentiment: bool | None = None, smart_format: bool | None = None, summarize: bool | None = None, tag: str | None = None, topics: bool | None = None, utt_split: bool | None = None, utterances: bool | None = None, version: bool | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageBreakdownV1Response, Get9ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the usage breakdown for a specific project, with various filter options by API feature or by groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND logic.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_usage_breakdown.with_raw_response.get9(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageBreakdownV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get9ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_usage_breakdown.with_raw_response.get9(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageBreakdownV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get9ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>Date \| None</code> | Start date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>end</code> | <code>Date \| None</code> | End date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>grouping</code> | <code>[V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr](deepgram/models/enums/v1_projects_project_id_usage_breakdown_get_parameters_grouping.py) \| None</code> | Common usage grouping parameters<br>**Default**: <code>None</code> |
| <code>accessor</code> | <code>str \| None</code> | Filter for requests where a specific accessor was used<br>**Default**: <code>None</code> |
| <code>alternatives</code> | <code>bool \| None</code> | Filter for requests where alternatives were used<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>bool \| None</code> | Filter for requests where callback method was used<br>**Default**: <code>None</code> |
| <code>callback</code> | <code>bool \| None</code> | Filter for requests where callback was used<br>**Default**: <code>None</code> |
| <code>channels</code> | <code>bool \| None</code> | Filter for requests where channels were used<br>**Default**: <code>None</code> |
| <code>custom_intent_mode</code> | <code>bool \| None</code> | Filter for requests where custom intent mode was used<br>**Default**: <code>None</code> |
| <code>custom_intent</code> | <code>bool \| None</code> | Filter for requests where custom intent was used<br>**Default**: <code>None</code> |
| <code>custom_topic_mode</code> | <code>bool \| None</code> | Filter for requests where custom topic mode was used<br>**Default**: <code>None</code> |
| <code>custom_topic</code> | <code>bool \| None</code> | Filter for requests where custom topic was used<br>**Default**: <code>None</code> |
| <code>deployment</code> | <code>[V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr](deepgram/models/enums/v1_projects_project_id_usage_breakdown_get_parameters_deployment.py) \| None</code> | Filter for requests where a specific deployment was used<br>**Default**: <code>None</code> |
| <code>detect_entities</code> | <code>bool \| None</code> | Filter for requests where detect entities was used<br>**Default**: <code>None</code> |
| <code>detect_language</code> | <code>bool \| None</code> | Filter for requests where detect language was used<br>**Default**: <code>None</code> |
| <code>diarize</code> | <code>bool \| None</code> | Filter for requests where diarize was used<br>**Default**: <code>None</code> |
| <code>dictation</code> | <code>bool \| None</code> | Filter for requests where dictation was used<br>**Default**: <code>None</code> |
| <code>encoding</code> | <code>bool \| None</code> | Filter for requests where encoding was used<br>**Default**: <code>None</code> |
| <code>endpoint</code> | <code>[V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr](deepgram/models/enums/v1_projects_project_id_usage_breakdown_get_parameters_endpoint.py) \| None</code> | Filter for requests where a specific endpoint was used<br>**Default**: <code>None</code> |
| <code>extra</code> | <code>bool \| None</code> | Filter for requests where extra was used<br>**Default**: <code>None</code> |
| <code>filler_words</code> | <code>bool \| None</code> | Filter for requests where filler words was used<br>**Default**: <code>None</code> |
| <code>intents</code> | <code>bool \| None</code> | Filter for requests where intents was used<br>**Default**: <code>None</code> |
| <code>keyterm</code> | <code>bool \| None</code> | Filter for requests where keyterm was used<br>**Default**: <code>None</code> |
| <code>keywords</code> | <code>bool \| None</code> | Filter for requests where keywords was used<br>**Default**: <code>None</code> |
| <code>language</code> | <code>bool \| None</code> | Filter for requests where language was used<br>**Default**: <code>None</code> |
| <code>measurements</code> | <code>bool \| None</code> | Filter for requests where measurements were used<br>**Default**: <code>None</code> |
| <code>method</code> | <code>[V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr](deepgram/models/enums/v1_projects_project_id_usage_breakdown_get_parameters_method.py) \| None</code> | Filter for requests where a specific method was used<br>**Default**: <code>None</code> |
| <code>model</code> | <code>str \| None</code> | Filter for requests where a specific model uuid was used<br>**Default**: <code>None</code> |
| <code>multichannel</code> | <code>bool \| None</code> | Filter for requests where multichannel was used<br>**Default**: <code>None</code> |
| <code>numerals</code> | <code>bool \| None</code> | Filter for requests where numerals were used<br>**Default**: <code>None</code> |
| <code>paragraphs</code> | <code>bool \| None</code> | Filter for requests where paragraphs were used<br>**Default**: <code>None</code> |
| <code>profanity_filter</code> | <code>bool \| None</code> | Filter for requests where profanity filter was used<br>**Default**: <code>None</code> |
| <code>punctuate</code> | <code>bool \| None</code> | Filter for requests where punctuate was used<br>**Default**: <code>None</code> |
| <code>redact</code> | <code>bool \| None</code> | Filter for requests where redact was used<br>**Default**: <code>None</code> |
| <code>replace</code> | <code>bool \| None</code> | Filter for requests where replace was used<br>**Default**: <code>None</code> |
| <code>sample_rate</code> | <code>bool \| None</code> | Filter for requests where sample rate was used<br>**Default**: <code>None</code> |
| <code>search</code> | <code>bool \| None</code> | Filter for requests where search was used<br>**Default**: <code>None</code> |
| <code>sentiment</code> | <code>bool \| None</code> | Filter for requests where sentiment was used<br>**Default**: <code>None</code> |
| <code>smart_format</code> | <code>bool \| None</code> | Filter for requests where smart format was used<br>**Default**: <code>None</code> |
| <code>summarize</code> | <code>bool \| None</code> | Filter for requests where summarize was used<br>**Default**: <code>None</code> |
| <code>tag</code> | <code>str \| None</code> | Filter for requests where a specific tag was used<br>**Default**: <code>None</code> |
| <code>topics</code> | <code>bool \| None</code> | Filter for requests where topics was used<br>**Default**: <code>None</code> |
| <code>utt_split</code> | <code>bool \| None</code> | Filter for requests where utt split was used<br>**Default**: <code>None</code> |
| <code>utterances</code> | <code>bool \| None</code> | Filter for requests where utterances was used<br>**Default**: <code>None</code> |
| <code>version</code> | <code>bool \| None</code> | Filter for requests where version was used<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[UsageBreakdownV1Response](deepgram/models/usage_breakdown_v1_response.py), [Get9ErrorBody](deepgram/errors/get9_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageBreakdownV1Response](deepgram/models/usage_breakdown_v1_response.py)</code> -- Usage breakdown response

**On `Failure`**: `error` is <code>[Get9ErrorBody](deepgram/errors/get9_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManageV1ProjectsUsageFields

> Source: [ManageV1ProjectsUsageFields](deepgram/apis/manage_v1_projects_usage_fields.py)

<details>
<summary><code>def list12(project_id: str, *, start: Date | None = None, end: Date | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageFieldsV1Response, List12ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the features, models, tags, languages, and processing method used for requests in the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.manage_v1_projects_usage_fields.with_raw_response.list12(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageFieldsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List12ErrorBody
```

**Async**

```python
result = await async_client.manage_v1_projects_usage_fields.with_raw_response.list12(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageFieldsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List12ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>start</code> | <code>Date \| None</code> | Start date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>end</code> | <code>Date \| None</code> | End date of the requested date range. Format accepted is YYYY-MM-DD<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[UsageFieldsV1Response](deepgram/models/usage_fields_v1_response.py), [List12ErrorBody](deepgram/errors/list12_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageFieldsV1Response](deepgram/models/usage_fields_v1_response.py)</code> -- A list of fields for a specific project

**On `Failure`**: `error` is <code>[List12ErrorBody](deepgram/errors/list12_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReadV1Text

> Source: [ReadV1Text](deepgram/apis/read_v1_text.py)

<details>
<summary><code>def analyze(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, sentiment: bool | None = False, summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None, tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None, topics: bool | None = False, custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None, custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, intents: bool | None = False, custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None, custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, language: str | None = "en", body: ReadV1Request | ReadV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReadV1Response, AnalyzeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Analyze text content using Deepgrams text analysis API

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.read_v1_text.with_raw_response.analyze()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReadV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AnalyzeErrorBody
```

**Async**

```python
result = await async_client.read_v1_text.with_raw_response.analyze()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReadV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AnalyzeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>callback</code> | <code>str \| None</code> | URL to which we'll make the callback request<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>[V1ListenPostParametersCallbackMethodOrStr](deepgram/models/enums/v1_listen_post_parameters_callback_method.py) \| None</code> | HTTP method by which the callback request will be made<br>**Default**: <code>None</code> |
| <code>sentiment</code> | <code>bool \| None</code> | Recognizes the sentiment throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>summarize</code> | <code>[V1ReadPostParametersSummarize](deepgram/models/unions/v1_read_post_parameters_summarize.py) \| [V1ReadPostParametersSummarizeDict](deepgram/models/unions/v1_read_post_parameters_summarize.py) \| None</code> | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only.<br>**Default**: <code>None</code> |
| <code>tag</code> | <code>[V1ReadPostParametersTag](deepgram/models/unions/v1_read_post_parameters_tag.py) \| [V1ReadPostParametersTagDict](deepgram/models/unions/v1_read_post_parameters_tag.py) \| None</code> | Label your requests for the purpose of identification during usage reporting<br>**Default**: <code>None</code> |
| <code>topics</code> | <code>bool \| None</code> | Detect topics throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>custom_topic</code> | <code>[V1ReadPostParametersCustomTopic](deepgram/models/unions/v1_read_post_parameters_custom_topic.py) \| [V1ReadPostParametersCustomTopicDict](deepgram/models/unions/v1_read_post_parameters_custom_topic.py) \| None</code> | Custom topics you want the model to detect within your input audio or text if present Submit up to `100`.<br>**Default**: <code>None</code> |
| <code>custom_topic_mode</code> | <code>[V1ListenPostParametersCustomTopicModeOrStr](deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py) \| None</code> | Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param<br>**Default**: <code>None</code> |
| <code>intents</code> | <code>bool \| None</code> | Recognizes speaker intent throughout a transcript or text<br>**Default**: <code>False</code> |
| <code>custom_intent</code> | <code>[V1ReadPostParametersCustomIntent](deepgram/models/unions/v1_read_post_parameters_custom_intent.py) \| [V1ReadPostParametersCustomIntentDict](deepgram/models/unions/v1_read_post_parameters_custom_intent.py) \| None</code> | Custom intents you want the model to detect within your input audio if present<br>**Default**: <code>None</code> |
| <code>custom_intent_mode</code> | <code>[V1ListenPostParametersCustomTopicModeOrStr](deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py) \| None</code> | Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.<br>**Default**: <code>None</code> |
| <code>language</code> | <code>str \| None</code> | The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available<br>**Default**: <code>"en"</code> |
| <code>body</code> | <code>[ReadV1Request](deepgram/models/unions/read_v1_request.py) \| [ReadV1RequestDict](deepgram/models/unions/read_v1_request.py) \| None</code> | Analyze a text file<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ReadV1Response](deepgram/models/read_v1_response.py), [AnalyzeErrorBody](deepgram/errors/analyze_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReadV1Response](deepgram/models/read_v1_response.py)</code> -- Successful text analysis

**On `Failure`**: `error` is <code>[AnalyzeErrorBody](deepgram/errors/analyze_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SelfHostedV1DistributionCredentials

> Source: [SelfHostedV1DistributionCredentials](deepgram/apis/self_hosted_v1_distribution_credentials.py)

<details>
<summary><code>def create5(project_id: str, *, scopes: list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None = None, provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None, body: CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateProjectDistributionCredentialsV1Response, Create5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a set of distribution credentials for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.self_hosted_v1_distribution_credentials.with_raw_response.create5(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create5ErrorBody
```

**Async**

```python
result = await async_client.self_hosted_v1_distribution_credentials.with_raw_response.create5(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>scopes</code> | <code>list&#91;[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr](deepgram/models/enums/v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_scopes_schema_items.py)&#93; \| None</code> | List of permission scopes for the credentials<br>**Default**: <code>None</code> |
| <code>provider</code> | <code>[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr](deepgram/models/enums/v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_provider.py) \| None</code> | The provider of the distribution service<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[CreateProjectDistributionCredentialsV1Request](deepgram/models/create_project_distribution_credentials_v1_request.py) \| [CreateProjectDistributionCredentialsV1RequestDict](deepgram/models/create_project_distribution_credentials_v1_request.py) \| None</code> | The set of distribution credentials to create<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[CreateProjectDistributionCredentialsV1Response](deepgram/models/create_project_distribution_credentials_v1_response.py), [Create5ErrorBody](deepgram/errors/create5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateProjectDistributionCredentialsV1Response](deepgram/models/create_project_distribution_credentials_v1_response.py)</code> -- Single distribution credential

**On `Failure`**: `error` is <code>[Create5ErrorBody](deepgram/errors/create5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete7(project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectDistributionCredentialsV1Response, Delete7ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a set of distribution credentials for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.self_hosted_v1_distribution_credentials.with_raw_response.delete7(
    project_id, distribution_credentials_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete7ErrorBody
```

**Async**

```python
result = await async_client.self_hosted_v1_distribution_credentials.with_raw_response.delete7(
    project_id, distribution_credentials_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete7ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>distribution_credentials_id</code> | <code>str</code> | The UUID of the distribution credentials |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectDistributionCredentialsV1Response](deepgram/models/get_project_distribution_credentials_v1_response.py), [Delete7ErrorBody](deepgram/errors/delete7_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectDistributionCredentialsV1Response](deepgram/models/get_project_distribution_credentials_v1_response.py)</code> -- Single distribution credential

**On `Failure`**: `error` is <code>[Delete7ErrorBody](deepgram/errors/delete7_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get11(project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetProjectDistributionCredentialsV1Response, Get11ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a set of distribution credentials for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.self_hosted_v1_distribution_credentials.with_raw_response.get11(project_id, distribution_credentials_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get11ErrorBody
```

**Async**

```python
result = await async_client.self_hosted_v1_distribution_credentials.with_raw_response.get11(
    project_id, distribution_credentials_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get11ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>distribution_credentials_id</code> | <code>str</code> | The UUID of the distribution credentials |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[GetProjectDistributionCredentialsV1Response](deepgram/models/get_project_distribution_credentials_v1_response.py), [Get11ErrorBody](deepgram/errors/get11_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetProjectDistributionCredentialsV1Response](deepgram/models/get_project_distribution_credentials_v1_response.py)</code> -- Single distribution credential

**On `Failure`**: `error` is <code>[Get11ErrorBody](deepgram/errors/get11_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list17(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectDistributionCredentialsV1Response, List17ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists sets of distribution credentials for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.self_hosted_v1_distribution_credentials.with_raw_response.list17(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List17ErrorBody
```

**Async**

```python
result = await async_client.self_hosted_v1_distribution_credentials.with_raw_response.list17(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectDistributionCredentialsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List17ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListProjectDistributionCredentialsV1Response](deepgram/models/list_project_distribution_credentials_v1_response.py), [List17ErrorBody](deepgram/errors/list17_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectDistributionCredentialsV1Response](deepgram/models/list_project_distribution_credentials_v1_response.py)</code> -- A list of distribution credentials for a specific project

**On `Failure`**: `error` is <code>[List17ErrorBody](deepgram/errors/list17_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SpeakV1Audio

> Source: [SpeakV1Audio](deepgram/apis/speak_v1_audio.py)

<details>
<summary><code>def generate(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, mip_opt_out: bool | None = False, tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None, bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None, container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None, encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None, model: V1SpeakPostParametersModelOrStr | None = None, sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None, speed: float | None = 1.0, body: SpeakV1Request | SpeakV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GenerateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert text into natural-sounding speech using Deepgram's TTS REST API

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.speak_v1_audio.with_raw_response.generate()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateErrorBody
```

**Async**

```python
result = await async_client.speak_v1_audio.with_raw_response.generate()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>callback</code> | <code>str \| None</code> | URL to which we'll make the callback request<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>[V1ListenPostParametersCallbackMethodOrStr](deepgram/models/enums/v1_listen_post_parameters_callback_method.py) \| None</code> | HTTP method by which the callback request will be made<br>**Default**: <code>None</code> |
| <code>mip_opt_out</code> | <code>bool \| None</code> | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br>**Default**: <code>False</code> |
| <code>tag</code> | <code>[V1SpeakPostParametersTag](deepgram/models/unions/v1_speak_post_parameters_tag.py) \| [V1SpeakPostParametersTagDict](deepgram/models/unions/v1_speak_post_parameters_tag.py) \| None</code> | Label your requests for the purpose of identification during usage reporting<br>**Default**: <code>None</code> |
| <code>bit_rate</code> | <code>[V1SpeakPostParametersBitRate](deepgram/models/unions/v1_speak_post_parameters_bit_rate.py) \| [V1SpeakPostParametersBitRateDict](deepgram/models/unions/v1_speak_post_parameters_bit_rate.py) \| None</code> | The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.<br>**Default**: <code>None</code> |
| <code>container</code> | <code>[V1SpeakPostParametersContainer](deepgram/models/unions/v1_speak_post_parameters_container.py) \| [V1SpeakPostParametersContainerDict](deepgram/models/unions/v1_speak_post_parameters_container.py) \| None</code> | Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.<br>**Default**: <code>None</code> |
| <code>encoding</code> | <code>[V1SpeakPostParametersEncoding](deepgram/models/unions/v1_speak_post_parameters_encoding.py) \| [V1SpeakPostParametersEncodingDict](deepgram/models/unions/v1_speak_post_parameters_encoding.py) \| None</code> | Encoding allows you to specify the expected encoding of your audio output<br>**Default**: <code>None</code> |
| <code>model</code> | <code>[V1SpeakPostParametersModelOrStr](deepgram/models/enums/v1_speak_post_parameters_model.py) \| None</code> | AI model used to process submitted text<br>**Default**: <code>None</code> |
| <code>sample_rate</code> | <code>[V1SpeakPostParametersSampleRate](deepgram/models/unions/v1_speak_post_parameters_sample_rate.py) \| [V1SpeakPostParametersSampleRateDict](deepgram/models/unions/v1_speak_post_parameters_sample_rate.py) \| None</code> | Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable<br>**Default**: <code>None</code> |
| <code>speed</code> | <code>float \| None</code> | Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody and voice quality. Not yet supported in all languages.<br>**Default**: <code>1.0</code> |
| <code>body</code> | <code>[SpeakV1Request](deepgram/models/speak_v1_request.py) \| [SpeakV1RequestDict](deepgram/models/speak_v1_request.py) \| None</code> | Transform text to speech<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;Any, [GenerateErrorBody](deepgram/errors/generate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Successful text-to-speech transformation

**On `Failure`**: `error` is <code>[GenerateErrorBody](deepgram/errors/generate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SpeakV2Audio

> Source: [SpeakV2Audio](deepgram/apis/speak_v2_audio.py)

<details>
<summary><code>def generate2(model: str, *, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, mip_opt_out: bool | None = False, tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None, bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None, container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None, encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None, sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None, priority: V2SpeakPostParametersPriorityOrStr | None = None, body: SpeakV2Request | SpeakV2RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SpeakV2AcceptedResponse, Generate2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API. Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up front and you don't need incremental playback or interruption.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.speak_v2_audio.with_raw_response.generate2(model)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SpeakV2AcceptedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Generate2ErrorBody
```

**Async**

```python
result = await async_client.speak_v2_audio.with_raw_response.generate2(model)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SpeakV2AcceptedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Generate2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>model</code> | <code>str</code> | Flux TTS model used to synthesize the submitted text, in the form `flux-{voice}-{language}` (for example, `flux-alexis-en`). Required; unlike the v1 (Aura) endpoint there is no default and only flux models are accepted. English-only at launch. |
| <code>callback</code> | <code>str \| None</code> | URL to which we'll make the callback request<br>**Default**: <code>None</code> |
| <code>callback_method</code> | <code>[V1ListenPostParametersCallbackMethodOrStr](deepgram/models/enums/v1_listen_post_parameters_callback_method.py) \| None</code> | HTTP method by which the callback request will be made<br>**Default**: <code>None</code> |
| <code>mip_opt_out</code> | <code>bool \| None</code> | Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing impacts before setting this to true. https://dpgr.am/deepgram-mip<br>**Default**: <code>False</code> |
| <code>tag</code> | <code>[V2SpeakPostParametersTag](deepgram/models/unions/v2_speak_post_parameters_tag.py) \| [V2SpeakPostParametersTagDict](deepgram/models/unions/v2_speak_post_parameters_tag.py) \| None</code> | Label your requests for the purpose of identification during usage reporting<br>**Default**: <code>None</code> |
| <code>bit_rate</code> | <code>[V2SpeakPostParametersBitRate](deepgram/models/unions/v2_speak_post_parameters_bit_rate.py) \| [V2SpeakPostParametersBitRateDict](deepgram/models/unions/v2_speak_post_parameters_bit_rate.py) \| None</code> | The bitrate of the audio in bits per second. Choose from predefined ranges or specific values based on the encoding type.<br>**Default**: <code>None</code> |
| <code>container</code> | <code>[V2SpeakPostParametersContainer](deepgram/models/unions/v2_speak_post_parameters_container.py) \| [V2SpeakPostParametersContainerDict](deepgram/models/unions/v2_speak_post_parameters_container.py) \| None</code> | Container specifies the file format wrapper for the output audio. The available options depend on the encoding type.<br>**Default**: <code>None</code> |
| <code>encoding</code> | <code>[V2SpeakPostParametersEncoding](deepgram/models/unions/v2_speak_post_parameters_encoding.py) \| [V2SpeakPostParametersEncodingDict](deepgram/models/unions/v2_speak_post_parameters_encoding.py) \| None</code> | Encoding allows you to specify the expected encoding of your audio output<br>**Default**: <code>None</code> |
| <code>sample_rate</code> | <code>[V2SpeakPostParametersSampleRate](deepgram/models/unions/v2_speak_post_parameters_sample_rate.py) \| [V2SpeakPostParametersSampleRateDict](deepgram/models/unions/v2_speak_post_parameters_sample_rate.py) \| None</code> | Sample Rate specifies the sample rate for the output audio. Based on the encoding, different sample rates are supported. For some encodings, the sample rate is not configurable<br>**Default**: <code>None</code> |
| <code>priority</code> | <code>[V2SpeakPostParametersPriorityOrStr](deepgram/models/enums/v2_speak_post_parameters_priority.py) \| None</code> | Processing priority for asynchronous (callback) requests. The only supported value is low.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>[SpeakV2Request](deepgram/models/speak_v2_request.py) \| [SpeakV2RequestDict](deepgram/models/speak_v2_request.py) \| None</code> | Transform text to speech<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[SpeakV2AcceptedResponse](deepgram/models/speak_v2_accepted_response.py), [Generate2ErrorBody](deepgram/errors/generate2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SpeakV2AcceptedResponse](deepgram/models/speak_v2_accepted_response.py)</code> -- Returns the synthesized audio in the requested encoding as a binary stream. When a `callback` URL is supplied, the request is processed asynchronously and the response body is instead a JSON acknowledgement (Content-Type `application/json`) of the form {"request_id": "..."}, with the audio delivered to the callback URL. Because this endpoint is typed as a binary audio stream, SDK callers that set `callback` receive this JSON acknowledgement through the audio byte iterator as raw bytes and must join the chunks and parse `request_id` themselves.

**On `Failure`**: `error` is <code>[Generate2ErrorBody](deepgram/errors/generate2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## VoiceAgentConfigurations

> Source: [VoiceAgentConfigurations](deepgram/apis/voice_agent_configurations.py)

<details>
<summary><code>def create(project_id: str, *, body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateAgentConfigurationV1Response, CreateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new reusable agent configuration. The `config` field must be a valid JSON string representing the `agent` block of a Settings message. The returned `agent_id` can be passed in place of the full `agent` object in future Settings messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_configurations.with_raw_response.create(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateAgentConfigurationV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateErrorBody
```

**Async**

```python
result = await async_client.voice_agent_configurations.with_raw_response.create(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateAgentConfigurationV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>body</code> | <code>[CreateAgentConfigurationV1Request](deepgram/models/create_agent_configuration_v1_request.py) \| [CreateAgentConfigurationV1RequestDict](deepgram/models/create_agent_configuration_v1_request.py) \| None</code> | Agent configuration details<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[CreateAgentConfigurationV1Response](deepgram/models/create_agent_configuration_v1_response.py), [CreateErrorBody](deepgram/errors/create_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateAgentConfigurationV1Response](deepgram/models/create_agent_configuration_v1_response.py)</code> -- Agent configuration created successfully

**On `Failure`**: `error` is <code>[CreateErrorBody](deepgram/errors/create_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete(project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, DeleteErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_configurations.with_raw_response.delete(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteErrorBody
```

**Async**

```python
result = await async_client.voice_agent_configurations.with_raw_response.delete(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>agent_id</code> | <code>str</code> | The unique identifier of the agent configuration |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;Any, [DeleteErrorBody](deepgram/errors/delete_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Agent configuration deleted

**On `Failure`**: `error` is <code>[DeleteErrorBody](deepgram/errors/delete_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get(project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentConfigurationV1, GetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the specified agent configuration in its uninterpolated form

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_configurations.with_raw_response.get(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentConfigurationV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetErrorBody
```

**Async**

```python
result = await async_client.voice_agent_configurations.with_raw_response.get(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentConfigurationV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>agent_id</code> | <code>str</code> | The unique identifier of the agent configuration |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentConfigurationV1](deepgram/models/agent_configuration_v1.py), [GetErrorBody](deepgram/errors/get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentConfigurationV1](deepgram/models/agent_configuration_v1.py)</code> -- An agent configuration

**On `Failure`**: `error` is <code>[GetErrorBody](deepgram/errors/get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list2(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListAgentConfigurationsV1Response, List2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all agent configurations for the specified project. Configurations are returned in their uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_configurations.with_raw_response.list2(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentConfigurationsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List2ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_configurations.with_raw_response.list2(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentConfigurationsV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListAgentConfigurationsV1Response](deepgram/models/list_agent_configurations_v1_response.py), [List2ErrorBody](deepgram/errors/list2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListAgentConfigurationsV1Response](deepgram/models/list_agent_configurations_v1_response.py)</code> -- A list of agent configurations

**On `Failure`**: `error` is <code>[List2ErrorBody](deepgram/errors/list2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update(project_id: str, agent_id: str, *, body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentConfigurationV1, UpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the metadata associated with an agent configuration. The config itself is immutable—to change the configuration, delete the existing agent and create a new one.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_configurations.with_raw_response.update(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentConfigurationV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateErrorBody
```

**Async**

```python
result = await async_client.voice_agent_configurations.with_raw_response.update(project_id, agent_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentConfigurationV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>agent_id</code> | <code>str</code> | The unique identifier of the agent configuration |
| <code>body</code> | <code>[UpdateAgentMetadataV1Request](deepgram/models/update_agent_metadata_v1_request.py) \| [UpdateAgentMetadataV1RequestDict](deepgram/models/update_agent_metadata_v1_request.py) \| None</code> | Updated metadata for the agent configuration<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentConfigurationV1](deepgram/models/agent_configuration_v1.py), [UpdateErrorBody](deepgram/errors/update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentConfigurationV1](deepgram/models/agent_configuration_v1.py)</code> -- Agent configuration updated

**On `Failure`**: `error` is <code>[UpdateErrorBody](deepgram/errors/update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## VoiceAgentVariables

> Source: [VoiceAgentVariables](deepgram/apis/voice_agent_variables.py)

<details>
<summary><code>def create2(project_id: str, *, body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentVariableV1, Create2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new template variable. Variables follow the `DG_<VARIABLE_NAME>` naming format and can substitute any JSON value in an agent configuration.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_variables.with_raw_response.create2(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create2ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_variables.with_raw_response.create2(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Create2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>body</code> | <code>[CreateAgentVariableV1Request](deepgram/models/create_agent_variable_v1_request.py) \| [CreateAgentVariableV1RequestDict](deepgram/models/create_agent_variable_v1_request.py) \| None</code> | Agent variable details<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentVariableV1](deepgram/models/agent_variable_v1.py), [Create2ErrorBody](deepgram/errors/create2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentVariableV1](deepgram/models/agent_variable_v1.py)</code> -- Agent variable created successfully

**On `Failure`**: `error` is <code>[Create2ErrorBody](deepgram/errors/create2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete2(project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, Delete2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified template variable

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_variables.with_raw_response.delete2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete2ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_variables.with_raw_response.delete2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Delete2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>variable_id</code> | <code>str</code> | The unique identifier of the agent variable |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;Any, [Delete2ErrorBody](deepgram/errors/delete2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Agent variable deleted

**On `Failure`**: `error` is <code>[Delete2ErrorBody](deepgram/errors/delete2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get2(project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentVariableV1, Get2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the specified template variable

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_variables.with_raw_response.get2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get2ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_variables.with_raw_response.get2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Get2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>variable_id</code> | <code>str</code> | The unique identifier of the agent variable |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentVariableV1](deepgram/models/agent_variable_v1.py), [Get2ErrorBody](deepgram/errors/get2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentVariableV1](deepgram/models/agent_variable_v1.py)</code> -- An agent variable

**On `Failure`**: `error` is <code>[Get2ErrorBody](deepgram/errors/get2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list3(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListAgentVariablesV1Response, List3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns all template variables for the specified project

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_variables.with_raw_response.list3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentVariablesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List3ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_variables.with_raw_response.list3(project_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAgentVariablesV1Response
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type List3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[ListAgentVariablesV1Response](deepgram/models/list_agent_variables_v1_response.py), [List3ErrorBody](deepgram/errors/list3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListAgentVariablesV1Response](deepgram/models/list_agent_variables_v1_response.py)</code> -- A list of agent variables

**On `Failure`**: `error` is <code>[List3ErrorBody](deepgram/errors/list3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update2(project_id: str, variable_id: str, *, body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AgentVariableV1, Update2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the value of an existing template variable

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.voice_agent_variables.with_raw_response.update2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update2ErrorBody
```

**Async**

```python
result = await async_client.voice_agent_variables.with_raw_response.update2(project_id, variable_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AgentVariableV1
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type Update2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The unique identifier of the project |
| <code>variable_id</code> | <code>str</code> | The unique identifier of the agent variable |
| <code>body</code> | <code>[UpdateAgentVariableV1Request](deepgram/models/update_agent_variable_v1_request.py) \| [UpdateAgentVariableV1RequestDict](deepgram/models/update_agent_variable_v1_request.py) \| None</code> | Updated value for the agent variable<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](deepgram/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](deepgram/core/results.py)&#91;[AgentVariableV1](deepgram/models/agent_variable_v1.py), [Update2ErrorBody](deepgram/errors/update2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AgentVariableV1](deepgram/models/agent_variable_v1.py)</code> -- Agent variable updated

**On `Failure`**: `error` is <code>[Update2ErrorBody](deepgram/errors/update2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](deepgram/models/unions/error_response.py)</code> |
| anything unmapped | <code>[RawError](deepgram/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

