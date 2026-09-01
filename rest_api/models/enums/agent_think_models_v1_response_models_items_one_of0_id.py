from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentThinkModelsV1ResponseModelsItemsOneOf0Id(str, Enum):
    """The unique identifier of the OpenAI model"""

    GPT_5 = "gpt-5"
    GPT_5_MINI = "gpt-5-mini"
    GPT_5_NANO = "gpt-5-nano"
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"

    __str__ = str.__str__


AgentThinkModelsV1ResponseModelsItemsOneOf0IdOrStr: TypeAlias = Annotated[
    AgentThinkModelsV1ResponseModelsItemsOneOf0Id | str,
    open_enum_validator(AgentThinkModelsV1ResponseModelsItemsOneOf0Id),
]
