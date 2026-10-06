from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_models_v1_response_stt_models import ListModelsV1ResponseSttModels, ListModelsV1ResponseSttModelsDict
from .list_models_v1_response_tts_models import ListModelsV1ResponseTtsModels, ListModelsV1ResponseTtsModelsDict


class ListModelsV1Response(SdkBaseModel):
    stt: Optional[list[ListModelsV1ResponseSttModels]] = UNSET
    tts: Optional[list[ListModelsV1ResponseTtsModels]] = UNSET


class ListModelsV1ResponseDict(TypedDict):
    stt: NotRequired[list[ListModelsV1ResponseSttModelsDict]]
    tts: NotRequired[list[ListModelsV1ResponseTtsModelsDict]]
