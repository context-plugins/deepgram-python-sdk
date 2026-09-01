from __future__ import annotations

from typing import Any

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateAgentVariableV1Request(SdkBaseModel):
    """Request body for updating an agent variable"""

    value: Any
    """The new value to substitute"""


class UpdateAgentVariableV1RequestDict(TypedDict):
    value: Any
