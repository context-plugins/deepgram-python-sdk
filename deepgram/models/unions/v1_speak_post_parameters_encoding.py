from __future__ import annotations

from typing import TypeAlias

from ..enums.v1_speak_post_parameters_encoding0 import V1SpeakPostParametersEncoding0OrStr
from ..enums.v1_speak_post_parameters_encoding1 import V1SpeakPostParametersEncoding1OrStr
from ..enums.v1_speak_post_parameters_encoding2 import V1SpeakPostParametersEncoding2OrStr
from ..enums.v1_speak_post_parameters_encoding3 import V1SpeakPostParametersEncoding3OrStr
from ..enums.v1_speak_post_parameters_encoding4 import V1SpeakPostParametersEncoding4OrStr
from ..enums.v1_speak_post_parameters_encoding5 import V1SpeakPostParametersEncoding5OrStr
from ..enums.v1_speak_post_parameters_encoding6 import V1SpeakPostParametersEncoding6OrStr

V1SpeakPostParametersEncoding: TypeAlias = (
    V1SpeakPostParametersEncoding0OrStr
    | V1SpeakPostParametersEncoding1OrStr
    | V1SpeakPostParametersEncoding2OrStr
    | V1SpeakPostParametersEncoding3OrStr
    | V1SpeakPostParametersEncoding4OrStr
    | V1SpeakPostParametersEncoding5OrStr
    | V1SpeakPostParametersEncoding6OrStr
)

V1SpeakPostParametersEncodingDict: TypeAlias = (
    V1SpeakPostParametersEncoding0OrStr
    | V1SpeakPostParametersEncoding1OrStr
    | V1SpeakPostParametersEncoding2OrStr
    | V1SpeakPostParametersEncoding3OrStr
    | V1SpeakPostParametersEncoding4OrStr
    | V1SpeakPostParametersEncoding5OrStr
    | V1SpeakPostParametersEncoding6OrStr
)
