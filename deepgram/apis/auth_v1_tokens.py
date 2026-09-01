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
from ..errors.grant_error import GrantErrorBody, grant_error_mapper
from ..models.grant_v1_request import GrantV1Request, GrantV1RequestDict
from ..models.grant_v1_response import GrantV1Response
from ..server.server import Server


class AuthV1Tokens:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthV1TokensWithRawResponse(client, server, auth)

    def grant(
        self,
        *,
        body: GrantV1Request | GrantV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GrantV1Response:
        """Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for
        core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint
        will not work with the Manage APIs.

        Args:
            body: Time to live settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Grant response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.grant(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AuthV1TokensWithRawResponse:
        return self._with_raw_response


class AsyncAuthV1Tokens:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthV1TokensWithRawResponse(client, server, auth)

    async def grant(
        self,
        *,
        body: GrantV1Request | GrantV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GrantV1Response:
        """Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for
        core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint
        will not work with the Manage APIs.

        Args:
            body: Time to live settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Grant response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.grant(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncAuthV1TokensWithRawResponse:
        return self._with_raw_response


class AuthV1TokensWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def grant(
        self,
        *,
        body: GrantV1Request | GrantV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GrantV1Response, GrantErrorBody]:
        """Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for
        core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint
        will not work with the Manage APIs.

        Args:
            body: Time to live settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/auth/grant"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GrantV1Request | GrantV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GrantV1Response],
            error_mapper=grant_error_mapper,
            request_options=request_options,
        )


class AsyncAuthV1TokensWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def grant(
        self,
        *,
        body: GrantV1Request | GrantV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GrantV1Response, GrantErrorBody]:
        """Generates a temporary JSON Web Token (JWT) with a 30-second (by default) TTL and usage::write permission for
        core voice APIs, requiring an API key with Member or higher authorization. Tokens created with this endpoint
        will not work with the Manage APIs.

        Args:
            body: Time to live settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/auth/grant"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GrantV1Request | GrantV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GrantV1Response],
            error_mapper=grant_error_mapper,
            request_options=request_options,
        )
