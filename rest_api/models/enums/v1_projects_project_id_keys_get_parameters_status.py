from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdKeysGetParametersStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"

    __str__ = str.__str__


V1ProjectsProjectIdKeysGetParametersStatusOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdKeysGetParametersStatus | str, open_enum_validator(V1ProjectsProjectIdKeysGetParametersStatus)
]
