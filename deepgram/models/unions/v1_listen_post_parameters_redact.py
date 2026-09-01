from __future__ import annotations

from typing import TypeAlias

from ..enums.v1_listen_post_parameters_redact_schema_one_of1_items import (
    V1ListenPostParametersRedactSchemaOneOf1ItemsOrStr,
)

V1ListenPostParametersRedact: TypeAlias = str | list[V1ListenPostParametersRedactSchemaOneOf1ItemsOrStr]

V1ListenPostParametersRedactDict: TypeAlias = str | list[V1ListenPostParametersRedactSchemaOneOf1ItemsOrStr]
