from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class CreateAgentVariableV1Request(SdkBaseModel):
    """Request body for creating an agent variable"""

    key: str
    """The variable name, following the DG_<VARIABLE_NAME> format"""

    value: Any
    """The value to substitute. Can be any valid JSON type (string, number, boolean, object, or array)"""

    api_version: int = 1
    """API version. Defaults to 1"""


class CreateAgentVariableV1RequestDict(TypedDict):
    key: str
    value: Any
    api_version: NotRequired[int]
