from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AgentThinkModelsV1ResponseModelsItemsOneOf1Id(str, Enum):
    """The unique identifier of the Anthropic model"""

    CLAUDE_3_5_HAIKU_LATEST = "claude-3-5-haiku-latest"
    CLAUDE_SONNET_4_20250514 = "claude-sonnet-4-20250514"

    __str__ = str.__str__


AgentThinkModelsV1ResponseModelsItemsOneOf1IdOrStr: TypeAlias = Annotated[
    AgentThinkModelsV1ResponseModelsItemsOneOf1Id | str,
    open_enum_validator(AgentThinkModelsV1ResponseModelsItemsOneOf1Id),
]
