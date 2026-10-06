from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .agent_variable_v1 import AgentVariableV1, AgentVariableV1Dict


class ListAgentVariablesV1Response(SdkBaseModel):
    variables: Optional[list[AgentVariableV1]] = UNSET
    """A list of agent variables for the project"""


class ListAgentVariablesV1ResponseDict(TypedDict):
    variables: NotRequired[list[AgentVariableV1Dict]]
