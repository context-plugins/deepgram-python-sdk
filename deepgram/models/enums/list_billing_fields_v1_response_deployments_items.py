from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ListBillingFieldsV1ResponseDeploymentsItems(str, Enum):
    HOSTED = "hosted"
    BETA = "beta"
    SELF_HOSTED = "self-hosted"
    DEDICATED = "dedicated"

    __str__ = str.__str__


ListBillingFieldsV1ResponseDeploymentsItemsOrStr: TypeAlias = Annotated[
    ListBillingFieldsV1ResponseDeploymentsItems | str, open_enum_validator(ListBillingFieldsV1ResponseDeploymentsItems)
]
