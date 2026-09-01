from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.agent_v1_settings_think_models import AsyncAgentV1SettingsThinkModels
from .apis.auth_v1_tokens import AsyncAuthV1Tokens
from .apis.listen_v1_media import AsyncListenV1Media
from .apis.manage_v1_models import AsyncManageV1Models
from .apis.manage_v1_projects import AsyncManageV1Projects
from .apis.manage_v1_projects_billing_balances import AsyncManageV1ProjectsBillingBalances
from .apis.manage_v1_projects_billing_breakdown import AsyncManageV1ProjectsBillingBreakdown
from .apis.manage_v1_projects_billing_fields import AsyncManageV1ProjectsBillingFields
from .apis.manage_v1_projects_billing_purchases import AsyncManageV1ProjectsBillingPurchases
from .apis.manage_v1_projects_keys import AsyncManageV1ProjectsKeys
from .apis.manage_v1_projects_members import AsyncManageV1ProjectsMembers
from .apis.manage_v1_projects_members_invites import AsyncManageV1ProjectsMembersInvites
from .apis.manage_v1_projects_members_scopes import AsyncManageV1ProjectsMembersScopes
from .apis.manage_v1_projects_models import AsyncManageV1ProjectsModels
from .apis.manage_v1_projects_requests import AsyncManageV1ProjectsRequests
from .apis.manage_v1_projects_usage import AsyncManageV1ProjectsUsage
from .apis.manage_v1_projects_usage_breakdown import AsyncManageV1ProjectsUsageBreakdown
from .apis.manage_v1_projects_usage_fields import AsyncManageV1ProjectsUsageFields
from .apis.read_v1_text import AsyncReadV1Text
from .apis.self_hosted_v1_distribution_credentials import AsyncSelfHostedV1DistributionCredentials
from .apis.speak_v1_audio import AsyncSpeakV1Audio
from .apis.speak_v2_audio import AsyncSpeakV2Audio
from .apis.voice_agent_configurations import AsyncVoiceAgentConfigurations
from .apis.voice_agent_variables import AsyncVoiceAgentVariables
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseRestApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    AsyncHttpClient,
    AsyncHttpxClient,
    AsyncRawClient,
    BearerAuthScheme,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncRestApiClient(BaseRestApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key_auth: str | None = None,
        jwt_auth: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpxClient(timeout=timeout)
            ),
            global_headers=[
                param[str]("User-Agent", "RestApiClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("Authorization", api_key_auth) if api_key_auth is not None else no_auth,
            jwt_auth=BearerAuthScheme(jwt_auth) if jwt_auth is not None else no_auth,
        )

    @cached_property
    def agent_v1_settings_think_models(self) -> AsyncAgentV1SettingsThinkModels:
        return AsyncAgentV1SettingsThinkModels(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_v1_tokens(self) -> AsyncAuthV1Tokens:
        return AsyncAuthV1Tokens(self._raw_client, self._server, self._auth)

    @cached_property
    def listen_v1_media(self) -> AsyncListenV1Media:
        return AsyncListenV1Media(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_models(self) -> AsyncManageV1Models:
        return AsyncManageV1Models(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects(self) -> AsyncManageV1Projects:
        return AsyncManageV1Projects(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_balances(self) -> AsyncManageV1ProjectsBillingBalances:
        return AsyncManageV1ProjectsBillingBalances(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_breakdown(self) -> AsyncManageV1ProjectsBillingBreakdown:
        return AsyncManageV1ProjectsBillingBreakdown(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_fields(self) -> AsyncManageV1ProjectsBillingFields:
        return AsyncManageV1ProjectsBillingFields(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_purchases(self) -> AsyncManageV1ProjectsBillingPurchases:
        return AsyncManageV1ProjectsBillingPurchases(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_keys(self) -> AsyncManageV1ProjectsKeys:
        return AsyncManageV1ProjectsKeys(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members(self) -> AsyncManageV1ProjectsMembers:
        return AsyncManageV1ProjectsMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members_invites(self) -> AsyncManageV1ProjectsMembersInvites:
        return AsyncManageV1ProjectsMembersInvites(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members_scopes(self) -> AsyncManageV1ProjectsMembersScopes:
        return AsyncManageV1ProjectsMembersScopes(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_models(self) -> AsyncManageV1ProjectsModels:
        return AsyncManageV1ProjectsModels(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_requests(self) -> AsyncManageV1ProjectsRequests:
        return AsyncManageV1ProjectsRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage(self) -> AsyncManageV1ProjectsUsage:
        return AsyncManageV1ProjectsUsage(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage_breakdown(self) -> AsyncManageV1ProjectsUsageBreakdown:
        return AsyncManageV1ProjectsUsageBreakdown(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage_fields(self) -> AsyncManageV1ProjectsUsageFields:
        return AsyncManageV1ProjectsUsageFields(self._raw_client, self._server, self._auth)

    @cached_property
    def read_v1_text(self) -> AsyncReadV1Text:
        return AsyncReadV1Text(self._raw_client, self._server, self._auth)

    @cached_property
    def self_hosted_v1_distribution_credentials(self) -> AsyncSelfHostedV1DistributionCredentials:
        return AsyncSelfHostedV1DistributionCredentials(self._raw_client, self._server, self._auth)

    @cached_property
    def speak_v1_audio(self) -> AsyncSpeakV1Audio:
        return AsyncSpeakV1Audio(self._raw_client, self._server, self._auth)

    @cached_property
    def speak_v2_audio(self) -> AsyncSpeakV2Audio:
        return AsyncSpeakV2Audio(self._raw_client, self._server, self._auth)

    @cached_property
    def voice_agent_configurations(self) -> AsyncVoiceAgentConfigurations:
        return AsyncVoiceAgentConfigurations(self._raw_client, self._server, self._auth)

    @cached_property
    def voice_agent_variables(self) -> AsyncVoiceAgentVariables:
        return AsyncVoiceAgentVariables(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncRestApiClient
