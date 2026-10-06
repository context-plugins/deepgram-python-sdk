from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
)
from ..errors.get5_error import Get5ErrorBody, get5_error_mapper
from ..errors.list6_error import List6ErrorBody, list6_error_mapper
from ..models.list_models_v1_response import ListModelsV1Response
from ..models.unions.get_model_v1_response import GetModelV1Response
from ..server.server import Server


class ManageV1Models:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ModelsWithRawResponse(client, server, auth)

    def get5(self, model_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetModelV1Response:
        """Returns metadata for a specific public model

        Args:
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A model object that can be either STT or TTS

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get5(model_id, request_options=request_options).unwrap()

    def list6(
        self, *, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListModelsV1Response:
        """Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

        Args:
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list6(
            include_outdated=include_outdated, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ModelsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1Models:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ModelsWithRawResponse(client, server, auth)

    async def get5(self, model_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetModelV1Response:
        """Returns metadata for a specific public model

        Args:
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A model object that can be either STT or TTS

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get5(model_id, request_options=request_options)).unwrap()

    async def list6(
        self, *, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListModelsV1Response:
        """Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

        Args:
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list6(include_outdated=include_outdated, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ModelsWithRawResponse:
        return self._with_raw_response


class ManageV1ModelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get5(
        self, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetModelV1Response, Get5ErrorBody]:
        """Returns metadata for a specific public model

        Args:
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/models/{model_id}"),
            path_params=[param[str]("model_id", model_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetModelV1Response],
            error_mapper=get5_error_mapper,
            request_options=request_options,
        )

    def list6(
        self, *, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListModelsV1Response, List6ErrorBody]:
        """Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

        Args:
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/models"),
            query_params=[param[bool | None]("include_outdated", include_outdated)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListModelsV1Response],
            error_mapper=list6_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ModelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get5(
        self, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetModelV1Response, Get5ErrorBody]:
        """Returns metadata for a specific public model

        Args:
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/models/{model_id}"),
            path_params=[param[str]("model_id", model_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[GetModelV1Response],
            error_mapper=get5_error_mapper,
            request_options=request_options,
        )

    async def list6(
        self, *, include_outdated: bool | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListModelsV1Response, List6ErrorBody]:
        """Returns metadata on all the latest public models. To retrieve custom models, use Get Project Models.

        Args:
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/models"),
            query_params=[param[bool | None]("include_outdated", include_outdated)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListModelsV1Response],
            error_mapper=list6_error_mapper,
            request_options=request_options,
        )
