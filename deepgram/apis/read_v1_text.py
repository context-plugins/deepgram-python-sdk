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
from ..errors.analyze_error import AnalyzeErrorBody, analyze_error_mapper
from ..models.enums.v1_listen_post_parameters_callback_method import V1ListenPostParametersCallbackMethodOrStr
from ..models.enums.v1_listen_post_parameters_custom_topic_mode import V1ListenPostParametersCustomTopicModeOrStr
from ..models.read_v1_response import ReadV1Response
from ..models.unions.read_v1_request import ReadV1Request, ReadV1RequestDict
from ..models.unions.v1_read_post_parameters_custom_intent import (
    V1ReadPostParametersCustomIntent,
    V1ReadPostParametersCustomIntentDict,
)
from ..models.unions.v1_read_post_parameters_custom_topic import (
    V1ReadPostParametersCustomTopic,
    V1ReadPostParametersCustomTopicDict,
)
from ..models.unions.v1_read_post_parameters_summarize import (
    V1ReadPostParametersSummarize,
    V1ReadPostParametersSummarizeDict,
)
from ..models.unions.v1_read_post_parameters_tag import V1ReadPostParametersTag, V1ReadPostParametersTagDict
from ..server.server import Server


class ReadV1Text:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReadV1TextWithRawResponse(client, server, auth)

    def analyze(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        sentiment: bool | None = False,
        summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None,
        tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        language: str | None = "en",
        body: ReadV1Request | ReadV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReadV1Response:
        """Analyze text content using Deepgrams text analysis API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
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
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            body: Analyze a text file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful text analysis

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.analyze(
            callback=callback,
            callback_method=callback_method,
            sentiment=sentiment,
            summarize=summarize,
            tag=tag,
            topics=topics,
            custom_topic=custom_topic,
            custom_topic_mode=custom_topic_mode,
            intents=intents,
            custom_intent=custom_intent,
            custom_intent_mode=custom_intent_mode,
            language=language,
            body=body,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ReadV1TextWithRawResponse:
        return self._with_raw_response


class AsyncReadV1Text:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReadV1TextWithRawResponse(client, server, auth)

    async def analyze(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        sentiment: bool | None = False,
        summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None,
        tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        language: str | None = "en",
        body: ReadV1Request | ReadV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReadV1Response:
        """Analyze text content using Deepgrams text analysis API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
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
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            body: Analyze a text file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful text analysis

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.analyze(
                callback=callback,
                callback_method=callback_method,
                sentiment=sentiment,
                summarize=summarize,
                tag=tag,
                topics=topics,
                custom_topic=custom_topic,
                custom_topic_mode=custom_topic_mode,
                intents=intents,
                custom_intent=custom_intent,
                custom_intent_mode=custom_intent_mode,
                language=language,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncReadV1TextWithRawResponse:
        return self._with_raw_response


class ReadV1TextWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def analyze(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        sentiment: bool | None = False,
        summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None,
        tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        language: str | None = "en",
        body: ReadV1Request | ReadV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReadV1Response, AnalyzeErrorBody]:
        """Analyze text content using Deepgrams text analysis API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
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
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            body: Analyze a text file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/read"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("sentiment", sentiment),
                param[V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None]("summarize", summarize),
                param[V1ReadPostParametersTag | V1ReadPostParametersTagDict | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None](
                    "custom_topic", custom_topic
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("intents", intents),
                param[V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None](
                    "custom_intent", custom_intent
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_intent_mode", custom_intent_mode),
                param[str | None]("language", language),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReadV1Request | ReadV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ReadV1Response],
            error_mapper=analyze_error_mapper,
            request_options=request_options,
        )


class AsyncReadV1TextWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def analyze(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        sentiment: bool | None = False,
        summarize: V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None = None,
        tag: V1ReadPostParametersTag | V1ReadPostParametersTagDict | None = None,
        topics: bool | None = False,
        custom_topic: V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None = None,
        custom_topic_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        intents: bool | None = False,
        custom_intent: V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None = None,
        custom_intent_mode: V1ListenPostParametersCustomTopicModeOrStr | None = None,
        language: str | None = "en",
        body: ReadV1Request | ReadV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReadV1Response, AnalyzeErrorBody]:
        """Analyze text content using Deepgrams text analysis API

        Args:
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
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
            language: The `BCP-47 language tag <https://tools.ietf.org/html/bcp47>`__ that hints at the primary spoken
                language. Depending on the Model and API endpoint you choose only certain languages are available
            body: Analyze a text file
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/read"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("sentiment", sentiment),
                param[V1ReadPostParametersSummarize | V1ReadPostParametersSummarizeDict | None]("summarize", summarize),
                param[V1ReadPostParametersTag | V1ReadPostParametersTagDict | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[V1ReadPostParametersCustomTopic | V1ReadPostParametersCustomTopicDict | None](
                    "custom_topic", custom_topic
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("intents", intents),
                param[V1ReadPostParametersCustomIntent | V1ReadPostParametersCustomIntentDict | None](
                    "custom_intent", custom_intent
                ),
                param[V1ListenPostParametersCustomTopicModeOrStr | None]("custom_intent_mode", custom_intent_mode),
                param[str | None]("language", language),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReadV1Request | ReadV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ReadV1Response],
            error_mapper=analyze_error_mapper,
            request_options=request_options,
        )
