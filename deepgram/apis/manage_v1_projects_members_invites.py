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
from ..errors.create4_error import Create4ErrorBody, create4_error_mapper
from ..errors.delete6_error import Delete6ErrorBody, delete6_error_mapper
from ..errors.list10_error import List10ErrorBody, list10_error_mapper
from ..models.create_project_invite_v1_request import CreateProjectInviteV1Request, CreateProjectInviteV1RequestDict
from ..models.create_project_invite_v1_response import CreateProjectInviteV1Response
from ..models.delete_project_invite_v1_response import DeleteProjectInviteV1Response
from ..models.list_project_invites_v1_response import ListProjectInvitesV1Response
from ..server.server import Server


class ManageV1ProjectsMembersInvites:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsMembersInvitesWithRawResponse(client, server, auth)

    def create4(
        self,
        project_id: str,
        *,
        body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateProjectInviteV1Response:
        """Generates an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            body: email to invite to the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The invite was successfully generated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.create4(project_id, body=body, request_options=request_options).unwrap()

    def delete6(
        self, project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectInviteV1Response:
        """Deletes an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            email: The email address of the member
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The invite was successfully deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete6(project_id, email, request_options=request_options).unwrap()

    def list10(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectInvitesV1Response:
        """Generates a list of invites for a specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of invites for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list10(project_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsMembersInvitesWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsMembersInvites:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsMembersInvitesWithRawResponse(client, server, auth)

    async def create4(
        self,
        project_id: str,
        *,
        body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateProjectInviteV1Response:
        """Generates an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            body: email to invite to the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The invite was successfully generated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.create4(project_id, body=body, request_options=request_options)).unwrap()

    async def delete6(
        self, project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectInviteV1Response:
        """Deletes an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            email: The email address of the member
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The invite was successfully deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.delete6(project_id, email, request_options=request_options)).unwrap()

    async def list10(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectInvitesV1Response:
        """Generates a list of invites for a specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of invites for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list10(project_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsMembersInvitesWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsMembersInvitesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create4(
        self,
        project_id: str,
        *,
        body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateProjectInviteV1Response, Create4ErrorBody]:
        """Generates an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            body: email to invite to the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/invites"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateProjectInviteV1Response],
            error_mapper=create4_error_mapper,
            request_options=request_options,
        )

    def delete6(
        self, project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectInviteV1Response, Delete6ErrorBody]:
        """Deletes an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            email: The email address of the member
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/invites/{email}"),
            path_params=[param[str]("project_id", project_id), param[str]("email", email)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectInviteV1Response],
            error_mapper=delete6_error_mapper,
            request_options=request_options,
        )

    def list10(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectInvitesV1Response, List10ErrorBody]:
        """Generates a list of invites for a specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/invites"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectInvitesV1Response],
            error_mapper=list10_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsMembersInvitesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create4(
        self,
        project_id: str,
        *,
        body: CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateProjectInviteV1Response, Create4ErrorBody]:
        """Generates an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            body: email to invite to the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/invites"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateProjectInviteV1Request | CreateProjectInviteV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[CreateProjectInviteV1Response],
            error_mapper=create4_error_mapper,
            request_options=request_options,
        )

    async def delete6(
        self, project_id: str, email: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectInviteV1Response, Delete6ErrorBody]:
        """Deletes an invite for a specific project

        Args:
            project_id: The unique identifier of the project
            email: The email address of the member
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/invites/{email}"),
            path_params=[param[str]("project_id", project_id), param[str]("email", email)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[DeleteProjectInviteV1Response],
            error_mapper=delete6_error_mapper,
            request_options=request_options,
        )

    async def list10(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectInvitesV1Response, List10ErrorBody]:
        """Generates a list of invites for a specific project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/invites"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListProjectInvitesV1Response],
            error_mapper=list10_error_mapper,
            request_options=request_options,
        )
