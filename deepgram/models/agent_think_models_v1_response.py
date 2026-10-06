from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.agent_think_models_v1_response_models_items import (
    AgentThinkModelsV1ResponseModelsItems,
    AgentThinkModelsV1ResponseModelsItemsDict,
)


class AgentThinkModelsV1Response(SdkBaseModel):
    models: list[AgentThinkModelsV1ResponseModelsItems]


class AgentThinkModelsV1ResponseDict(TypedDict):
    models: list[AgentThinkModelsV1ResponseModelsItemsDict]
