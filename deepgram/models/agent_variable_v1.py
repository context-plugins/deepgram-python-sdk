from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class AgentVariableV1(SdkBaseModel):
    """A template variable for agent configurations"""

    variable_id: str
    """The unique identifier of the variable"""

    key: str
    """The variable name, following the DG_<VARIABLE_NAME> format"""

    value: Any
    """The value to substitute. Can be any valid JSON type"""

    created_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp when the variable was created"""

    updated_at: Optional[RFC3339DateTime] = UNSET
    """Timestamp when the variable was last updated"""


class AgentVariableV1Dict(TypedDict):
    variable_id: str
    key: str
    value: Any
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
