from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class UsageFieldsV1ResponseModelsItems(SdkBaseModel):
    name: Optional[str] = UNSET
    """Name of the model."""

    language: Optional[str] = UNSET
    """The language supported by the model (IETF language tag)."""

    version: Optional[str] = UNSET
    """Version identifier of the model, typically with a date and a revision number."""

    model_id: Optional[str] = UNSET
    """Unique identifier for the model."""


class UsageFieldsV1ResponseModelsItemsDict(TypedDict):
    name: NotRequired[str]
    language: NotRequired[str]
    version: NotRequired[str]
    model_id: NotRequired[str]
