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
from ..errors.create2_error import Create2ErrorBody, create2_error_mapper
from ..errors.delete2_error import Delete2ErrorBody, delete2_error_mapper
from ..errors.get2_error import Get2ErrorBody, get2_error_mapper
from ..errors.list3_error import List3ErrorBody, list3_error_mapper
from ..errors.update2_error import Update2ErrorBody, update2_error_mapper
from ..models.agent_variable_v1 import AgentVariableV1
from ..models.create_agent_variable_v1_request import CreateAgentVariableV1Request, CreateAgentVariableV1RequestDict
from ..models.list_agent_variables_v1_response import ListAgentVariablesV1Response
from ..models.update_agent_variable_v1_request import UpdateAgentVariableV1Request, UpdateAgentVariableV1RequestDict
from ..server.server import Server


class VoiceAgentVariables:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VoiceAgentVariablesWithRawResponse(client, server, auth)

    def create2(
        self,
        project_id: str,
        *,
        body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentVariableV1:
        """Creates a new template variable. Variables follow the ``DG_<VARIABLE_NAME>`` naming format and can substitute
        any JSON value in an agent configuration.

        Args:
            project_id: The unique identifier of the project
            body: Agent variable details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.create2(project_id, body=body, request_options=request_options).unwrap()

    def delete2(self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Deletes the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete2(project_id, variable_id, request_options=request_options).unwrap()

    def get2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentVariableV1:
        """Returns the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An agent variable

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get2(project_id, variable_id, request_options=request_options).unwrap()

    def list3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentVariablesV1Response:
        """Returns all template variables for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of agent variables

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list3(project_id, request_options=request_options).unwrap()

    def update2(
        self,
        project_id: str,
        variable_id: str,
        *,
        body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentVariableV1:
        """Updates the value of an existing template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            body: Updated value for the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable updated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.update2(
            project_id, variable_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> VoiceAgentVariablesWithRawResponse:
        return self._with_raw_response


class AsyncVoiceAgentVariables:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVoiceAgentVariablesWithRawResponse(client, server, auth)

    async def create2(
        self,
        project_id: str,
        *,
        body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentVariableV1:
        """Creates a new template variable. Variables follow the ``DG_<VARIABLE_NAME>`` naming format and can substitute
        any JSON value in an agent configuration.

        Args:
            project_id: The unique identifier of the project
            body: Agent variable details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.create2(project_id, body=body, request_options=request_options)).unwrap()

    async def delete2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Deletes the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.delete2(project_id, variable_id, request_options=request_options)
        ).unwrap()

    async def get2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentVariableV1:
        """Returns the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An agent variable

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get2(project_id, variable_id, request_options=request_options)).unwrap()

    async def list3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentVariablesV1Response:
        """Returns all template variables for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of agent variables

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list3(project_id, request_options=request_options)).unwrap()

    async def update2(
        self,
        project_id: str,
        variable_id: str,
        *,
        body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentVariableV1:
        """Updates the value of an existing template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            body: Updated value for the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Agent variable updated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.update2(project_id, variable_id, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVoiceAgentVariablesWithRawResponse:
        return self._with_raw_response


class VoiceAgentVariablesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create2(
        self,
        project_id: str,
        *,
        body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentVariableV1, Create2ErrorBody]:
        """Creates a new template variable. Variables follow the ``DG_<VARIABLE_NAME>`` naming format and can substitute
        any JSON value in an agent configuration.

        Args:
            project_id: The unique identifier of the project
            body: Agent variable details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=create2_error_mapper,
            request_options=request_options,
        )

    def delete2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, Delete2ErrorBody]:
        """Deletes the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=delete2_error_mapper,
            request_options=request_options,
        )

    def get2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentVariableV1, Get2ErrorBody]:
        """Returns the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=get2_error_mapper,
            request_options=request_options,
        )

    def list3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentVariablesV1Response, List3ErrorBody]:
        """Returns all template variables for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListAgentVariablesV1Response],
            error_mapper=list3_error_mapper,
            request_options=request_options,
        )

    def update2(
        self,
        project_id: str,
        variable_id: str,
        *,
        body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentVariableV1, Update2ErrorBody]:
        """Updates the value of an existing template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            body: Updated value for the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=update2_error_mapper,
            request_options=request_options,
        )


class AsyncVoiceAgentVariablesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create2(
        self,
        project_id: str,
        *,
        body: CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentVariableV1, Create2ErrorBody]:
        """Creates a new template variable. Variables follow the ``DG_<VARIABLE_NAME>`` naming format and can substitute
        any JSON value in an agent configuration.

        Args:
            project_id: The unique identifier of the project
            body: Agent variable details
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentVariableV1Request | CreateAgentVariableV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=create2_error_mapper,
            request_options=request_options,
        )

    async def delete2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, Delete2ErrorBody]:
        """Deletes the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=delete2_error_mapper,
            request_options=request_options,
        )

    async def get2(
        self, project_id: str, variable_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentVariableV1, Get2ErrorBody]:
        """Returns the specified template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=get2_error_mapper,
            request_options=request_options,
        )

    async def list3(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentVariablesV1Response, List3ErrorBody]:
        """Returns all template variables for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListAgentVariablesV1Response],
            error_mapper=list3_error_mapper,
            request_options=request_options,
        )

    async def update2(
        self,
        project_id: str,
        variable_id: str,
        *,
        body: UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentVariableV1, Update2ErrorBody]:
        """Updates the value of an existing template variable

        Args:
            project_id: The unique identifier of the project
            variable_id: The unique identifier of the agent variable
            body: Updated value for the agent variable
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default("/v1/projects/{project_id}/agent-variables/{variable_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("variable_id", variable_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAgentVariableV1Request | UpdateAgentVariableV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentVariableV1],
            error_mapper=update2_error_mapper,
            request_options=request_options,
        )
