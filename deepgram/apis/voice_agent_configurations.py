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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_error import CreateErrorBody, create_error_mapper
from ..errors.delete_error import DeleteErrorBody, delete_error_mapper
from ..errors.get_error import GetErrorBody, get_error_mapper
from ..errors.list2_error import List2ErrorBody, list2_error_mapper
from ..errors.update_error import UpdateErrorBody, update_error_mapper
from ..models.agent_configuration_v1 import AgentConfigurationV1
from ..models.create_agent_configuration_v1_request import (
    CreateAgentConfigurationV1Request,
    CreateAgentConfigurationV1RequestDict,
)
from ..models.create_agent_configuration_v1_response import CreateAgentConfigurationV1Response
from ..models.list_agent_configurations_v1_response import ListAgentConfigurationsV1Response
from ..models.update_agent_metadata_v1_request import UpdateAgentMetadataV1Request, UpdateAgentMetadataV1RequestDict
from ..server.server import Server


class VoiceAgentConfigurations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VoiceAgentConfigurationsWithRawResponse(client, server, auth)

    def create(
        self,
        project_id: str,
        *,
        body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAgentConfigurationV1Response:
        """Creates a new reusable agent configuration. The ``config`` field must be a valid JSON string representing the
        ``agent`` block of a Settings message. The returned ``agent_id`` can be passed in place of the full ``agent``
        object in future Settings messages.

        Args:
            project_id: The unique identifier of the project
            body: Agent configuration details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.create(project_id, body=body, request_options=request_options).unwrap()

    def delete(self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if
        your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete(project_id, agent_id, request_options=request_options).unwrap()

    def get(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentConfigurationV1:
        """Returns the specified agent configuration in its uninterpolated form

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An agent configuration

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get(project_id, agent_id, request_options=request_options).unwrap()

    def list2(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentConfigurationsV1Response:
        """Returns all agent configurations for the specified project. Configurations are returned in their
        uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of agent configurations

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list2(project_id, request_options=request_options).unwrap()

    def update(
        self,
        project_id: str,
        agent_id: str,
        *,
        body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentConfigurationV1:
        """Updates the metadata associated with an agent configuration. The config itself is immutable—to change the
        configuration, delete the existing agent and create a new one.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            body: Updated metadata for the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration updated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.update(project_id, agent_id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VoiceAgentConfigurationsWithRawResponse:
        return self._with_raw_response


class AsyncVoiceAgentConfigurations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVoiceAgentConfigurationsWithRawResponse(client, server, auth)

    async def create(
        self,
        project_id: str,
        *,
        body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateAgentConfigurationV1Response:
        """Creates a new reusable agent configuration. The ``config`` field must be a valid JSON string representing the
        ``agent`` block of a Settings message. The returned ``agent_id`` can be passed in place of the full ``agent``
        object in future Settings messages.

        Args:
            project_id: The unique identifier of the project
            body: Agent configuration details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration created successfully

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.create(project_id, body=body, request_options=request_options)).unwrap()

    async def delete(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if
        your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration deleted

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.delete(project_id, agent_id, request_options=request_options)).unwrap()

    async def get(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AgentConfigurationV1:
        """Returns the specified agent configuration in its uninterpolated form

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An agent configuration

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.get(project_id, agent_id, request_options=request_options)).unwrap()

    async def list2(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListAgentConfigurationsV1Response:
        """Returns all agent configurations for the specified project. Configurations are returned in their
        uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            A list of agent configurations

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list2(project_id, request_options=request_options)).unwrap()

    async def update(
        self,
        project_id: str,
        agent_id: str,
        *,
        body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AgentConfigurationV1:
        """Updates the metadata associated with an agent configuration. The config itself is immutable—to change the
        configuration, delete the existing agent and create a new one.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            body: Updated metadata for the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Agent configuration updated

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.update(project_id, agent_id, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncVoiceAgentConfigurationsWithRawResponse:
        return self._with_raw_response


class VoiceAgentConfigurationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create(
        self,
        project_id: str,
        *,
        body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAgentConfigurationV1Response, CreateErrorBody]:
        """Creates a new reusable agent configuration. The ``config`` field must be a valid JSON string representing the
        ``agent`` block of a Settings message. The returned ``agent_id`` can be passed in place of the full ``agent``
        object in future Settings messages.

        Args:
            project_id: The unique identifier of the project
            body: Agent configuration details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/agents"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateAgentConfigurationV1Response],
            error_mapper=create_error_mapper,
            request_options=request_options,
        )

    def delete(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteErrorBody]:
        """Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if
        your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[Any],
            error_mapper=delete_error_mapper,
            request_options=request_options,
        )

    def get(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentConfigurationV1, GetErrorBody]:
        """Returns the specified agent configuration in its uninterpolated form

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentConfigurationV1],
            error_mapper=get_error_mapper,
            request_options=request_options,
        )

    def list2(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentConfigurationsV1Response, List2ErrorBody]:
        """Returns all agent configurations for the specified project. Configurations are returned in their
        uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agents"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListAgentConfigurationsV1Response],
            error_mapper=list2_error_mapper,
            request_options=request_options,
        )

    def update(
        self,
        project_id: str,
        agent_id: str,
        *,
        body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentConfigurationV1, UpdateErrorBody]:
        """Updates the metadata associated with an agent configuration. The config itself is immutable—to change the
        configuration, delete the existing agent and create a new one.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            body: Updated metadata for the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[AgentConfigurationV1],
            error_mapper=update_error_mapper,
            request_options=request_options,
        )


class AsyncVoiceAgentConfigurationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create(
        self,
        project_id: str,
        *,
        body: CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateAgentConfigurationV1Response, CreateErrorBody]:
        """Creates a new reusable agent configuration. The ``config`` field must be a valid JSON string representing the
        ``agent`` block of a Settings message. The returned ``agent_id`` can be passed in place of the full ``agent``
        object in future Settings messages.

        Args:
            project_id: The unique identifier of the project
            body: Agent configuration details
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/agents"),
            path_params=[param[str]("project_id", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateAgentConfigurationV1Request | CreateAgentConfigurationV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[CreateAgentConfigurationV1Response],
            error_mapper=create_error_mapper,
            request_options=request_options,
        )

    async def delete(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteErrorBody]:
        """Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if
        your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[Any],
            error_mapper=delete_error_mapper,
            request_options=request_options,
        )

    async def get(
        self, project_id: str, agent_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AgentConfigurationV1, GetErrorBody]:
        """Returns the specified agent configuration in its uninterpolated form

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[AgentConfigurationV1],
            error_mapper=get_error_mapper,
            request_options=request_options,
        )

    async def list2(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListAgentConfigurationsV1Response, List2ErrorBody]:
        """Returns all agent configurations for the specified project. Configurations are returned in their
        uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/agents"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[ListAgentConfigurationsV1Response],
            error_mapper=list2_error_mapper,
            request_options=request_options,
        )

    async def update(
        self,
        project_id: str,
        agent_id: str,
        *,
        body: UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AgentConfigurationV1, UpdateErrorBody]:
        """Updates the metadata associated with an agent configuration. The config itself is immutable—to change the
        configuration, delete the existing agent and create a new one.

        Args:
            project_id: The unique identifier of the project
            agent_id: The unique identifier of the agent configuration
            body: Updated metadata for the agent configuration
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/projects/{project_id}/agents/{agent_id}"),
            path_params=[param[str]("project_id", project_id), param[str]("agent_id", agent_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateAgentMetadataV1Request | UpdateAgentMetadataV1RequestDict | None](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[AgentConfigurationV1],
            error_mapper=update_error_mapper,
            request_options=request_options,
        )
