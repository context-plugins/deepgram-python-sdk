from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.agent_think_models_v1_response_models_items_one_of0_id import (
    AgentThinkModelsV1ResponseModelsItemsOneOf0IdOrStr,
)


class AgentThinkModelsV1ResponseModelsItems0(SdkBaseModel):
    """OpenAI models"""

    id: AgentThinkModelsV1ResponseModelsItemsOneOf0IdOrStr
    """The unique identifier of the OpenAI model"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems0Dict(TypedDict):
    id: AgentThinkModelsV1ResponseModelsItemsOneOf0IdOrStr
    name: str
    provider: Any
