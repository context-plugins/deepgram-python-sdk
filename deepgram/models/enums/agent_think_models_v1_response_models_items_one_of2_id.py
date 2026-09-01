from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentThinkModelsV1ResponseModelsItemsOneOf2Id(str, Enum):
    """The unique identifier of the Google model"""

    GEMINI_2_5_FLASH = "gemini-2.5-flash"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"
    GEMINI_2_0_FLASH_LITE = "gemini-2.0-flash-lite"

    __str__ = str.__str__


AgentThinkModelsV1ResponseModelsItemsOneOf2IdOrStr: TypeAlias = Annotated[
    AgentThinkModelsV1ResponseModelsItemsOneOf2Id | str,
    open_enum_validator(AgentThinkModelsV1ResponseModelsItemsOneOf2Id),
]
