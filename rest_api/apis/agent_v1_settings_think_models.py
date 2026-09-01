from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder
from ..errors.list_error import ListErrorBody, list_error_mapper
from ..models.agent_think_models_v1_response import AgentThinkModelsV1Response
from ..server.server import Server


class AgentV1SettingsThinkModels:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AgentV1SettingsThinkModelsWithRawResponse(client, server, auth)

    def list_(self, *, request_options: RequestOptionsOrDict | None = None) -> AgentThinkModelsV1Response:
        """Retrieves the available think models that can be used for AI agent processing

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of available think models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list_(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AgentV1SettingsThinkModelsWithRawResponse:
        return self._with_raw_response


class AsyncAgentV1SettingsThinkModels:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAgentV1SettingsThinkModelsWithRawResponse(client, server, auth)

    async def list_(self, *, request_options: RequestOptionsOrDict | None = None) -> AgentThinkModelsV1Response:
        """Retrieves the available think models that can be used for AI agent processing

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of available think models

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list_(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAgentV1SettingsThinkModelsWithRawResponse:
        return self._with_raw_response


class AgentV1SettingsThinkModelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentThinkModelsV1Response, ListErrorBody]:
        """Retrieves the available think models that can be used for AI agent processing

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/settings/think/models"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentThinkModelsV1Response],
            error_mapper=list_error_mapper,
            request_options=request_options,
        )


class AsyncAgentV1SettingsThinkModelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentThinkModelsV1Response, ListErrorBody]:
        """Retrieves the available think models that can be used for AI agent processing

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/agent/settings/think/models"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentThinkModelsV1Response],
            error_mapper=list_error_mapper,
            request_options=request_options,
        )
