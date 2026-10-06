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
from ..errors.get4_error import Get4ErrorBody, get4_error_mapper
from ..errors.list5_error import List5ErrorBody, list5_error_mapper
from ..models.list_models_v1_response import ListModelsV1Response
from ..models.unions.get_model_v1_response import GetModelV1Response
from ..server.server import Server


class ManageV1ProjectsModels:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsModelsWithRawResponse(client, server, auth)

    def get4(
        self, project_id: str, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetModelV1Response:
        """Returns metadata for a specific model

        Args:
            project_id: The unique identifier of the project
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A model object that can be either STT or TTS

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get4(project_id, model_id, request_options=request_options).unwrap()

    def list5(
        self,
        project_id: str,
        *,
        include_outdated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListModelsV1Response:
        """Returns metadata on all the latest models that a specific project has access to, including non-public models

        Args:
            project_id: The unique identifier of the project
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list5(
            project_id, include_outdated=include_outdated, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsModelsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsModels:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsModelsWithRawResponse(client, server, auth)

    async def get4(
        self, project_id: str, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetModelV1Response:
        """Returns metadata for a specific model

        Args:
            project_id: The unique identifier of the project
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A model object that can be either STT or TTS

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get4(project_id, model_id, request_options=request_options)).unwrap()

    async def list5(
        self,
        project_id: str,
        *,
        include_outdated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListModelsV1Response:
        """Returns metadata on all the latest models that a specific project has access to, including non-public models

        Args:
            project_id: The unique identifier of the project
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list5(
                project_id, include_outdated=include_outdated, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsModelsWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsModelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get4(
        self, project_id: str, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetModelV1Response, Get4ErrorBody]:
        """Returns metadata for a specific model

        Args:
            project_id: The unique identifier of the project
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/models/{model_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("model_id", model_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetModelV1Response],
            error_mapper=get4_error_mapper,
            request_options=request_options,
        )

    def list5(
        self,
        project_id: str,
        *,
        include_outdated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListModelsV1Response, List5ErrorBody]:
        """Returns metadata on all the latest models that a specific project has access to, including non-public models

        Args:
            project_id: The unique identifier of the project
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/models"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[bool | None]("include_outdated", include_outdated)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListModelsV1Response],
            error_mapper=list5_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsModelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get4(
        self, project_id: str, model_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetModelV1Response, Get4ErrorBody]:
        """Returns metadata for a specific model

        Args:
            project_id: The unique identifier of the project
            model_id: The specific UUID of the model
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/models/{model_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("model_id", model_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[GetModelV1Response],
            error_mapper=get4_error_mapper,
            request_options=request_options,
        )

    async def list5(
        self,
        project_id: str,
        *,
        include_outdated: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListModelsV1Response, List5ErrorBody]:
        """Returns metadata on all the latest models that a specific project has access to, including non-public models

        Args:
            project_id: The unique identifier of the project
            include_outdated: returns non-latest versions of models
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/models"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[bool | None]("include_outdated", include_outdated)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListModelsV1Response],
            error_mapper=list5_error_mapper,
            request_options=request_options,
        )
