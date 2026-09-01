from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItems(str, Enum):
    SELF_HOSTED_PRODUCTS = "self-hosted:products"
    SELF_HOSTED_PRODUCT_API = "self-hosted:product:api"
    SELF_HOSTED_PRODUCT_ENGINE = "self-hosted:product:engine"
    SELF_HOSTED_PRODUCT_LICENSE_PROXY = "self-hosted:product:license-proxy"
    SELF_HOSTED_PRODUCT_DGTOOLS = "self-hosted:product:dgtools"
    SELF_HOSTED_PRODUCT_BILLING = "self-hosted:product:billing"
    SELF_HOSTED_PRODUCT_HOTPEPPER = "self-hosted:product:hotpepper"
    SELF_HOSTED_PRODUCT_METRICS_SERVER = "self-hosted:product:metrics-server"

    __str__ = str.__str__


V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItemsOrStr: TypeAlias = Annotated[
    V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItems | str,
    open_enum_validator(V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItems),
]
