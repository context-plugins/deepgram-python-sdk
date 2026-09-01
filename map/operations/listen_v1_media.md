<!-- Generated file — do not edit; regenerated with the SDK. -->

# ListenV1Media — operations

Accessor: `client.listen_v1_media` · Source: `deepgram/apis/listen_v1_media.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.listen_v1_media.transcribe

- **Route**: `POST /v1/listen`
- **Auth**: `api_key_auth`
- **Signature**: `def transcribe(*, callback: str | None = None, callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None, extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None, sentiment: bool | None = False, summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None, tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None, topics: bool | None = False, custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None, custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, intents: bool | None = False, custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None, custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None, detect_entities: bool | None = False, detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None, diarize: bool | None = False, diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None, dictation: bool | None = False, encoding: V1ListenPostParametersEncodingOrStr | None = None, filler_words: bool | None = False, keyterm: list[str] | None = None, keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None, language: str | None = "en", measurements: bool | None = False, model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None, multichannel: bool | None = False, numerals: bool | None = False, paragraphs: bool | None = False, profanity_filter: bool | None = False, punctuate: bool | None = False, redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None, replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None, search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None, smart_format: bool | None = False, utterances: bool | None = False, utt_split: float | None = 0.8, version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None, mip_opt_out: bool | None = False, body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `callback` — query · `callback_method` — query · `extra` — query · `sentiment` — query · `summarize` — query · `tag` — query · `topics` — query · `custom_topic` — query · `custom_topic_mode` — query · `intents` — query · `custom_intent` — query · `custom_intent_mode` — query · `detect_entities` — query · `detect_language` — query · `diarize` — query · `diarize_model` — query · `dictation` — query · `encoding` — query · `filler_words` — query · `keyterm` — query · `keywords` — query · `language` — query · `measurements` — query · `model` — query · `multichannel` — query · `numerals` — query · `paragraphs` — query · `profanity_filter` — query · `punctuate` — query · `redact` — query · `replace` — query · `search` — query · `smart_format` — query · `utterances` — query · `utt_split` — query · `version` — query · `mip_opt_out` — query · `body` — JSON body
- **Returns (parsed)**: `ListenV1MediaTranscribeResponse200`
- **Returns (raw)**: `ApiResult[ListenV1MediaTranscribeResponse200, TranscribeErrorBody]`
- **Error**: `TranscribeErrorBody` — **Case A (typed)**
- **Error arms**: `ListenV1Response` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ListenPostParametersCallbackMethodOrStr` | `deepgram/models/enums/v1_listen_post_parameters_callback_method.py` |
| `V1ListenPostParametersExtra` | `deepgram/models/unions/v1_listen_post_parameters_extra.py` |
| `V1ListenPostParametersExtraDict` | `deepgram/models/unions/v1_listen_post_parameters_extra.py` |
| `V1ListenPostParametersSummarize` | `deepgram/models/unions/v1_listen_post_parameters_summarize.py` |
| `V1ListenPostParametersSummarizeDict` | `deepgram/models/unions/v1_listen_post_parameters_summarize.py` |
| `V1ListenPostParametersTag` | `deepgram/models/unions/v1_listen_post_parameters_tag.py` |
| `V1ListenPostParametersTagDict` | `deepgram/models/unions/v1_listen_post_parameters_tag.py` |
| `V1ListenPostParametersCustomTopic` | `deepgram/models/unions/v1_listen_post_parameters_custom_topic.py` |
| `V1ListenPostParametersCustomTopicDict` | `deepgram/models/unions/v1_listen_post_parameters_custom_topic.py` |
| `V1ListenPostParametersCustomTopicModeOrStr` | `deepgram/models/enums/v1_listen_post_parameters_custom_topic_mode.py` |
| `V1ListenPostParametersCustomIntent` | `deepgram/models/unions/v1_listen_post_parameters_custom_intent.py` |
| `V1ListenPostParametersCustomIntentDict` | `deepgram/models/unions/v1_listen_post_parameters_custom_intent.py` |
| `V1ListenPostParametersDetectLanguage` | `deepgram/models/unions/v1_listen_post_parameters_detect_language.py` |
| `V1ListenPostParametersDetectLanguageDict` | `deepgram/models/unions/v1_listen_post_parameters_detect_language.py` |
| `V1ListenPostParametersDiarizeModelOrStr` | `deepgram/models/enums/v1_listen_post_parameters_diarize_model.py` |
| `V1ListenPostParametersEncodingOrStr` | `deepgram/models/enums/v1_listen_post_parameters_encoding.py` |
| `V1ListenPostParametersKeywords` | `deepgram/models/unions/v1_listen_post_parameters_keywords.py` |
| `V1ListenPostParametersKeywordsDict` | `deepgram/models/unions/v1_listen_post_parameters_keywords.py` |
| `V1ListenPostParametersModel` | `deepgram/models/unions/v1_listen_post_parameters_model.py` |
| `V1ListenPostParametersModelDict` | `deepgram/models/unions/v1_listen_post_parameters_model.py` |
| `V1ListenPostParametersRedact` | `deepgram/models/unions/v1_listen_post_parameters_redact.py` |
| `V1ListenPostParametersRedactDict` | `deepgram/models/unions/v1_listen_post_parameters_redact.py` |
| `V1ListenPostParametersReplace` | `deepgram/models/unions/v1_listen_post_parameters_replace.py` |
| `V1ListenPostParametersReplaceDict` | `deepgram/models/unions/v1_listen_post_parameters_replace.py` |
| `V1ListenPostParametersSearch` | `deepgram/models/unions/v1_listen_post_parameters_search.py` |
| `V1ListenPostParametersSearchDict` | `deepgram/models/unions/v1_listen_post_parameters_search.py` |
| `V1ListenPostParametersVersion` | `deepgram/models/unions/v1_listen_post_parameters_version.py` |
| `V1ListenPostParametersVersionDict` | `deepgram/models/unions/v1_listen_post_parameters_version.py` |
| `ListenV1RequestUrl` | `deepgram/models/listen_v1_request_url.py` |
| `ListenV1RequestUrlDict` | `deepgram/models/listen_v1_request_url.py` |
| `ListenV1MediaTranscribeResponse200` | `deepgram/models/unions/listen_v1_media_transcribe_response200.py` |
| `TranscribeErrorBody` | `deepgram/errors/transcribe_error.py` |
| `ListenV1Response` | `deepgram/models/listen_v1_response.py` |

