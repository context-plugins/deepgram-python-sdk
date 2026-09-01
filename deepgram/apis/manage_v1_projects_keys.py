from __future__ import annotations

from typing import Any
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
from ..errors.create3_error import Create3ErrorBody, create3_error_mapper
from ..errors.delete4_error import Delete4ErrorBody, delete4_error_mapper
from ..errors.get6_error import Get6ErrorBody, get6_error_mapper
from ..errors.list7_error import List7ErrorBody, list7_error_mapper
from ..models.create_key_v1_response import CreateKeyV1Response
from ..models.delete_project_key_v1_response import DeleteProjectKeyV1Response
from ..models.enums.v1_projects_project_id_keys_get_parameters_status import (
    V1ProjectsProjectIdKeysGetParametersStatusOrStr,
)
from ..models.get_project_key_v1_response import GetProjectKeyV1Response
from ..models.list_project_keys_v1_response import ListProjectKeysV1Response
from ..server.server import Server


class ManageV1ProjectsKeys:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsKeysWithRawResponse(client, server, auth)

    def create3(
        self, project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CreateKeyV1Response:
        """Creates a new API key with specified settings for the project

        Args:
            project_id: The unique identifier of the project
            body: API key settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API key created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.create3(project_id, body=body, request_options=request_options).unwrap()

    def delete4(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectKeyV1Response:
        """Deletes an API key for a specific project

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API key deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete4(project_id, key_id, request_options=request_options).unwrap()

    def get6(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectKeyV1Response:
        """Retrieves information about a specified API key

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A specific API key

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get6(project_id, key_id, request_options=request_options).unwrap()

    def list7(
        self,
        project_id: str,
        *,
        status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectKeysV1Response:
        """Retrieves all API keys associated with the specified project

        Args:
            project_id: The unique identifier of the project
            status: Only return keys with a specific status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of API keys

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list7(project_id, status=status, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsKeysWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsKeys:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsKeysWithRawResponse(client, server, auth)

    async def create3(
        self, project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> CreateKeyV1Response:
        """Creates a new API key with specified settings for the project

        Args:
            project_id: The unique identifier of the project
            body: API key settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API key created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.create3(project_id, body=body, request_options=request_options)).unwrap()

    async def delete4(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteProjectKeyV1Response:
        """Deletes an API key for a specific project

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            API key deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.delete4(project_id, key_id, request_options=request_options)).unwrap()

    async def get6(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectKeyV1Response:
        """Retrieves information about a specified API key

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A specific API key

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get6(project_id, key_id, request_options=request_options)).unwrap()

    async def list7(
        self,
        project_id: str,
        *,
        status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectKeysV1Response:
        """Retrieves all API keys associated with the specified project

        Args:
            project_id: The unique identifier of the project
            status: Only return keys with a specific status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of API keys

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list7(project_id, status=status, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsKeysWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsKeysWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create3(
        self, project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateKeyV1Response, Create3ErrorBody]:
        """Creates a new API key with specified settings for the project

        Args:
            project_id: The unique identifier of the project
            body: API key settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/keys"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateKeyV1Response],
            error_mapper=create3_error_mapper,
            request_options=request_options,
        )

    def delete4(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectKeyV1Response, Delete4ErrorBody]:
        """Deletes an API key for a specific project

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/keys/{key_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("key_id", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectKeyV1Response],
            error_mapper=delete4_error_mapper,
            request_options=request_options,
        )

    def get6(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectKeyV1Response, Get6ErrorBody]:
        """Retrieves information about a specified API key

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/keys/{key_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("key_id", key_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectKeyV1Response],
            error_mapper=get6_error_mapper,
            request_options=request_options,
        )

    def list7(
        self,
        project_id: str,
        *,
        status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectKeysV1Response, List7ErrorBody]:
        """Retrieves all API keys associated with the specified project

        Args:
            project_id: The unique identifier of the project
            status: Only return keys with a specific status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/keys"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[V1ProjectsProjectIdKeysGetParametersStatusOrStr | None]("status", status)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectKeysV1Response],
            error_mapper=list7_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsKeysWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create3(
        self, project_id: str, *, body: Any | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateKeyV1Response, Create3ErrorBody]:
        """Creates a new API key with specified settings for the project

        Args:
            project_id: The unique identifier of the project
            body: API key settings
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/keys"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateKeyV1Response],
            error_mapper=create3_error_mapper,
            request_options=request_options,
        )

    async def delete4(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteProjectKeyV1Response, Delete4ErrorBody]:
        """Deletes an API key for a specific project

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/keys/{key_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("key_id", key_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[DeleteProjectKeyV1Response],
            error_mapper=delete4_error_mapper,
            request_options=request_options,
        )

    async def get6(
        self, project_id: str, key_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectKeyV1Response, Get6ErrorBody]:
        """Retrieves information about a specified API key

        Args:
            project_id: The unique identifier of the project
            key_id: The unique identifier of the API key
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/keys/{key_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("key_id", key_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectKeyV1Response],
            error_mapper=get6_error_mapper,
            request_options=request_options,
        )

    async def list7(
        self,
        project_id: str,
        *,
        status: V1ProjectsProjectIdKeysGetParametersStatusOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectKeysV1Response, List7ErrorBody]:
        """Retrieves all API keys associated with the specified project

        Args:
            project_id: The unique identifier of the project
            status: Only return keys with a specific status
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/keys"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[V1ProjectsProjectIdKeysGetParametersStatusOrStr | None]("status", status)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectKeysV1Response],
            error_mapper=list7_error_mapper,
            request_options=request_options,
        )
