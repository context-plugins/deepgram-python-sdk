from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentThinkModelsV1ResponseModelsItemsOneOf3Id(str, Enum):
    """The unique identifier of the Groq model"""

    OPENAI_GPT_OSS_20B = "openai/gpt-oss-20b"

    __str__ = str.__str__


AgentThinkModelsV1ResponseModelsItemsOneOf3IdOrStr: TypeAlias = Annotated[
    AgentThinkModelsV1ResponseModelsItemsOneOf3Id | str,
    open_enum_validator(AgentThinkModelsV1ResponseModelsItemsOneOf3Id),
]
