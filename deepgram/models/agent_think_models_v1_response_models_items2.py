from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.agent_think_models_v1_response_models_items_one_of2_id import (
    AgentThinkModelsV1ResponseModelsItemsOneOf2IdOrStr,
)


class AgentThinkModelsV1ResponseModelsItems2(SdkBaseModel):
    """Google models"""

    id: AgentThinkModelsV1ResponseModelsItemsOneOf2IdOrStr
    """The unique identifier of the Google model"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems2Dict(TypedDict):
    id: AgentThinkModelsV1ResponseModelsItemsOneOf2IdOrStr
    name: str
    provider: Any
