from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
)
from ..errors.generate2_error import Generate2ErrorBody, generate2_error_mapper
from ..models.enums.v1_listen_post_parameters_callback_method import (
    V1ListenPostParametersCallbackMethod,
    V1ListenPostParametersCallbackMethodOrStr,
)
from ..models.enums.v2_speak_post_parameters_priority import V2SpeakPostParametersPriorityOrStr
from ..models.speak_v2_accepted_response import SpeakV2AcceptedResponse
from ..models.speak_v2_request import SpeakV2Request, SpeakV2RequestDict
from ..models.unions.v2_speak_post_parameters_bit_rate import (
    V2SpeakPostParametersBitRate,
    V2SpeakPostParametersBitRateDict,
)
from ..models.unions.v2_speak_post_parameters_container import (
    V2SpeakPostParametersContainer,
    V2SpeakPostParametersContainerDict,
)
from ..models.unions.v2_speak_post_parameters_encoding import (
    V2SpeakPostParametersEncoding,
    V2SpeakPostParametersEncodingDict,
)
from ..models.unions.v2_speak_post_parameters_sample_rate import (
    V2SpeakPostParametersSampleRate,
    V2SpeakPostParametersSampleRateDict,
)
from ..models.unions.v2_speak_post_parameters_tag import V2SpeakPostParametersTag, V2SpeakPostParametersTagDict
from ..server.server import Server


class SpeakV2Audio:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SpeakV2AudioWithRawResponse(client, server, auth)

    def generate2(
        self,
        model: str,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST,
        mip_opt_out: bool | None = False,
        tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None,
        bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None,
        container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None,
        encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None,
        sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None,
        priority: V2SpeakPostParametersPriorityOrStr | None = None,
        body: SpeakV2Request | SpeakV2RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SpeakV2AcceptedResponse:
        """Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API.
        Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up
        front and you don't need incremental playback or interruption.

        Args:
            model: Flux TTS model used to synthesize the submitted text, in the form ``flux-{voice}-{language}`` (for
                example, ``flux-alexis-en``). Required; unlike the v1 (Aura) endpoint there is no default and only flux
                models are accepted. English-only at launch.
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            tag: Label your requests for the purpose of identification during usage reporting
            bit_rate: The bitrate of the audio in bits per second. Choose from predefined ranges or specific values
                based on the encoding type.
            container: Container specifies the file format wrapper for the output audio. The available options depend on
                the encoding type.
            encoding: Encoding allows you to specify the expected encoding of your audio output
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            priority: Processing priority for asynchronous (callback) requests. The only supported value is low.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the synthesized audio in the requested encoding as a binary stream. When a ``callback`` URL is
            supplied, the request is processed asynchronously and the response body is instead a JSON acknowledgement
            (Content-Type ``application/json``) of the form {"request_id": "..."}, with the audio delivered to the
            callback URL. Because this endpoint is typed as a binary audio stream, SDK callers that set ``callback``
            receive this JSON acknowledgement through the audio byte iterator as raw bytes and must join the chunks and
            parse ``request_id`` themselves.

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.generate2(
            model,
            callback=callback,
            callback_method=callback_method,
            mip_opt_out=mip_opt_out,
            tag=tag,
            bit_rate=bit_rate,
            container=container,
            encoding=encoding,
            sample_rate=sample_rate,
            priority=priority,
            body=body,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SpeakV2AudioWithRawResponse:
        return self._with_raw_response


class AsyncSpeakV2Audio:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSpeakV2AudioWithRawResponse(client, server, auth)

    async def generate2(
        self,
        model: str,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST,
        mip_opt_out: bool | None = False,
        tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None,
        bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None,
        container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None,
        encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None,
        sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None,
        priority: V2SpeakPostParametersPriorityOrStr | None = None,
        body: SpeakV2Request | SpeakV2RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SpeakV2AcceptedResponse:
        """Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API.
        Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up
        front and you don't need incremental playback or interruption.

        Args:
            model: Flux TTS model used to synthesize the submitted text, in the form ``flux-{voice}-{language}`` (for
                example, ``flux-alexis-en``). Required; unlike the v1 (Aura) endpoint there is no default and only flux
                models are accepted. English-only at launch.
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            tag: Label your requests for the purpose of identification during usage reporting
            bit_rate: The bitrate of the audio in bits per second. Choose from predefined ranges or specific values
                based on the encoding type.
            container: Container specifies the file format wrapper for the output audio. The available options depend on
                the encoding type.
            encoding: Encoding allows you to specify the expected encoding of your audio output
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            priority: Processing priority for asynchronous (callback) requests. The only supported value is low.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the synthesized audio in the requested encoding as a binary stream. When a ``callback`` URL is
            supplied, the request is processed asynchronously and the response body is instead a JSON acknowledgement
            (Content-Type ``application/json``) of the form {"request_id": "..."}, with the audio delivered to the
            callback URL. Because this endpoint is typed as a binary audio stream, SDK callers that set ``callback``
            receive this JSON acknowledgement through the audio byte iterator as raw bytes and must join the chunks and
            parse ``request_id`` themselves.

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.generate2(
                model,
                callback=callback,
                callback_method=callback_method,
                mip_opt_out=mip_opt_out,
                tag=tag,
                bit_rate=bit_rate,
                container=container,
                encoding=encoding,
                sample_rate=sample_rate,
                priority=priority,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSpeakV2AudioWithRawResponse:
        return self._with_raw_response


class SpeakV2AudioWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def generate2(
        self,
        model: str,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST,
        mip_opt_out: bool | None = False,
        tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None,
        bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None,
        container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None,
        encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None,
        sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None,
        priority: V2SpeakPostParametersPriorityOrStr | None = None,
        body: SpeakV2Request | SpeakV2RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SpeakV2AcceptedResponse, Generate2ErrorBody]:
        """Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API.
        Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up
        front and you don't need incremental playback or interruption.

        Args:
            model: Flux TTS model used to synthesize the submitted text, in the form ``flux-{voice}-{language}`` (for
                example, ``flux-alexis-en``). Required; unlike the v1 (Aura) endpoint there is no default and only flux
                models are accepted. English-only at launch.
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            tag: Label your requests for the purpose of identification during usage reporting
            bit_rate: The bitrate of the audio in bits per second. Choose from predefined ranges or specific values
                based on the encoding type.
            container: Container specifies the file format wrapper for the output audio. The available options depend on
                the encoding type.
            encoding: Encoding allows you to specify the expected encoding of your audio output
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            priority: Processing priority for asynchronous (callback) requests. The only supported value is low.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/speak"),
            query_params=[
                param[str]("model", model),
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("mip_opt_out", mip_opt_out),
                param[V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None]("tag", tag),
                param[V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None]("bit_rate", bit_rate),
                param[V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None](
                    "container", container
                ),
                param[V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None]("encoding", encoding),
                param[V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None](
                    "sample_rate", sample_rate
                ),
                param[V2SpeakPostParametersPriorityOrStr | None]("priority", priority),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SpeakV2Request | SpeakV2RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[SpeakV2AcceptedResponse],
            error_mapper=generate2_error_mapper,
            request_options=request_options,
        )


class AsyncSpeakV2AudioWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def generate2(
        self,
        model: str,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = V1ListenPostParametersCallbackMethod.POST,
        mip_opt_out: bool | None = False,
        tag: V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None = None,
        bit_rate: V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None = None,
        container: V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None = None,
        encoding: V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None = None,
        sample_rate: V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None = None,
        priority: V2SpeakPostParametersPriorityOrStr | None = None,
        body: SpeakV2Request | SpeakV2RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SpeakV2AcceptedResponse, Generate2ErrorBody]:
        """Synthesize a complete block of text into a single audio response using Deepgram's Flux TTS batch (REST) API.
        Use this for pre-rendering fixed audio (IVR prompts, notifications, narration) where the whole text is known up
        front and you don't need incremental playback or interruption.

        Args:
            model: Flux TTS model used to synthesize the submitted text, in the form ``flux-{voice}-{language}`` (for
                example, ``flux-alexis-en``). Required; unlike the v1 (Aura) endpoint there is no default and only flux
                models are accepted. English-only at launch.
            callback: URL to which we'll make the callback request
            callback_method: HTTP method by which the callback request will be made
            mip_opt_out: Opts out requests from the Deepgram Model Improvement Program. Refer to our Docs for pricing
                impacts before setting this to true. https://dpgr.am/deepgram-mip
            tag: Label your requests for the purpose of identification during usage reporting
            bit_rate: The bitrate of the audio in bits per second. Choose from predefined ranges or specific values
                based on the encoding type.
            container: Container specifies the file format wrapper for the output audio. The available options depend on
                the encoding type.
            encoding: Encoding allows you to specify the expected encoding of your audio output
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            priority: Processing priority for asynchronous (callback) requests. The only supported value is low.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/speak"),
            query_params=[
                param[str]("model", model),
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("mip_opt_out", mip_opt_out),
                param[V2SpeakPostParametersTag | V2SpeakPostParametersTagDict | None]("tag", tag),
                param[V2SpeakPostParametersBitRate | V2SpeakPostParametersBitRateDict | None]("bit_rate", bit_rate),
                param[V2SpeakPostParametersContainer | V2SpeakPostParametersContainerDict | None](
                    "container", container
                ),
                param[V2SpeakPostParametersEncoding | V2SpeakPostParametersEncodingDict | None]("encoding", encoding),
                param[V2SpeakPostParametersSampleRate | V2SpeakPostParametersSampleRateDict | None](
                    "sample_rate", sample_rate
                ),
                param[V2SpeakPostParametersPriorityOrStr | None]("priority", priority),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SpeakV2Request | SpeakV2RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[SpeakV2AcceptedResponse],
            error_mapper=generate2_error_mapper,
            request_options=request_options,
        )
