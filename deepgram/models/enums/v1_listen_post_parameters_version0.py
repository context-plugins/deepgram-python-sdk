from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersVersion0(str, Enum):
    """Use the latest version of a model"""

    LATEST = "latest"

    __str__ = str.__str__


V1ListenPostParametersVersion0OrStr: TypeAlias = Annotated[
    V1ListenPostParametersVersion0 | str, open_enum_validator(V1ListenPostParametersVersion0)
]
