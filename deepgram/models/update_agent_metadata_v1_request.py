from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateAgentMetadataV1Request(SdkBaseModel):
    """Request body for updating agent configuration metadata"""

    metadata: dict[str, str]
    """A map of string key-value pairs to associate with this agent configuration"""


class UpdateAgentMetadataV1RequestDict(TypedDict):
    metadata: dict[str, str]
