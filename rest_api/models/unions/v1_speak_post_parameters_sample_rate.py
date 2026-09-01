from __future__ import annotations

from typing import TypeAlias

from ..enums.v1_speak_post_parameters_sample_rate0 import V1SpeakPostParametersSampleRate0OrStr
from ..enums.v1_speak_post_parameters_sample_rate1 import V1SpeakPostParametersSampleRate1OrStr
from ..enums.v1_speak_post_parameters_sample_rate2 import V1SpeakPostParametersSampleRate2OrStr
from ..enums.v1_speak_post_parameters_sample_rate3 import V1SpeakPostParametersSampleRate3OrStr
from ..enums.v1_speak_post_parameters_sample_rate4 import V1SpeakPostParametersSampleRate4OrStr

V1SpeakPostParametersSampleRate: TypeAlias = (
    V1SpeakPostParametersSampleRate0OrStr
    | V1SpeakPostParametersSampleRate1OrStr
    | V1SpeakPostParametersSampleRate2OrStr
    | V1SpeakPostParametersSampleRate3OrStr
    | V1SpeakPostParametersSampleRate4OrStr
)

V1SpeakPostParametersSampleRateDict: TypeAlias = (
    V1SpeakPostParametersSampleRate0OrStr
    | V1SpeakPostParametersSampleRate1OrStr
    | V1SpeakPostParametersSampleRate2OrStr
    | V1SpeakPostParametersSampleRate3OrStr
    | V1SpeakPostParametersSampleRate4OrStr
)
