from __future__ import annotations

from typing import TypeAlias

from ..enums.v2_speak_post_parameters_sample_rate0 import V2SpeakPostParametersSampleRate0OrStr
from ..enums.v2_speak_post_parameters_sample_rate1 import V2SpeakPostParametersSampleRate1OrStr
from ..enums.v2_speak_post_parameters_sample_rate2 import V2SpeakPostParametersSampleRate2OrStr
from ..enums.v2_speak_post_parameters_sample_rate3 import V2SpeakPostParametersSampleRate3OrStr

V2SpeakPostParametersSampleRate: TypeAlias = (
    V2SpeakPostParametersSampleRate0OrStr
    | V2SpeakPostParametersSampleRate1OrStr
    | V2SpeakPostParametersSampleRate2OrStr
    | V2SpeakPostParametersSampleRate3OrStr
)

V2SpeakPostParametersSampleRateDict: TypeAlias = (
    V2SpeakPostParametersSampleRate0OrStr
    | V2SpeakPostParametersSampleRate1OrStr
    | V2SpeakPostParametersSampleRate2OrStr
    | V2SpeakPostParametersSampleRate3OrStr
)
