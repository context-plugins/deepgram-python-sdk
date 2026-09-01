from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.agent_think_models_v1_response_models_items_one_of1_id import (
    AgentThinkModelsV1ResponseModelsItemsOneOf1IdOrStr,
)


class AgentThinkModelsV1ResponseModelsItems1(SdkBaseModel):
    """Anthropic models"""

    id: AgentThinkModelsV1ResponseModelsItemsOneOf1IdOrStr
    """The unique identifier of the Anthropic model"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems1Dict(TypedDict):
    id: AgentThinkModelsV1ResponseModelsItemsOneOf1IdOrStr
    name: str
    provider: Any
