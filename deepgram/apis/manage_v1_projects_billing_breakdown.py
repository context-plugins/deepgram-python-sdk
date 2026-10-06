from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
)
from ..errors.list14_error import List14ErrorBody, list14_error_mapper
from ..models.billing_breakdown_v1_response import BillingBreakdownV1Response
from ..models.enums.v1_projects_project_id_billing_breakdown_get_parameters_deployment import (
    V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr,
)
from ..models.enums.v1_projects_project_id_billing_breakdown_get_parameters_grouping_schema_items import (
    V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr,
)
from ..server.server import Server


class ManageV1ProjectsBillingBreakdown:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsBillingBreakdownWithRawResponse(client, server, auth)

    def list14(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        accessor: str | None = None,
        deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None,
        tag: str | None = None,
        line_item: str | None = None,
        grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BillingBreakdownV1Response:
        """Retrieves the billing summary for a specific project, with various filter options or by grouping options.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            accessor: Filter for requests where a specific accessor was used
            deployment: Filter for requests where a specific deployment was used
            tag: Filter for requests where a specific tag was used
            line_item: Filter requests by line item (e.g. streaming::nova-3)
            grouping: Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Billing breakdown response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list14(
            project_id,
            start=start,
            end=end,
            accessor=accessor,
            deployment=deployment,
            tag=tag,
            line_item=line_item,
            grouping=grouping,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsBillingBreakdownWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsBillingBreakdown:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsBillingBreakdownWithRawResponse(client, server, auth)

    async def list14(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        accessor: str | None = None,
        deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None,
        tag: str | None = None,
        line_item: str | None = None,
        grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BillingBreakdownV1Response:
        """Retrieves the billing summary for a specific project, with various filter options or by grouping options.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            accessor: Filter for requests where a specific accessor was used
            deployment: Filter for requests where a specific deployment was used
            tag: Filter for requests where a specific tag was used
            line_item: Filter requests by line item (e.g. streaming::nova-3)
            grouping: Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Billing breakdown response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list14(
                project_id,
                start=start,
                end=end,
                accessor=accessor,
                deployment=deployment,
                tag=tag,
                line_item=line_item,
                grouping=grouping,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsBillingBreakdownWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsBillingBreakdownWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list14(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        accessor: str | None = None,
        deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None,
        tag: str | None = None,
        line_item: str | None = None,
        grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BillingBreakdownV1Response, List14ErrorBody]:
        """Retrieves the billing summary for a specific project, with various filter options or by grouping options.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            accessor: Filter for requests where a specific accessor was used
            deployment: Filter for requests where a specific deployment was used
            tag: Filter for requests where a specific tag was used
            line_item: Filter requests by line item (e.g. streaming::nova-3)
            grouping: Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/billing/breakdown"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[Date | None]("start", start),
                param[Date | None]("end", end),
                param[str | None]("accessor", accessor),
                param[V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[str | None]("tag", tag),
                param[str | None]("line_item", line_item),
                param[list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None](
                    "grouping", grouping
                ),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[BillingBreakdownV1Response],
            error_mapper=list14_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsBillingBreakdownWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def list14(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        accessor: str | None = None,
        deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None,
        tag: str | None = None,
        line_item: str | None = None,
        grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BillingBreakdownV1Response, List14ErrorBody]:
        """Retrieves the billing summary for a specific project, with various filter options or by grouping options.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            accessor: Filter for requests where a specific accessor was used
            deployment: Filter for requests where a specific deployment was used
            tag: Filter for requests where a specific tag was used
            line_item: Filter requests by line item (e.g. streaming::nova-3)
            grouping: Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/billing/breakdown"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[Date | None]("start", start),
                param[Date | None]("end", end),
                param[str | None]("accessor", accessor),
                param[V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[str | None]("tag", tag),
                param[str | None]("line_item", line_item),
                param[list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None](
                    "grouping", grouping
                ),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[BillingBreakdownV1Response],
            error_mapper=list14_error_mapper,
            request_options=request_options,
        )
