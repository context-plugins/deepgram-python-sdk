from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.agent_think_models_v1_response_models_items_one_of3_id import (
    AgentThinkModelsV1ResponseModelsItemsOneOf3IdOrStr,
)


class AgentThinkModelsV1ResponseModelsItems3(SdkBaseModel):
    """Groq models"""

    id: AgentThinkModelsV1ResponseModelsItemsOneOf3IdOrStr
    """The unique identifier of the Groq model"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems3Dict(TypedDict):
    id: AgentThinkModelsV1ResponseModelsItemsOneOf3IdOrStr
    name: str
    provider: Any
