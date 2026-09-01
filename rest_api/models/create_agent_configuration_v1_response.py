from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateAgentConfigurationV1Response(SdkBaseModel):
    agent_id: str
    """The unique identifier of the newly created agent configuration"""

    config: Any
    """The parsed agent configuration object"""

    metadata: Optional[dict[str, str]] = UNSET
    """Metadata associated with the agent configuration"""


class CreateAgentConfigurationV1ResponseDict(TypedDict):
    agent_id: str
    config: Any
    metadata: NotRequired[dict[str, str]]
