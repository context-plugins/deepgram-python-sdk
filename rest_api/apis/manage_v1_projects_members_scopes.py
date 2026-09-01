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
from ..errors.list9_error import List9ErrorBody, list9_error_mapper
from ..errors.update4_error import Update4ErrorBody, update4_error_mapper
from ..models.list_project_member_scopes_v1_response import ListProjectMemberScopesV1Response
from ..models.update_project_member_scopes_v1_request import (
    UpdateProjectMemberScopesV1Request,
    UpdateProjectMemberScopesV1RequestDict,
)
from ..models.update_project_member_scopes_v1_response import UpdateProjectMemberScopesV1Response
from ..server.server import Server


class ManageV1ProjectsMembersScopes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsMembersScopesWithRawResponse(client, server, auth)

    def list9(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectMemberScopesV1Response:
        """Retrieves a list of scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of scopes for a specific member

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list9(project_id, member_id, request_options=request_options).unwrap()

    def update4(
        self,
        project_id: str,
        member_id: str,
        *,
        body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateProjectMemberScopesV1Response:
        """Updates the scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            body: A scope to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated the scopes for a specific member

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.update4(
            project_id, member_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsMembersScopesWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsMembersScopes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsMembersScopesWithRawResponse(client, server, auth)

    async def list9(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectMemberScopesV1Response:
        """Retrieves a list of scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of scopes for a specific member

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list9(project_id, member_id, request_options=request_options)).unwrap()

    async def update4(
        self,
        project_id: str,
        member_id: str,
        *,
        body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateProjectMemberScopesV1Response:
        """Updates the scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            body: A scope to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Updated the scopes for a specific member

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.update4(project_id, member_id, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsMembersScopesWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsMembersScopesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list9(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectMemberScopesV1Response, List9ErrorBody]:
        """Retrieves a list of scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}/scopes"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectMemberScopesV1Response],
            error_mapper=list9_error_mapper,
            request_options=request_options,
        )

    def update4(
        self,
        project_id: str,
        member_id: str,
        *,
        body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateProjectMemberScopesV1Response, Update4ErrorBody]:
        """Updates the scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            body: A scope to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}/scopes"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UpdateProjectMemberScopesV1Response],
            error_mapper=update4_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsMembersScopesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list9(
        self, project_id: str, member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectMemberScopesV1Response, List9ErrorBody]:
        """Retrieves a list of scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}/scopes"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectMemberScopesV1Response],
            error_mapper=list9_error_mapper,
            request_options=request_options,
        )

    async def update4(
        self,
        project_id: str,
        member_id: str,
        *,
        body: UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateProjectMemberScopesV1Response, Update4ErrorBody]:
        """Updates the scopes for a specific member

        Args:
            project_id: The unique identifier of the project
            member_id: The unique identifier of the Member
            body: A scope to update
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/projects/{project_id}/members/{member_id}/scopes"),
            path_params=[param[str]("project_id", project_id), param[str]("member_id", member_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateProjectMemberScopesV1Request | UpdateProjectMemberScopesV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UpdateProjectMemberScopesV1Response],
            error_mapper=update4_error_mapper,
            request_options=request_options,
        )
