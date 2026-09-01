from __future__ import annotations

from typing import Any, Literal

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class AgentThinkModelsV1ResponseModelsItems3(SdkBaseModel):
    """Groq models"""

    id: Literal["openai/gpt-oss-20b"] = "openai/gpt-oss-20b"
    """The unique identifier of the Groq model"""

    name: str
    """The display name of the model"""

    provider: Any
    """The provider of the model"""


class AgentThinkModelsV1ResponseModelsItems3Dict(TypedDict):
    id: NotRequired[Literal["openai/gpt-oss-20b"]]
    name: str
    provider: Any
