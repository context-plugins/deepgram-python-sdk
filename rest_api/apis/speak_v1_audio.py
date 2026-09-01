from __future__ import annotations

from typing import Any
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
from ..errors.generate_error import GenerateErrorBody, generate_error_mapper
from ..models.enums.v1_listen_post_parameters_callback_method import V1ListenPostParametersCallbackMethodOrStr
from ..models.enums.v1_speak_post_parameters_model import V1SpeakPostParametersModelOrStr
from ..models.speak_v1_request import SpeakV1Request, SpeakV1RequestDict
from ..models.unions.v1_speak_post_parameters_bit_rate import (
    V1SpeakPostParametersBitRate,
    V1SpeakPostParametersBitRateDict,
)
from ..models.unions.v1_speak_post_parameters_container import (
    V1SpeakPostParametersContainer,
    V1SpeakPostParametersContainerDict,
)
from ..models.unions.v1_speak_post_parameters_encoding import (
    V1SpeakPostParametersEncoding,
    V1SpeakPostParametersEncodingDict,
)
from ..models.unions.v1_speak_post_parameters_sample_rate import (
    V1SpeakPostParametersSampleRate,
    V1SpeakPostParametersSampleRateDict,
)
from ..models.unions.v1_speak_post_parameters_tag import V1SpeakPostParametersTag, V1SpeakPostParametersTagDict
from ..server.server import Server


class SpeakV1Audio:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SpeakV1AudioWithRawResponse(client, server, auth)

    def generate(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        mip_opt_out: bool | None = False,
        tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None,
        bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None,
        container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None,
        encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None,
        model: V1SpeakPostParametersModelOrStr | None = None,
        sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None,
        speed: float | None = 1.0,
        body: SpeakV1Request | SpeakV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Convert text into natural-sounding speech using Deepgram's TTS REST API

        Args:
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
            model: AI model used to process submitted text
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            speed: Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody
                and voice quality. Not yet supported in all languages.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful text-to-speech transformation

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.generate(
            callback=callback,
            callback_method=callback_method,
            mip_opt_out=mip_opt_out,
            tag=tag,
            bit_rate=bit_rate,
            container=container,
            encoding=encoding,
            model=model,
            sample_rate=sample_rate,
            speed=speed,
            body=body,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> SpeakV1AudioWithRawResponse:
        return self._with_raw_response


class AsyncSpeakV1Audio:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSpeakV1AudioWithRawResponse(client, server, auth)

    async def generate(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        mip_opt_out: bool | None = False,
        tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None,
        bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None,
        container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None,
        encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None,
        model: V1SpeakPostParametersModelOrStr | None = None,
        sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None,
        speed: float | None = 1.0,
        body: SpeakV1Request | SpeakV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Convert text into natural-sounding speech using Deepgram's TTS REST API

        Args:
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
            model: AI model used to process submitted text
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            speed: Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody
                and voice quality. Not yet supported in all languages.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful text-to-speech transformation

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.generate(
                callback=callback,
                callback_method=callback_method,
                mip_opt_out=mip_opt_out,
                tag=tag,
                bit_rate=bit_rate,
                container=container,
                encoding=encoding,
                model=model,
                sample_rate=sample_rate,
                speed=speed,
                body=body,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSpeakV1AudioWithRawResponse:
        return self._with_raw_response


class SpeakV1AudioWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def generate(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        mip_opt_out: bool | None = False,
        tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None,
        bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None,
        container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None,
        encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None,
        model: V1SpeakPostParametersModelOrStr | None = None,
        sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None,
        speed: float | None = 1.0,
        body: SpeakV1Request | SpeakV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GenerateErrorBody]:
        """Convert text into natural-sounding speech using Deepgram's TTS REST API

        Args:
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
            model: AI model used to process submitted text
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            speed: Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody
                and voice quality. Not yet supported in all languages.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/speak"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("mip_opt_out", mip_opt_out),
                param[V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None]("tag", tag),
                param[V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None]("bit_rate", bit_rate),
                param[V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None](
                    "container", container
                ),
                param[V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None]("encoding", encoding),
                param[V1SpeakPostParametersModelOrStr | None]("model", model),
                param[V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None](
                    "sample_rate", sample_rate
                ),
                param[float | None]("speed", speed),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SpeakV1Request | SpeakV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=generate_error_mapper,
            request_options=request_options,
        )


class AsyncSpeakV1AudioWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def generate(
        self,
        *,
        callback: str | None = None,
        callback_method: V1ListenPostParametersCallbackMethodOrStr | None = None,
        mip_opt_out: bool | None = False,
        tag: V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None = None,
        bit_rate: V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None = None,
        container: V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None = None,
        encoding: V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None = None,
        model: V1SpeakPostParametersModelOrStr | None = None,
        sample_rate: V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None = None,
        speed: float | None = 1.0,
        body: SpeakV1Request | SpeakV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GenerateErrorBody]:
        """Convert text into natural-sounding speech using Deepgram's TTS REST API

        Args:
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
            model: AI model used to process submitted text
            sample_rate: Sample Rate specifies the sample rate for the output audio. Based on the encoding, different
                sample rates are supported. For some encodings, the sample rate is not configurable
            speed: Speaking rate multiplier that adjusts the pace of generated speech while preserving natural prosody
                and voice quality. Not yet supported in all languages.
            body: Transform text to speech
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/speak"),
            query_params=[
                param[str | None]("callback", callback),
                param[V1ListenPostParametersCallbackMethodOrStr | None]("callback_method", callback_method),
                param[bool | None]("mip_opt_out", mip_opt_out),
                param[V1SpeakPostParametersTag | V1SpeakPostParametersTagDict | None]("tag", tag),
                param[V1SpeakPostParametersBitRate | V1SpeakPostParametersBitRateDict | None]("bit_rate", bit_rate),
                param[V1SpeakPostParametersContainer | V1SpeakPostParametersContainerDict | None](
                    "container", container
                ),
                param[V1SpeakPostParametersEncoding | V1SpeakPostParametersEncodingDict | None]("encoding", encoding),
                param[V1SpeakPostParametersModelOrStr | None]("model", model),
                param[V1SpeakPostParametersSampleRate | V1SpeakPostParametersSampleRateDict | None](
                    "sample_rate", sample_rate
                ),
                param[float | None]("speed", speed),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SpeakV1Request | SpeakV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=generate_error_mapper,
            request_options=request_options,
        )
