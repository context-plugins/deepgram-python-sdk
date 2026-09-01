from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.list12_error import List12ErrorBody, list12_error_mapper
from ..models.usage_fields_v1_response import UsageFieldsV1Response
from ..server.server import Server


class ManageV1ProjectsUsageFields:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsUsageFieldsWithRawResponse(client, server, auth)

    def list12(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageFieldsV1Response:
        """Lists the features, models, tags, languages, and processing method used for requests in the specified project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of fields for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.list12(
            project_id, start=start, end=end, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsUsageFieldsWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsUsageFields:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsUsageFieldsWithRawResponse(client, server, auth)

    async def list12(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageFieldsV1Response:
        """Lists the features, models, tags, languages, and processing method used for requests in the specified project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of fields for a specific project

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.list12(project_id, start=start, end=end, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsUsageFieldsWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsUsageFieldsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list12(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageFieldsV1Response, List12ErrorBody]:
        """Lists the features, models, tags, languages, and processing method used for requests in the specified project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/usage/fields"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[Date | None]("start", start), param[Date | None]("end", end)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UsageFieldsV1Response],
            error_mapper=list12_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsUsageFieldsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list12(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageFieldsV1Response, List12ErrorBody]:
        """Lists the features, models, tags, languages, and processing method used for requests in the specified project

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/usage/fields"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[param[Date | None]("start", start), param[Date | None]("end", end)],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UsageFieldsV1Response],
            error_mapper=list12_error_mapper,
            request_options=request_options,
        )
