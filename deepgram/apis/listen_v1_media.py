from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
)
from ..errors.transcribe_error import TranscribeErrorBody, transcribe_error_mapper
from ..models.enums.v1_listen_post_parameters_callback_method import V1ListenPostParametersCallbackMethodOrStr
from ..models.enums.v1_listen_post_parameters_custom_topic_mode import V1ListenPostParametersCustomTopicModeOrStr
from ..models.enums.v1_listen_post_parameters_diarize_model import V1ListenPostParametersDiarizeModelOrStr
from ..models.enums.v1_listen_post_parameters_encoding import V1ListenPostParametersEncodingOrStr
from ..models.listen_v1_request_url import ListenV1RequestUrl, ListenV1RequestUrlDict
from ..models.unions.listen_v1_media_transcribe_response200 import ListenV1MediaTranscribeResponse200
from ..models.unions.v1_listen_post_parameters_custom_intent import (
    V1ListenPostParametersCustomIntent,
    V1ListenPostParametersCustomIntentDict,
)
from ..models.unions.v1_listen_post_parameters_custom_topic import (
    V1ListenPostParametersCustomTopic,
    V1ListenPostParametersCustomTopicDict,
)
from ..models.unions.v1_listen_post_parameters_detect_language import (
    V1ListenPostParametersDetectLanguage,
    V1ListenPostParametersDetectLanguageDict,
)
from ..models.unions.v1_listen_post_parameters_extra import V1ListenPostParametersExtra, V1ListenPostParametersExtraDict
from ..models.unions.v1_listen_post_parameters_keywords import (
    V1ListenPostParametersKeywords,
    V1ListenPostParametersKeywordsDict,
)
from ..models.unions.v1_listen_post_parameters_model import V1ListenPostParametersModel, V1ListenPostParametersModelDict
from ..models.unions.v1_listen_post_parameters_redact import (
    V1ListenPostParametersRedact,
    V1ListenPostParametersRedactDict,
)
from ..models.unions.v1_listen_post_parameters_replace import (
    V1ListenPostParametersReplace,
    V1ListenPostParametersReplaceDict,
)
from ..models.unions.v1_listen_post_parameters_search import (
    V1ListenPostParametersSearch,
    V1ListenPostParametersSearchDict,
)
from ..models.unions.v1_listen_post_parameters_summarize import (
    V1ListenPostParametersSummarize,
    V1ListenPostParametersSummarizeDict,
)
from ..models.unions.v1_listen_post_parameters_tag import V1ListenPostParametersTag, V1ListenPostParametersTagDict
from ..models.unions.v1_listen_post_parameters_version import (
    V1ListenPostParametersVersion,
    V1ListenPostParametersVersionDict,
)
from ..server.server import Server


class ListenV1Media:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ListenV1MediaWithRawResponse(client, server, auth)

    def transcribe(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None,
        sentiment: bool | None = False,
        summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None,
        tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        detect_entities: bool | None = False,
        detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None,
        diarize: bool | None = False,
        diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None,
        dictation: bool | None = False,
        encoding: V1ListenPostParametersEncodingOrStr | None = None,
        filler_words: bool | None = False,
        keyterm: list[str] | None = None,
        keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None,
        language: str | None = "en",
        measurements: bool | None = False,
        model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None,
        multichannel: bool | None = False,
        numerals: bool | None = False,
        paragraphs: bool | None = False,
        profanity_filter: bool | None = False,
        punctuate: bool | None = False,
        redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None,
        replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None,
        search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None,
        smart_format: bool | None = False,
        utterances: bool | None = False,
        utt_split: float | None = 0.8,
        version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None,
        mip_opt_out: bool | None = False,
        body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListenV1MediaTranscribeResponse200:
        """Transcribe audio and video using Deepgram's speech-to-text REST API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            extra: Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
            sentiment: Recognizes the sentiment throughout a transcript or text
            summarize: Summarize content. For Listen API, supports string version option. For Read API, accepts boolean
                only.
            tag: Label your requests for the purpose of identification during usage reporting
            topics: Detect topics throughout a transcript or text
            custom_topic: Custom topics you want the model to detect within your input audio or text if present Submit
                up to ``100``.
            custom_topic_mode: Sets how the model will interpret strings submitted to the ``custom_topic`` param. When
                ``strict``, the model will only return topics submitted using the ``custom_topic`` param. When
                ``extended``, the model will return its own detected topics in addition to those submitted using the
                ``custom_topic`` param
            intents: Recognizes speaker intent throughout a transcript or text
            custom_intent: Custom intents you want the model to detect within your input audio if present
            custom_intent_mode: Sets how the model will interpret intents submitted to the ``custom_intent`` param. When
                ``strict``, the model will only return intents submitted using the ``custom_intent`` param. When
                ``extended``, the model will return its own detected intents in the ``custom_intent`` param.
            detect_entities: Identifies and extracts key entities from content in submitted audio
            detect_language: Identifies the dominant language spoken in submitted audio
            diarize: Deprecated: use ``diarize_model`` instead. Recognize speaker changes. Each word in the transcript
                will be assigned a speaker number starting at 0.
            diarize_model: Select and enable a specific diarization model version. Specifying this parameter enables
                diarization and selects the model — you do not need to also set the deprecated ``diarize=true``
                parameter. For batch, supported values are ``latest`` (currently v2), ``v1``, and ``v2``. For streaming,
                supported values are ``latest`` (currently v1) and ``v1``; ``v2`` returns a validation error on
                streaming requests.
            dictation: Dictation mode for controlling formatting with dictated speech
            encoding: Specify the expected encoding of your submitted audio
            filler_words: Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
            keyterm: Key term prompting improves recognition of specialized terminology and brands. Only compatible with
                Nova-3. ``keyterm`` accepts plain terms only. Unlike the legacy ``keywords`` feature, it does not
                support weights or intensifiers. Appending one (for example, ``keyterm=term:0.15``) is not rejected—the
                weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple
                separate keyterms, repeat the ``keyterm`` parameter (for example, ``keyterm=term1&keyterm=term2``). To
                boost one multi-word phrase as a single keyterm, join the words with ``%20`` or ``+`` (for example,
                ``keyterm=customer%20service``). Do not separate keyterms with commas, semicolons, or line breaks.
            keywords: Keywords can boost or suppress specialized terminology and brands
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            measurements: Spoken measurements will be converted to their corresponding abbreviations
            model: AI model used to process submitted audio
            multichannel: Transcribe each audio channel independently
            numerals: Numerals converts numbers from written format to numerical format
            paragraphs: Splits audio into paragraphs to improve transcript readability
            profanity_filter: Profanity Filter looks for recognized profanity and converts it to the nearest recognized
                non-profane word or removes it from the transcript completely
            punctuate: Add punctuation and capitalization to the transcript
            redact: Redaction removes sensitive information from your transcripts
            replace: Search for terms or phrases in submitted audio and replaces them
            search: Search for terms or phrases in submitted audio
            smart_format: Apply formatting to transcript output. When set to true, additional formatting will be applied
                to transcripts to improve readability
            utterances: Segments speech into meaningful semantic units
            utt_split: Seconds to wait before detecting a pause between words in submitted audio
            version: Version of an AI model to use
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            body: Transcribe an audio or video file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns either transcription results, or a request_id when using a callback.

        Raises:
            ApiError: Invalid Request ``error`` is ``ListenV1Response | RawError``."""
        return self._with_raw_response.transcribe(
            callback=callback,
            callback_method=callback_method,
            extra=extra,
            sentiment=sentiment,
            summarize=summarize,
            tag=tag,
            topics=topics,
            custom_topic=custom_topic,
            custom_topic_mode=custom_topic_mode,
            intents=intents,
            custom_intent=custom_intent,
            custom_intent_mode=custom_intent_mode,
            detect_entities=detect_entities,
            detect_language=detect_language,
            diarize=diarize,
            diarize_model=diarize_model,
            dictation=dictation,
            encoding=encoding,
            filler_words=filler_words,
            keyterm=keyterm,
            keywords=keywords,
            language=language,
            measurements=measurements,
            model=model,
            multichannel=multichannel,
            numerals=numerals,
            paragraphs=paragraphs,
            profanity_filter=profanity_filter,
            punctuate=punctuate,
            redact=redact,
            replace=replace,
            search=search,
            smart_format=smart_format,
            utterances=utterances,
            utt_split=utt_split,
            version=version,
            mip_opt_out=mip_opt_out,
            body=body,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ListenV1MediaWithRawResponse:
        return self._with_raw_response


class AsyncListenV1Media:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncListenV1MediaWithRawResponse(client, server, auth)

    async def transcribe(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None,
        sentiment: bool | None = False,
        summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None,
        tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        detect_entities: bool | None = False,
        detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None,
        diarize: bool | None = False,
        diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None,
        dictation: bool | None = False,
        encoding: V1ListenPostParametersEncodingOrStr | None = None,
        filler_words: bool | None = False,
        keyterm: list[str] | None = None,
        keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None,
        language: str | None = "en",
        measurements: bool | None = False,
        model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None,
        multichannel: bool | None = False,
        numerals: bool | None = False,
        paragraphs: bool | None = False,
        profanity_filter: bool | None = False,
        punctuate: bool | None = False,
        redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None,
        replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None,
        search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None,
        smart_format: bool | None = False,
        utterances: bool | None = False,
        utt_split: float | None = 0.8,
        version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None,
        mip_opt_out: bool | None = False,
        body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListenV1MediaTranscribeResponse200:
        """Transcribe audio and video using Deepgram's speech-to-text REST API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            extra: Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
            sentiment: Recognizes the sentiment throughout a transcript or text
            summarize: Summarize content. For Listen API, supports string version option. For Read API, accepts boolean
                only.
            tag: Label your requests for the purpose of identification during usage reporting
            topics: Detect topics throughout a transcript or text
            custom_topic: Custom topics you want the model to detect within your input audio or text if present Submit
                up to ``100``.
            custom_topic_mode: Sets how the model will interpret strings submitted to the ``custom_topic`` param. When
                ``strict``, the model will only return topics submitted using the ``custom_topic`` param. When
                ``extended``, the model will return its own detected topics in addition to those submitted using the
                ``custom_topic`` param
            intents: Recognizes speaker intent throughout a transcript or text
            custom_intent: Custom intents you want the model to detect within your input audio if present
            custom_intent_mode: Sets how the model will interpret intents submitted to the ``custom_intent`` param. When
                ``strict``, the model will only return intents submitted using the ``custom_intent`` param. When
                ``extended``, the model will return its own detected intents in the ``custom_intent`` param.
            detect_entities: Identifies and extracts key entities from content in submitted audio
            detect_language: Identifies the dominant language spoken in submitted audio
            diarize: Deprecated: use ``diarize_model`` instead. Recognize speaker changes. Each word in the transcript
                will be assigned a speaker number starting at 0.
            diarize_model: Select and enable a specific diarization model version. Specifying this parameter enables
                diarization and selects the model — you do not need to also set the deprecated ``diarize=true``
                parameter. For batch, supported values are ``latest`` (currently v2), ``v1``, and ``v2``. For streaming,
                supported values are ``latest`` (currently v1) and ``v1``; ``v2`` returns a validation error on
                streaming requests.
            dictation: Dictation mode for controlling formatting with dictated speech
            encoding: Specify the expected encoding of your submitted audio
            filler_words: Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
            keyterm: Key term prompting improves recognition of specialized terminology and brands. Only compatible with
                Nova-3. ``keyterm`` accepts plain terms only. Unlike the legacy ``keywords`` feature, it does not
                support weights or intensifiers. Appending one (for example, ``keyterm=term:0.15``) is not rejected—the
                weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple
                separate keyterms, repeat the ``keyterm`` parameter (for example, ``keyterm=term1&keyterm=term2``). To
                boost one multi-word phrase as a single keyterm, join the words with ``%20`` or ``+`` (for example,
                ``keyterm=customer%20service``). Do not separate keyterms with commas, semicolons, or line breaks.
            keywords: Keywords can boost or suppress specialized terminology and brands
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            measurements: Spoken measurements will be converted to their corresponding abbreviations
            model: AI model used to process submitted audio
            multichannel: Transcribe each audio channel independently
            numerals: Numerals converts numbers from written format to numerical format
            paragraphs: Splits audio into paragraphs to improve transcript readability
            profanity_filter: Profanity Filter looks for recognized profanity and converts it to the nearest recognized
                non-profane word or removes it from the transcript completely
            punctuate: Add punctuation and capitalization to the transcript
            redact: Redaction removes sensitive information from your transcripts
            replace: Search for terms or phrases in submitted audio and replaces them
            search: Search for terms or phrases in submitted audio
            smart_format: Apply formatting to transcript output. When set to true, additional formatting will be applied
                to transcripts to improve readability
            utterances: Segments speech into meaningful semantic units
            utt_split: Seconds to wait before detecting a pause between words in submitted audio
            version: Version of an AI model to use
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            body: Transcribe an audio or video file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns either transcription results, or a request_id when using a callback.

        Raises:
            ApiError: Invalid Request ``error`` is ``ListenV1Response | RawError``."""
        return (
            await self._with_raw_response.transcribe(
                callback=callback,
                callback_method=callback_method,
                extra=extra,
                sentiment=sentiment,
                summarize=summarize,
                tag=tag,
                topics=topics,
                custom_topic=custom_topic,
                custom_topic_mode=custom_topic_mode,
                intents=intents,
                custom_intent=custom_intent,
                custom_intent_mode=custom_intent_mode,
                detect_entities=detect_entities,
                detect_language=detect_language,
                diarize=diarize,
                diarize_model=diarize_model,
                dictation=dictation,
                encoding=encoding,
                filler_words=filler_words,
                keyterm=keyterm,
                keywords=keywords,
                language=language,
                measurements=measurements,
                model=model,
                multichannel=multichannel,
                numerals=numerals,
                paragraphs=paragraphs,
                profanity_filter=profanity_filter,
                punctuate=punctuate,
                redact=redact,
                replace=replace,
                search=search,
                smart_format=smart_format,
                utterances=utterances,
                utt_split=utt_split,
                version=version,
                mip_opt_out=mip_opt_out,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncListenV1MediaWithRawResponse:
        return self._with_raw_response


class ListenV1MediaWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def transcribe(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None,
        sentiment: bool | None = False,
        summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None,
        tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        detect_entities: bool | None = False,
        detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None,
        diarize: bool | None = False,
        diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None,
        dictation: bool | None = False,
        encoding: V1ListenPostParametersEncodingOrStr | None = None,
        filler_words: bool | None = False,
        keyterm: list[str] | None = None,
        keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None,
        language: str | None = "en",
        measurements: bool | None = False,
        model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None,
        multichannel: bool | None = False,
        numerals: bool | None = False,
        paragraphs: bool | None = False,
        profanity_filter: bool | None = False,
        punctuate: bool | None = False,
        redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None,
        replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None,
        search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None,
        smart_format: bool | None = False,
        utterances: bool | None = False,
        utt_split: float | None = 0.8,
        version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None,
        mip_opt_out: bool | None = False,
        body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListenV1MediaTranscribeResponse200, TranscribeErrorBody]:
        """Transcribe audio and video using Deepgram's speech-to-text REST API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            extra: Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
            sentiment: Recognizes the sentiment throughout a transcript or text
            summarize: Summarize content. For Listen API, supports string version option. For Read API, accepts boolean
                only.
            tag: Label your requests for the purpose of identification during usage reporting
            topics: Detect topics throughout a transcript or text
            custom_topic: Custom topics you want the model to detect within your input audio or text if present Submit
                up to ``100``.
            custom_topic_mode: Sets how the model will interpret strings submitted to the ``custom_topic`` param. When
                ``strict``, the model will only return topics submitted using the ``custom_topic`` param. When
                ``extended``, the model will return its own detected topics in addition to those submitted using the
                ``custom_topic`` param
            intents: Recognizes speaker intent throughout a transcript or text
            custom_intent: Custom intents you want the model to detect within your input audio if present
            custom_intent_mode: Sets how the model will interpret intents submitted to the ``custom_intent`` param. When
                ``strict``, the model will only return intents submitted using the ``custom_intent`` param. When
                ``extended``, the model will return its own detected intents in the ``custom_intent`` param.
            detect_entities: Identifies and extracts key entities from content in submitted audio
            detect_language: Identifies the dominant language spoken in submitted audio
            diarize: Deprecated: use ``diarize_model`` instead. Recognize speaker changes. Each word in the transcript
                will be assigned a speaker number starting at 0.
            diarize_model: Select and enable a specific diarization model version. Specifying this parameter enables
                diarization and selects the model — you do not need to also set the deprecated ``diarize=true``
                parameter. For batch, supported values are ``latest`` (currently v2), ``v1``, and ``v2``. For streaming,
                supported values are ``latest`` (currently v1) and ``v1``; ``v2`` returns a validation error on
                streaming requests.
            dictation: Dictation mode for controlling formatting with dictated speech
            encoding: Specify the expected encoding of your submitted audio
            filler_words: Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
            keyterm: Key term prompting improves recognition of specialized terminology and brands. Only compatible with
                Nova-3. ``keyterm`` accepts plain terms only. Unlike the legacy ``keywords`` feature, it does not
                support weights or intensifiers. Appending one (for example, ``keyterm=term:0.15``) is not rejected—the
                weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple
                separate keyterms, repeat the ``keyterm`` parameter (for example, ``keyterm=term1&keyterm=term2``). To
                boost one multi-word phrase as a single keyterm, join the words with ``%20`` or ``+`` (for example,
                ``keyterm=customer%20service``). Do not separate keyterms with commas, semicolons, or line breaks.
            keywords: Keywords can boost or suppress specialized terminology and brands
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            measurements: Spoken measurements will be converted to their corresponding abbreviations
            model: AI model used to process submitted audio
            multichannel: Transcribe each audio channel independently
            numerals: Numerals converts numbers from written format to numerical format
            paragraphs: Splits audio into paragraphs to improve transcript readability
            profanity_filter: Profanity Filter looks for recognized profanity and converts it to the nearest recognized
                non-profane word or removes it from the transcript completely
            punctuate: Add punctuation and capitalization to the transcript
            redact: Redaction removes sensitive information from your transcripts
            replace: Search for terms or phrases in submitted audio and replaces them
            search: Search for terms or phrases in submitted audio
            smart_format: Apply formatting to transcript output. When set to true, additional formatting will be applied
                to transcripts to improve readability
            utterances: Segments speech into meaningful semantic units
            utt_split: Seconds to wait before detecting a pause between words in submitted audio
            version: Version of an AI model to use
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            body: Transcribe an audio or video file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/listen"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None]("extra", extra),
                param[bool | None]("sentiment", sentiment),
                param[V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None](
                    "summarize", summarize
                ),
                param[V1ListenPostParametersTag | V1ListenPostParametersTagDict | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None](
                    "custom_topic", custom_topic
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("intents", intents),
                param[V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None](
                    "custom_intent", custom_intent
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_intent_mode", custom_intent_mode),
                param[bool | None]("detect_entities", detect_entities),
                param[V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None](
                    "detect_language", detect_language
                ),
                param[bool | None]("diarize", diarize),
                param[V1ListenPostParametersDiarizeModelOrStr | None]("diarize_model", diarize_model),
                param[bool | None]("dictation", dictation),
                param[V1ListenPostParametersEncodingOrStr | None]("encoding", encoding),
                param[bool | None]("filler_words", filler_words),
                param[list[str] | None]("keyterm", keyterm),
                param[V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None]("keywords", keywords),
                param[str | None]("language", language),
                param[bool | None]("measurements", measurements),
                param[V1ListenPostParametersModel | V1ListenPostParametersModelDict | None]("model", model),
                param[bool | None]("multichannel", multichannel),
                param[bool | None]("numerals", numerals),
                param[bool | None]("paragraphs", paragraphs),
                param[bool | None]("profanity_filter", profanity_filter),
                param[bool | None]("punctuate", punctuate),
                param[V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None]("redact", redact),
                param[V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None]("replace", replace),
                param[V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None]("search", search),
                param[bool | None]("smart_format", smart_format),
                param[bool | None]("utterances", utterances),
                param[float | None]("utt_split", utt_split),
                param[V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None]("version", version),
                param[bool | None]("mip_opt_out", mip_opt_out),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListenV1RequestUrl | ListenV1RequestUrlDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListenV1MediaTranscribeResponse200],
            error_mapper=transcribe_error_mapper,
            request_options=request_options,
        )


class AsyncListenV1MediaWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def transcribe(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        extra: V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None = None,
        sentiment: bool | None = False,
        summarize: V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None = None,
        tag: V1ListenPostParametersTag | V1ListenPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        detect_entities: bool | None = False,
        detect_language: V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None = None,
        diarize: bool | None = False,
        diarize_model: V1ListenPostParametersDiarizeModelOrStr | None = None,
        dictation: bool | None = False,
        encoding: V1ListenPostParametersEncodingOrStr | None = None,
        filler_words: bool | None = False,
        keyterm: list[str] | None = None,
        keywords: V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None = None,
        language: str | None = "en",
        measurements: bool | None = False,
        model: V1ListenPostParametersModel | V1ListenPostParametersModelDict | None = None,
        multichannel: bool | None = False,
        numerals: bool | None = False,
        paragraphs: bool | None = False,
        profanity_filter: bool | None = False,
        punctuate: bool | None = False,
        redact: V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None = None,
        replace: V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None = None,
        search: V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None = None,
        smart_format: bool | None = False,
        utterances: bool | None = False,
        utt_split: float | None = 0.8,
        version: V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None = None,
        mip_opt_out: bool | None = False,
        body: ListenV1RequestUrl | ListenV1RequestUrlDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListenV1MediaTranscribeResponse200, TranscribeErrorBody]:
        """Transcribe audio and video using Deepgram's speech-to-text REST API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            extra: Arbitrary key-value pairs that are attached to the API response for usage in downstream processing
            sentiment: Recognizes the sentiment throughout a transcript or text
            summarize: Summarize content. For Listen API, supports string version option. For Read API, accepts boolean
                only.
            tag: Label your requests for the purpose of identification during usage reporting
            topics: Detect topics throughout a transcript or text
            custom_topic: Custom topics you want the model to detect within your input audio or text if present Submit
                up to ``100``.
            custom_topic_mode: Sets how the model will interpret strings submitted to the ``custom_topic`` param. When
                ``strict``, the model will only return topics submitted using the ``custom_topic`` param. When
                ``extended``, the model will return its own detected topics in addition to those submitted using the
                ``custom_topic`` param
            intents: Recognizes speaker intent throughout a transcript or text
            custom_intent: Custom intents you want the model to detect within your input audio if present
            custom_intent_mode: Sets how the model will interpret intents submitted to the ``custom_intent`` param. When
                ``strict``, the model will only return intents submitted using the ``custom_intent`` param. When
                ``extended``, the model will return its own detected intents in the ``custom_intent`` param.
            detect_entities: Identifies and extracts key entities from content in submitted audio
            detect_language: Identifies the dominant language spoken in submitted audio
            diarize: Deprecated: use ``diarize_model`` instead. Recognize speaker changes. Each word in the transcript
                will be assigned a speaker number starting at 0.
            diarize_model: Select and enable a specific diarization model version. Specifying this parameter enables
                diarization and selects the model — you do not need to also set the deprecated ``diarize=true``
                parameter. For batch, supported values are ``latest`` (currently v2), ``v1``, and ``v2``. For streaming,
                supported values are ``latest`` (currently v1) and ``v1``; ``v2`` returns a validation error on
                streaming requests.
            dictation: Dictation mode for controlling formatting with dictated speech
            encoding: Specify the expected encoding of your submitted audio
            filler_words: Filler Words can help transcribe interruptions in your audio, like "uh" and "um"
            keyterm: Key term prompting improves recognition of specialized terminology and brands. Only compatible with
                Nova-3. ``keyterm`` accepts plain terms only. Unlike the legacy ``keywords`` feature, it does not
                support weights or intensifiers. Appending one (for example, ``keyterm=term:0.15``) is not rejected—the
                weight is silently ignored and the entire value is treated as a literal keyterm. To boost multiple
                separate keyterms, repeat the ``keyterm`` parameter (for example, ``keyterm=term1&keyterm=term2``). To
                boost one multi-word phrase as a single keyterm, join the words with ``%20`` or ``+`` (for example,
                ``keyterm=customer%20service``). Do not separate keyterms with commas, semicolons, or line breaks.
            keywords: Keywords can boost or suppress specialized terminology and brands
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            measurements: Spoken measurements will be converted to their corresponding abbreviations
            model: AI model used to process submitted audio
            multichannel: Transcribe each audio channel independently
            numerals: Numerals converts numbers from written format to numerical format
            paragraphs: Splits audio into paragraphs to improve transcript readability
            profanity_filter: Profanity Filter looks for recognized profanity and converts it to the nearest recognized
                non-profane word or removes it from the transcript completely
            punctuate: Add punctuation and capitalization to the transcript
            redact: Redaction removes sensitive information from your transcripts
            replace: Search for terms or phrases in submitted audio and replaces them
            search: Search for terms or phrases in submitted audio
            smart_format: Apply formatting to transcript output. When set to true, additional formatting will be applied
                to transcripts to improve readability
            utterances: Segments speech into meaningful semantic units
            utt_split: Seconds to wait before detecting a pause between words in submitted audio
            version: Version of an AI model to use
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            body: Transcribe an audio or video file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/listen"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[V1ListenPostParametersExtra | V1ListenPostParametersExtraDict | None]("extra", extra),
                param[bool | None]("sentiment", sentiment),
                param[V1ListenPostParametersSummarize | V1ListenPostParametersSummarizeDict | None](
                    "summarize", summarize
                ),
                param[V1ListenPostParametersTag | V1ListenPostParametersTagDict | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[V1ListenPostParametersCustomTopic | V1ListenPostParametersCustomTopicDict | None](
                    "custom_topic", custom_topic
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("intents", intents),
                param[V1ListenPostParametersCustomIntent | V1ListenPostParametersCustomIntentDict | None](
                    "custom_intent", custom_intent
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_intent_mode", custom_intent_mode),
                param[bool | None]("detect_entities", detect_entities),
                param[V1ListenPostParametersDetectLanguage | V1ListenPostParametersDetectLanguageDict | None](
                    "detect_language", detect_language
                ),
                param[bool | None]("diarize", diarize),
                param[V1ListenPostParametersDiarizeModelOrStr | None]("diarize_model", diarize_model),
                param[bool | None]("dictation", dictation),
                param[V1ListenPostParametersEncodingOrStr | None]("encoding", encoding),
                param[bool | None]("filler_words", filler_words),
                param[list[str] | None]("keyterm", keyterm),
                param[V1ListenPostParametersKeywords | V1ListenPostParametersKeywordsDict | None]("keywords", keywords),
                param[str | None]("language", language),
                param[bool | None]("measurements", measurements),
                param[V1ListenPostParametersModel | V1ListenPostParametersModelDict | None]("model", model),
                param[bool | None]("multichannel", multichannel),
                param[bool | None]("numerals", numerals),
                param[bool | None]("paragraphs", paragraphs),
                param[bool | None]("profanity_filter", profanity_filter),
                param[bool | None]("punctuate", punctuate),
                param[V1ListenPostParametersRedact | V1ListenPostParametersRedactDict | None]("redact", redact),
                param[V1ListenPostParametersReplace | V1ListenPostParametersReplaceDict | None]("replace", replace),
                param[V1ListenPostParametersSearch | V1ListenPostParametersSearchDict | None]("search", search),
                param[bool | None]("smart_format", smart_format),
                param[bool | None]("utterances", utterances),
                param[float | None]("utt_split", utt_split),
                param[V1ListenPostParametersVersion | V1ListenPostParametersVersionDict | None]("version", version),
                param[bool | None]("mip_opt_out", mip_opt_out),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListenV1RequestUrl | ListenV1RequestUrlDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListenV1MediaTranscribeResponse200],
            error_mapper=transcribe_error_mapper,
            request_options=request_options,
        )
