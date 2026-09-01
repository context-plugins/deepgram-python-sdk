from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ReadPostParametersSummarize0(str, Enum):
    V2 = "v2"

    __str__ = str.__str__


V1ReadPostParametersSummarize0OrStr: TypeAlias = Annotated[
    V1ReadPostParametersSummarize0 | str, open_enum_validator(V1ReadPostParametersSummarize0)
]
