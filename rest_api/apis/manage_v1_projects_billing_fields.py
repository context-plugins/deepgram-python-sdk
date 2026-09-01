from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.list15_error import List15ErrorBody, list15_error_mapper
from ..models.list_billing_fields_v1_response import ListBillingFieldsV1Response
from ..server.server import Server


class ManageV1ProjectsBillingFields:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsBillingFieldsWithRawResponse(client, server, auth)

    def list15(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBillingFieldsV1Response:
        """Lists the accessors, deployment types, tags, and line items used for billing data in the specified time
        period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to
        know what filters are available.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of billing fields for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list15(
            project_id, start=start, end=end, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsBillingFieldsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsBillingFields:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsBillingFieldsWithRawResponse(client, server, auth)

    async def list15(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBillingFieldsV1Response:
        """Lists the accessors, deployment types, tags, and line items used for billing data in the specified time
        period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to
        know what filters are available.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of billing fields for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list15(project_id, start=start, end=end, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsBillingFieldsWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsBillingFieldsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list15(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBillingFieldsV1Response, List15ErrorBody]:
        """Lists the accessors, deployment types, tags, and line items used for billing data in the specified time
        period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to
        know what filters are available.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/billing/fields"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[Date | None]("start", start), param[Date | None]("end", end)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListBillingFieldsV1Response],
            error_mapper=list15_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsBillingFieldsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list15(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBillingFieldsV1Response, List15ErrorBody]:
        """Lists the accessors, deployment types, tags, and line items used for billing data in the specified time
        period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to
        know what filters are available.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/billing/fields"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[Date | None]("start", start), param[Date | None]("end", end)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListBillingFieldsV1Response],
            error_mapper=list15_error_mapper,
            request_options=request_options,
        )
