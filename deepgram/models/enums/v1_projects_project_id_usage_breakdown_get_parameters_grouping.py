from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdUsageBreakdownGetParametersGrouping(str, Enum):
    ACCESSOR = "accessor"
    ENDPOINT = "endpoint"
    FEATURE_SET = "feature_set"
    MODELS = "models"
    METHOD = "method"
    TAGS = "tags"
    DEPLOYMENT = "deployment"

    __str__ = str.__str__


V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdUsageBreakdownGetParametersGrouping | str,
    open_enum_validator(V1ProjectsProjectIdUsageBreakdownGetParametersGrouping),
]
