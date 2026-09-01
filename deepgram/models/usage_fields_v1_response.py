from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .usage_fields_v1_response_models_items import (
    UsageFieldsV1ResponseModelsItems,
    UsageFieldsV1ResponseModelsItemsDict,
)


class UsageFieldsV1Response(SdkBaseModel):
    tags: Optional[list[str]] = UNSET
    """List of tags associated with the project"""

    models: Optional[list[UsageFieldsV1ResponseModelsItems]] = UNSET
    """List of models available for the project."""

    processing_methods: Optional[list[str]] = UNSET
    """Processing methods supported by the API"""

    features: Optional[list[str]] = UNSET
    """API features available to the project"""


class UsageFieldsV1ResponseDict(TypedDict):
    tags: NotRequired[list[str]]
    models: NotRequired[list[UsageFieldsV1ResponseModelsItems | UsageFieldsV1ResponseModelsItemsDict]]
    processing_methods: NotRequired[list[str]]
    features: NotRequired[list[str]]
