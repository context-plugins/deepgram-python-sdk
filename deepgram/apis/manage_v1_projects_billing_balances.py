from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.get10_error import Get10ErrorBody, get10_error_mapper
from ..errors.list13_error import List13ErrorBody, list13_error_mapper
from ..models.get_project_balance_v1_response import GetProjectBalanceV1Response
from ..models.list_project_balances_v1_response import ListProjectBalancesV1Response
from ..server.server import Server


class ManageV1ProjectsBillingBalances:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsBillingBalancesWithRawResponse(client, server, auth)

    def get10(
        self, project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectBalanceV1Response:
        """Retrieves details about the specified balance

        Args:
            project_id: The unique identifier of the project
            balance_id: The unique identifier of the balance
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A specific balance

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get10(project_id, balance_id, request_options=request_options).unwrap()

    def list13(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectBalancesV1Response:
        """Generates a list of outstanding balances for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of outstanding balances

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list13(project_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsBillingBalancesWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsBillingBalances:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsBillingBalancesWithRawResponse(client, server, auth)

    async def get10(
        self, project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectBalanceV1Response:
        """Retrieves details about the specified balance

        Args:
            project_id: The unique identifier of the project
            balance_id: The unique identifier of the balance
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A specific balance

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get10(project_id, balance_id, request_options=request_options)).unwrap()

    async def list13(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectBalancesV1Response:
        """Generates a list of outstanding balances for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of outstanding balances

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list13(project_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsBillingBalancesWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsBillingBalancesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get10(
        self, project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectBalanceV1Response, Get10ErrorBody]:
        """Retrieves details about the specified balance

        Args:
            project_id: The unique identifier of the project
            balance_id: The unique identifier of the balance
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/balances/{balance_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("balance_id", balance_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectBalanceV1Response],
            error_mapper=get10_error_mapper,
            request_options=request_options,
        )

    def list13(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectBalancesV1Response, List13ErrorBody]:
        """Generates a list of outstanding balances for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/balances"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectBalancesV1Response],
            error_mapper=list13_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsBillingBalancesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get10(
        self, project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectBalanceV1Response, Get10ErrorBody]:
        """Retrieves details about the specified balance

        Args:
            project_id: The unique identifier of the project
            balance_id: The unique identifier of the balance
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/balances/{balance_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("balance_id", balance_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectBalanceV1Response],
            error_mapper=get10_error_mapper,
            request_options=request_options,
        )

    async def list13(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectBalancesV1Response, List13ErrorBody]:
        """Generates a list of outstanding balances for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/balances"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectBalancesV1Response],
            error_mapper=list13_error_mapper,
            request_options=request_options,
        )
