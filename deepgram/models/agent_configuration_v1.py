from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AgentConfigurationV1(SdkBaseModel):
    """A reusable agent configuration"""

    agent_id: str
    """The unique identifier of the agent configuration"""

    config: Any
    """The agent configuration object"""

    metadata: Optional[dict[str, str]] = UNSET
    """A map of arbitrary key-value pairs for labeling or organizing the agent configuration"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp when the configuration was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp when the configuration was last updated"""


class AgentConfigurationV1Dict(TypedDict):
    agent_id: str
    config: Any
    metadata: NotRequired[dict[str, str]]
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
