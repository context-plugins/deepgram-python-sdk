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
from ..errors.create5_error import Create5ErrorBody, create5_error_mapper
from ..errors.delete7_error import Delete7ErrorBody, delete7_error_mapper
from ..errors.get11_error import Get11ErrorBody, get11_error_mapper
from ..errors.list17_error import List17ErrorBody, list17_error_mapper
from ..models.create_project_distribution_credentials_v1_request import (
    CreateProjectDistributionCredentialsV1Request,
    CreateProjectDistributionCredentialsV1RequestDict,
)
from ..models.create_project_distribution_credentials_v1_response import CreateProjectDistributionCredentialsV1Response
from ..models.enums.v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_provider import (
    V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr,
)
from ..models.enums.v1_projects_project_id_self_hosted_distribution_credentials_post_parameters_scopes_schema_items import (
    V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr,
)
from ..models.get_project_distribution_credentials_v1_response import GetProjectDistributionCredentialsV1Response
from ..models.list_project_distribution_credentials_v1_response import ListProjectDistributionCredentialsV1Response
from ..server.server import Server


class SelfHostedV1DistributionCredentials:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SelfHostedV1DistributionCredentialsWithRawResponse(client, server, auth)

    def create5(
        self,
        project_id: str,
        *,
        scopes: (
            list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None
        ) = None,
        provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None,
        body: (
            CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateProjectDistributionCredentialsV1Response:
        """Creates a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            scopes: List of permission scopes for the credentials
            provider: The provider of the distribution service
            body: The set of distribution credentials to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.create5(
            project_id, scopes=scopes, provider=provider, body=body, request_options=request_options
        ).unwrap()

    def delete7(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectDistributionCredentialsV1Response:
        """Deletes a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.delete7(
            project_id, distribution_credentials_id, request_options=request_options
        ).unwrap()

    def get11(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectDistributionCredentialsV1Response:
        """Returns a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get11(
            project_id, distribution_credentials_id, request_options=request_options
        ).unwrap()

    def list17(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectDistributionCredentialsV1Response:
        """Lists sets of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of distribution credentials for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list17(project_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SelfHostedV1DistributionCredentialsWithRawResponse:
        return self._with_raw_response


class AsyncSelfHostedV1DistributionCredentials:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSelfHostedV1DistributionCredentialsWithRawResponse(client, server, auth)

    async def create5(
        self,
        project_id: str,
        *,
        scopes: (
            list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None
        ) = None,
        provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None,
        body: (
            CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateProjectDistributionCredentialsV1Response:
        """Creates a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            scopes: List of permission scopes for the credentials
            provider: The provider of the distribution service
            body: The set of distribution credentials to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.create5(
                project_id, scopes=scopes, provider=provider, body=body, request_options=request_options
            )
        ).unwrap()

    async def delete7(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectDistributionCredentialsV1Response:
        """Deletes a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.delete7(
                project_id, distribution_credentials_id, request_options=request_options
            )
        ).unwrap()

    async def get11(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetProjectDistributionCredentialsV1Response:
        """Returns a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Single distribution credential

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.get11(
                project_id, distribution_credentials_id, request_options=request_options
            )
        ).unwrap()

    async def list17(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListProjectDistributionCredentialsV1Response:
        """Lists sets of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of distribution credentials for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (await self._with_raw_response.list17(project_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSelfHostedV1DistributionCredentialsWithRawResponse:
        return self._with_raw_response


class SelfHostedV1DistributionCredentialsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create5(
        self,
        project_id: str,
        *,
        scopes: (
            list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None
        ) = None,
        provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None,
        body: (
            CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateProjectDistributionCredentialsV1Response, Create5ErrorBody]:
        """Creates a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            scopes: List of permission scopes for the credentials
            provider: The provider of the distribution service
            body: The set of distribution credentials to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/self-hosted/distribution/credentials"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[
                    (
                        list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr]
                        | None
                    )
                ]("scopes", scopes),
                param[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None](
                    "provider", provider
                ),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
            ](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateProjectDistributionCredentialsV1Response],
            error_mapper=create5_error_mapper,
            request_options=request_options,
        )

    def delete7(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectDistributionCredentialsV1Response, Delete7ErrorBody]:
        """Deletes a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}"
            ),
            path_params=[
                param[str]("project_id", project_id),
                param[str]("distribution_credentials_id", distribution_credentials_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectDistributionCredentialsV1Response],
            error_mapper=delete7_error_mapper,
            request_options=request_options,
        )

    def get11(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectDistributionCredentialsV1Response, Get11ErrorBody]:
        """Returns a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}"
            ),
            path_params=[
                param[str]("project_id", project_id),
                param[str]("distribution_credentials_id", distribution_credentials_id),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectDistributionCredentialsV1Response],
            error_mapper=get11_error_mapper,
            request_options=request_options,
        )

    def list17(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectDistributionCredentialsV1Response, List17ErrorBody]:
        """Lists sets of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/self-hosted/distribution/credentials"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectDistributionCredentialsV1Response],
            error_mapper=list17_error_mapper,
            request_options=request_options,
        )


class AsyncSelfHostedV1DistributionCredentialsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create5(
        self,
        project_id: str,
        *,
        scopes: (
            list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr] | None
        ) = None,
        provider: V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None = None,
        body: (
            CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
        ) = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateProjectDistributionCredentialsV1Response, Create5ErrorBody]:
        """Creates a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            scopes: List of permission scopes for the credentials
            provider: The provider of the distribution service
            body: The set of distribution credentials to create
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{project_id}/self-hosted/distribution/credentials"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[
                    (
                        list[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr]
                        | None
                    )
                ]("scopes", scopes),
                param[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProviderOrStr | None](
                    "provider", provider
                ),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                CreateProjectDistributionCredentialsV1Request | CreateProjectDistributionCredentialsV1RequestDict | None
            ](body),
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[CreateProjectDistributionCredentialsV1Response],
            error_mapper=create5_error_mapper,
            request_options=request_options,
        )

    async def delete7(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectDistributionCredentialsV1Response, Delete7ErrorBody]:
        """Deletes a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default(
                "/v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}"
            ),
            path_params=[
                param[str]("project_id", project_id),
                param[str]("distribution_credentials_id", distribution_credentials_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectDistributionCredentialsV1Response],
            error_mapper=delete7_error_mapper,
            request_options=request_options,
        )

    async def get11(
        self, project_id: str, distribution_credentials_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetProjectDistributionCredentialsV1Response, Get11ErrorBody]:
        """Returns a set of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            distribution_credentials_id: The UUID of the distribution credentials
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default(
                "/v1/projects/{project_id}/self-hosted/distribution/credentials/{distribution_credentials_id}"
            ),
            path_params=[
                param[str]("project_id", project_id),
                param[str]("distribution_credentials_id", distribution_credentials_id),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[GetProjectDistributionCredentialsV1Response],
            error_mapper=get11_error_mapper,
            request_options=request_options,
        )

    async def list17(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListProjectDistributionCredentialsV1Response, List17ErrorBody]:
        """Lists sets of distribution credentials for the specified project

        Args:
            project_id: The unique identifier of the project
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/self-hosted/distribution/credentials"),
            path_params=[param[str]("project_id", project_id)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[ListProjectDistributionCredentialsV1Response],
            error_mapper=list17_error_mapper,
            request_options=request_options,
        )
