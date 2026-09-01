from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import ApiResult, AsyncRawClient, RawClient, RequestOptionsOrDict, SecuredRawResponse, json_decoder, param
from ..errors.delete5_error import Delete5ErrorBody, delete5_error_mapper
from ..errors.list8_error import List8ErrorBody, list8_error_mapper
from ..models.delete_project_member_v1_response import DeleteProjectMemberV1Response
from ..models.list_project_members_v1_response import ListProjectMembersV1Response
from ..server.server import Server


class ManageV1ProjectsMembers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsMembersWithRawResponse(client, server, auth)

    def delete5(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectMemberV1Response:
        """Removes a member from the project using their unique member ID

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete the specific member from the project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete5(project_id, member_id, request_options=request_options).unwrap()

    def list8(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectMembersV1Response:
        """Retrieves a list of members for a given project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of members for a given project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list8(project_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsMembersWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsMembers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsMembersWithRawResponse(client, server, auth)

    async def delete5(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectMemberV1Response:
        """Removes a member from the project using their unique member ID

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete the specific member from the project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.delete5(project_id, member_id, request_options=request_options)).unwrap()

    async def list8(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectMembersV1Response:
        """Retrieves a list of members for a given project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of members for a given project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list8(project_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsMembersWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsMembersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete5(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectMemberV1Response, Delete5ErrorBody]:
        """Removes a member from the project using their unique member ID

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectMemberV1Response],
            error_mapper=delete5_error_mapper,
            request_options=request_options,
        )

    def list8(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectMembersV1Response, List8ErrorBody]:
        """Retrieves a list of members for a given project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/members"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectMembersV1Response],
            error_mapper=list8_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsMembersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete5(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectMemberV1Response, Delete5ErrorBody]:
        """Removes a member from the project using their unique member ID

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectMemberV1Response],
            error_mapper=delete5_error_mapper,
            request_options=request_options,
        )

    async def list8(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectMembersV1Response, List8ErrorBody]:
        """Retrieves a list of members for a given project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/members"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectMembersV1Response],
            error_mapper=list8_error_mapper,
            request_options=request_options,
        )
