from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
)
from ..errors.get7_error import Get7ErrorBody, get7_error_mapper
from ..errors.list11_error import List11ErrorBody, list11_error_mapper
from ..models.enums.v1_projects_project_id_requests_get_parameters_deployment import (
    V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr,
)
from ..models.enums.v1_projects_project_id_requests_get_parameters_endpoint import (
    V1ProjectsProjectIdRequestsGetParametersEndpointOrStr,
)
from ..models.enums.v1_projects_project_id_requests_get_parameters_method import (
    V1ProjectsProjectIdRequestsGetParametersMethodOrStr,
)
from ..models.enums.v1_projects_project_id_requests_get_parameters_status import (
    V1ProjectsProjectIdRequestsGetParametersStatusOrStr,
)
from ..models.get_project_request_v1_response import GetProjectRequestV1Response
from ..models.list_project_requests_v1_response import ListProjectRequestsV1Response
from ..server.server import Server


class ManageV1ProjectsRequests:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsRequestsWithRawResponse(client, server, auth)

    def get7(
        self, project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectRequestV1Response:
        """Retrieves a specific request for a specific project

        Args:
            project_id: The unique identifier of the project
            request_id: The unique identifier of the request
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A specific request for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get7(project_id, request_id, request_options=request_options).unwrap()

    def list11(
        self,
        project_id: str,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        limit: float | None = 10.0,
        page: float | None = None,
        accessor: str | None = None,
        request_id: str | None = None,
        deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None,
        endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None,
        method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None,
        status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectRequestsV1Response:
        """Generates a list of requests for a specific project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            end: End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            accessor: Filter for requests where a specific accessor was used
            request_id: Filter for a specific request id
            deployment: Filter for requests where a specific deployment was used
            endpoint: Filter for requests where a specific endpoint was used
            method: Filter for requests where a specific method was used
            status: Filter for requests that succeeded (status code < 300) or failed (status code >=400)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of requests for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list11(
            project_id,
            start=start,
            end=end,
            limit=limit,
            page=page,
            accessor=accessor,
            request_id=request_id,
            deployment=deployment,
            endpoint=endpoint,
            method=method,
            status=status,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsRequestsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsRequests:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsRequestsWithRawResponse(client, server, auth)

    async def get7(
        self, project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectRequestV1Response:
        """Retrieves a specific request for a specific project

        Args:
            project_id: The unique identifier of the project
            request_id: The unique identifier of the request
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A specific request for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get7(project_id, request_id, request_options=request_options)).unwrap()

    async def list11(
        self,
        project_id: str,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        limit: float | None = 10.0,
        page: float | None = None,
        accessor: str | None = None,
        request_id: str | None = None,
        deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None,
        endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None,
        method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None,
        status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectRequestsV1Response:
        """Generates a list of requests for a specific project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            end: End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            accessor: Filter for requests where a specific accessor was used
            request_id: Filter for a specific request id
            deployment: Filter for requests where a specific deployment was used
            endpoint: Filter for requests where a specific endpoint was used
            method: Filter for requests where a specific method was used
            status: Filter for requests that succeeded (status code < 300) or failed (status code >=400)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of requests for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list11(
                project_id,
                start=start,
                end=end,
                limit=limit,
                page=page,
                accessor=accessor,
                request_id=request_id,
                deployment=deployment,
                endpoint=endpoint,
                method=method,
                status=status,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsRequestsWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsRequestsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get7(
        self, project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectRequestV1Response, Get7ErrorBody]:
        """Retrieves a specific request for a specific project

        Args:
            project_id: The unique identifier of the project
            request_id: The unique identifier of the request
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/requests/{request_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("request_id", request_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectRequestV1Response],
            error_mapper=get7_error_mapper,
            request_options=request_options,
        )

    def list11(
        self,
        project_id: str,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        limit: float | None = 10.0,
        page: float | None = None,
        accessor: str | None = None,
        request_id: str | None = None,
        deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None,
        endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None,
        method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None,
        status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectRequestsV1Response, List11ErrorBody]:
        """Generates a list of requests for a specific project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            end: End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            accessor: Filter for requests where a specific accessor was used
            request_id: Filter for a specific request id
            deployment: Filter for requests where a specific deployment was used
            endpoint: Filter for requests where a specific endpoint was used
            method: Filter for requests where a specific method was used
            status: Filter for requests that succeeded (status code < 300) or failed (status code >=400)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/requests"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[RFC3339DateTime | None]("start", start),
                param[RFC3339DateTime | None]("end", end),
                param[float | None]("limit", limit),
                param[float | None]("page", page),
                param[str | None]("accessor", accessor),
                param[str | None]("request_id", request_id),
                param[V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None]("endpoint", endpoint),
                param[V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None]("method", method),
                param[V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None]("status", status),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectRequestsV1Response],
            error_mapper=list11_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsRequestsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get7(
        self, project_id: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectRequestV1Response, Get7ErrorBody]:
        """Retrieves a specific request for a specific project

        Args:
            project_id: The unique identifier of the project
            request_id: The unique identifier of the request
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/requests/{request_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("request_id", request_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[GetProjectRequestV1Response],
            error_mapper=get7_error_mapper,
            request_options=request_options,
        )

    async def list11(
        self,
        project_id: str,
        *,
        start: RFC3339DateTime | None = None,
        end: RFC3339DateTime | None = None,
        limit: float | None = 10.0,
        page: float | None = None,
        accessor: str | None = None,
        request_id: str | None = None,
        deployment: V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None = None,
        endpoint: V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None = None,
        method: V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None = None,
        status: V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectRequestsV1Response, List11ErrorBody]:
        """Generates a list of requests for a specific project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            end: End date of the requested date range. Formats accepted are YYYY-MM-DD, YYYY-MM-DDTHH:MM:SS, or
                YYYY-MM-DDTHH:MM:SS+HH:MM
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            accessor: Filter for requests where a specific accessor was used
            request_id: Filter for a specific request id
            deployment: Filter for requests where a specific deployment was used
            endpoint: Filter for requests where a specific endpoint was used
            method: Filter for requests where a specific method was used
            status: Filter for requests that succeeded (status code < 300) or failed (status code >=400)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/requests"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[RFC3339DateTime | None]("start", start),
                param[RFC3339DateTime | None]("end", end),
                param[float | None]("limit", limit),
                param[float | None]("page", page),
                param[str | None]("accessor", accessor),
                param[str | None]("request_id", request_id),
                param[V1ProjectsProjectIdRequestsGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[V1ProjectsProjectIdRequestsGetParametersEndpointOrStr | None]("endpoint", endpoint),
                param[V1ProjectsProjectIdRequestsGetParametersMethodOrStr | None]("method", method),
                param[V1ProjectsProjectIdRequestsGetParametersStatusOrStr | None]("status", status),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListProjectRequestsV1Response],
            error_mapper=list11_error_mapper,
            request_options=request_options,
        )
