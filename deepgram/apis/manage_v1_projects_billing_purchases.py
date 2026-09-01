from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.list16_error import List16ErrorBody, list16_error_mapper
from ..models.list_project_purchases_v1_response import ListProjectPurchasesV1Response
from ..server.server import Server


class ManageV1ProjectsBillingPurchases:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsBillingPurchasesWithRawResponse(client, server, auth)

    def list16(
        self, project_id: str, *, limit: float | None = 10.0, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectPurchasesV1Response:
        """Returns the original purchased amount on an order transaction

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of purchases for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list16(project_id, limit=limit, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsBillingPurchasesWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsBillingPurchases:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsBillingPurchasesWithRawResponse(client, server, auth)

    async def list16(
        self, project_id: str, *, limit: float | None = 10.0, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectPurchasesV1Response:
        """Returns the original purchased amount on an order transaction

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of purchases for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list16(project_id, limit=limit, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsBillingPurchasesWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsBillingPurchasesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list16(
        self, project_id: str, *, limit: float | None = 10.0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectPurchasesV1Response, List16ErrorBody]:
        """Returns the original purchased amount on an order transaction

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/purchases"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[float | None]("limit", limit)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectPurchasesV1Response],
            error_mapper=list16_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsBillingPurchasesWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list16(
        self, project_id: str, *, limit: float | None = 10.0, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectPurchasesV1Response, List16ErrorBody]:
        """Returns the original purchased amount on an order transaction

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/purchases"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[float | None]("limit", limit)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectPurchasesV1Response],
            error_mapper=list16_error_mapper,
            request_options=request_options,
        )
