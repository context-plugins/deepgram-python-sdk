from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AgentThinkModelsV1ResponseModelsItems4(SdkBaseModel):
    """AWS Bedrock models (custom models accepted)"""

    id: str
    """The unique identifier of the AWS Bedrock model (any model string accepted for BYO LLMs)"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems4Dict(TypedDict):
    id: str
    name: str
    provider: Any
