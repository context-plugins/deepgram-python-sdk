from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItems(str, Enum):
    ACCESSOR = "accessor"
    DEPLOYMENT = "deployment"
    LINE_ITEM = "line_item"
    TAGS = "tags"

    __str__ = str.__str__


V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItems | str,
    open_enum_validator(V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItems),
]
