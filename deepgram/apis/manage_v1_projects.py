from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete3_error import Delete3ErrorBody, delete3_error_mapper
from ..errors.get3_error import Get3ErrorBody, get3_error_mapper
from ..errors.leave_error import LeaveErrorBody, leave_error_mapper
from ..errors.list4_error import List4ErrorBody, list4_error_mapper
from ..errors.update3_error import Update3ErrorBody, update3_error_mapper
from ..models.delete_project_v1_response import DeleteProjectV1Response
from ..models.get_project_v1_response import GetProjectV1Response
from ..models.leave_project_v1_response import LeaveProjectV1Response
from ..models.list_projects_v1_response import ListProjectsV1Response
from ..models.update_project_v1_request import UpdateProjectV1Request, UpdateProjectV1RequestDict
from ..models.update_project_v1_response import UpdateProjectV1Response
from ..server.server import Server


class ManageV1Projects:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsWithRawResponse(client, server, auth)

    def delete3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectV1Response:
        """Deletes the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete3(project_id, request_options=request_options).unwrap()

    def get3(
        self,
        project_id: str,
        *,
        limit: float | None = 10.0,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetProjectV1Response:
        """Retrieves information about the specified project

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get3(
            project_id, limit=limit, page=page, request_options=request_options
        ).unwrap()

    def leave(self, project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> LeaveProjectV1Response:
        """Removes the authenticated account from the specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully removed account from project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.leave(project_id, request_options=request_options).unwrap()

    def list4(self, *, request_options: RequestOptionsOrDict | None = None) -> ListProjectsV1Response:
        """Retrieves basic information about the projects associated with the API key

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of projects

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list4(request_options=request_options).unwrap()

    def update3(
        self,
        project_id: str,
        *,
        body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateProjectV1Response:
        """Updates the name or other properties of an existing project

        Args:
            project_id: The unique identifier of the project
            body: The name of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.update3(project_id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1Projects:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsWithRawResponse(client, server, auth)

    async def delete3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectV1Response:
        """Deletes the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.delete3(project_id, request_options=request_options)).unwrap()

    async def get3(
        self,
        project_id: str,
        *,
        limit: float | None = 10.0,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetProjectV1Response:
        """Retrieves information about the specified project

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.get3(project_id, limit=limit, page=page, request_options=request_options)
        ).unwrap()

    async def leave(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> LeaveProjectV1Response:
        """Removes the authenticated account from the specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully removed account from project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.leave(project_id, request_options=request_options)).unwrap()

    async def list4(self, *, request_options: RequestOptionsOrDict | None = None) -> ListProjectsV1Response:
        """Retrieves basic information about the projects associated with the API key

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of projects

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list4(request_options=request_options)).unwrap()

    async def update3(
        self,
        project_id: str,
        *,
        body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateProjectV1Response:
        """Updates the name or other properties of an existing project

        Args:
            project_id: The unique identifier of the project
            body: The name of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.update3(project_id, body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectV1Response, Delete3ErrorBody]:
        """Deletes the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectV1Response],
            error_mapper=delete3_error_mapper,
            request_options=request_options,
        )

    def get3(
        self,
        project_id: str,
        *,
        limit: float | None = 10.0,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetProjectV1Response, Get3ErrorBody]:
        """Retrieves information about the specified project

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[float | None]("limit", limit), param[float | None]("page", page)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectV1Response],
            error_mapper=get3_error_mapper,
            request_options=request_options,
        )

    def leave(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaveProjectV1Response, LeaveErrorBody]:
        """Removes the authenticated account from the specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/leave"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[LeaveProjectV1Response],
            error_mapper=leave_error_mapper,
            request_options=request_options,
        )

    def list4(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectsV1Response, List4ErrorBody]:
        """Retrieves basic information about the projects associated with the API key

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects"),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectsV1Response],
            error_mapper=list4_error_mapper,
            request_options=request_options,
        )

    def update3(
        self,
        project_id: str,
        *,
        body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateProjectV1Response, Update3ErrorBody]:
        """Updates the name or other properties of an existing project

        Args:
            project_id: The unique identifier of the project
            body: The name of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProjectV1Request | UpdateProjectV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UpdateProjectV1Response],
            error_mapper=update3_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectV1Response, Delete3ErrorBody]:
        """Deletes the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[DeleteProjectV1Response],
            error_mapper=delete3_error_mapper,
            request_options=request_options,
        )

    async def get3(
        self,
        project_id: str,
        *,
        limit: float | None = 10.0,
        page: float | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetProjectV1Response, Get3ErrorBody]:
        """Retrieves information about the specified project

        Args:
            project_id: The unique identifier of the project
            limit: Number of results to return per page. Default 10. Range [1,1000]
            page: Navigate and return the results to retrieve specific portions of information of the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[float | None]("limit", limit), param[float | None]("page", page)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[GetProjectV1Response],
            error_mapper=get3_error_mapper,
            request_options=request_options,
        )

    async def leave(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LeaveProjectV1Response, LeaveErrorBody]:
        """Removes the authenticated account from the specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/leave"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[LeaveProjectV1Response],
            error_mapper=leave_error_mapper,
            request_options=request_options,
        )

    async def list4(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectsV1Response, List4ErrorBody]:
        """Retrieves basic information about the projects associated with the API key

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects"),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListProjectsV1Response],
            error_mapper=list4_error_mapper,
            request_options=request_options,
        )

    async def update3(
        self,
        project_id: str,
        *,
        body: UpdateProjectV1Request | UpdateProjectV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateProjectV1Response, Update3ErrorBody]:
        """Updates the name or other properties of an existing project

        Args:
            project_id: The unique identifier of the project
            body: The name of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/projects/{project_id}"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProjectV1Request | UpdateProjectV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[UpdateProjectV1Response],
            error_mapper=update3_error_mapper,
            request_options=request_options,
        )
