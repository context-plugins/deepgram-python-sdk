from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.agent_v1_settings_think_models import AgentV1SettingsThinkModels
from .apis.auth_v1_tokens import AuthV1Tokens
from .apis.listen_v1_media import ListenV1Media
from .apis.manage_v1_models import ManageV1Models
from .apis.manage_v1_projects import ManageV1Projects
from .apis.manage_v1_projects_billing_balances import ManageV1ProjectsBillingBalances
from .apis.manage_v1_projects_billing_breakdown import ManageV1ProjectsBillingBreakdown
from .apis.manage_v1_projects_billing_fields import ManageV1ProjectsBillingFields
from .apis.manage_v1_projects_billing_purchases import ManageV1ProjectsBillingPurchases
from .apis.manage_v1_projects_keys import ManageV1ProjectsKeys
from .apis.manage_v1_projects_members import ManageV1ProjectsMembers
from .apis.manage_v1_projects_members_invites import ManageV1ProjectsMembersInvites
from .apis.manage_v1_projects_members_scopes import ManageV1ProjectsMembersScopes
from .apis.manage_v1_projects_models import ManageV1ProjectsModels
from .apis.manage_v1_projects_requests import ManageV1ProjectsRequests
from .apis.manage_v1_projects_usage import ManageV1ProjectsUsage
from .apis.manage_v1_projects_usage_breakdown import ManageV1ProjectsUsageBreakdown
from .apis.manage_v1_projects_usage_fields import ManageV1ProjectsUsageFields
from .apis.read_v1_text import ReadV1Text
from .apis.self_hosted_v1_distribution_credentials import SelfHostedV1DistributionCredentials
from .apis.speak_v1_audio import SpeakV1Audio
from .apis.speak_v2_audio import SpeakV2Audio
from .apis.voice_agent_configurations import VoiceAgentConfigurations
from .apis.voice_agent_variables import VoiceAgentVariables
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseDeepgramClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    ApiKeyHeaderScheme,
    BearerAuthScheme,
    HttpClient,
    HttpxClient,
    RawClient,
    no_auth,
    param,
)
from .server.environment import Environment


class DeepgramClient(BaseDeepgramClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        custom_http_client: HttpClient | None = None,
        api_key_auth: str | None = None,
        jwt_auth: str | None = None,
    ) -> None:
        super().__init__(environment=environment, base_url=base_url, timeout=timeout)
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else HttpxClient(timeout=timeout),
            global_headers=[
                param[str]("User-Agent", "DeepgramClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(
            api_key_auth=ApiKeyHeaderScheme("Authorization", api_key_auth) if api_key_auth is not None else no_auth,
            jwt_auth=BearerAuthScheme(jwt_auth) if jwt_auth is not None else no_auth,
        )

    @cached_property
    def agent_v1_settings_think_models(self) -> AgentV1SettingsThinkModels:
        return AgentV1SettingsThinkModels(self._raw_client, self._server, self._auth)

    @cached_property
    def auth_v1_tokens(self) -> AuthV1Tokens:
        return AuthV1Tokens(self._raw_client, self._server, self._auth)

    @cached_property
    def listen_v1_media(self) -> ListenV1Media:
        return ListenV1Media(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_models(self) -> ManageV1Models:
        return ManageV1Models(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects(self) -> ManageV1Projects:
        return ManageV1Projects(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_balances(self) -> ManageV1ProjectsBillingBalances:
        return ManageV1ProjectsBillingBalances(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_breakdown(self) -> ManageV1ProjectsBillingBreakdown:
        return ManageV1ProjectsBillingBreakdown(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_fields(self) -> ManageV1ProjectsBillingFields:
        return ManageV1ProjectsBillingFields(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_billing_purchases(self) -> ManageV1ProjectsBillingPurchases:
        return ManageV1ProjectsBillingPurchases(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_keys(self) -> ManageV1ProjectsKeys:
        return ManageV1ProjectsKeys(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members(self) -> ManageV1ProjectsMembers:
        return ManageV1ProjectsMembers(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members_invites(self) -> ManageV1ProjectsMembersInvites:
        return ManageV1ProjectsMembersInvites(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_members_scopes(self) -> ManageV1ProjectsMembersScopes:
        return ManageV1ProjectsMembersScopes(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_models(self) -> ManageV1ProjectsModels:
        return ManageV1ProjectsModels(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_requests(self) -> ManageV1ProjectsRequests:
        return ManageV1ProjectsRequests(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage(self) -> ManageV1ProjectsUsage:
        return ManageV1ProjectsUsage(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage_breakdown(self) -> ManageV1ProjectsUsageBreakdown:
        return ManageV1ProjectsUsageBreakdown(self._raw_client, self._server, self._auth)

    @cached_property
    def manage_v1_projects_usage_fields(self) -> ManageV1ProjectsUsageFields:
        return ManageV1ProjectsUsageFields(self._raw_client, self._server, self._auth)

    @cached_property
    def read_v1_text(self) -> ReadV1Text:
        return ReadV1Text(self._raw_client, self._server, self._auth)

    @cached_property
    def self_hosted_v1_distribution_credentials(self) -> SelfHostedV1DistributionCredentials:
        return SelfHostedV1DistributionCredentials(self._raw_client, self._server, self._auth)

    @cached_property
    def speak_v1_audio(self) -> SpeakV1Audio:
        return SpeakV1Audio(self._raw_client, self._server, self._auth)

    @cached_property
    def speak_v2_audio(self) -> SpeakV2Audio:
        return SpeakV2Audio(self._raw_client, self._server, self._auth)

    @cached_property
    def voice_agent_configurations(self) -> VoiceAgentConfigurations:
        return VoiceAgentConfigurations(self._raw_client, self._server, self._auth)

    @cached_property
    def voice_agent_variables(self) -> VoiceAgentVariables:
        return VoiceAgentVariables(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = DeepgramClient
