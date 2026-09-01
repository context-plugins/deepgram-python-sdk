from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersRedactSchemaOneOf1Items(str, Enum):
    PCI = "pci"
    PII = "pii"
    NUMBERS = "numbers"

    __str__ = str.__str__


V1ListenPostParametersRedactSchemaOneOf1ItemsOrStr: TypeAlias = Annotated[
    V1ListenPostParametersRedactSchemaOneOf1Items | str,
    open_enum_validator(V1ListenPostParametersRedactSchemaOneOf1Items),
]
