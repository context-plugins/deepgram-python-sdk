from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .agent_configuration_v1 import AgentConfigurationV1, AgentConfigurationV1Dict


class ListAgentConfigurationsV1Response(SdkBaseModel):
    agents: Optional[list[AgentConfigurationV1]] = UNSET
    """A list of agent configurations for the project"""


class ListAgentConfigurationsV1ResponseDict(TypedDict):
    agents: NotRequired[list[AgentConfigurationV1 | AgentConfigurationV1Dict]]
