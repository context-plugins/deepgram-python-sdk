from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateAgentConfigurationV1Request(SdkBaseModel):
    """Request body for creating an agent configuration"""

    config: str
    """A valid JSON string representing the agent block of a Settings message"""

    metadata: Optional[dict[str, str]] = UNSET
    """A map of arbitrary key-value pairs for labeling or organizing the agent configuration"""

    api_version: Optional[int] = UNSET
    """API version. Defaults to 1"""


class CreateAgentConfigurationV1RequestDict(TypedDict):
    config: str
    metadata: NotRequired[dict[str, str]]
    api_version: NotRequired[int]
