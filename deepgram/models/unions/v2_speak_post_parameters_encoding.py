from __future__ import annotations

from typing import TypeAlias

from ..enums.v2_speak_post_parameters_encoding0 import V2SpeakPostParametersEncoding0OrStr
from ..enums.v2_speak_post_parameters_encoding1 import V2SpeakPostParametersEncoding1OrStr
from ..enums.v2_speak_post_parameters_encoding2 import V2SpeakPostParametersEncoding2OrStr
from ..enums.v2_speak_post_parameters_encoding3 import V2SpeakPostParametersEncoding3OrStr
from ..enums.v2_speak_post_parameters_encoding4 import V2SpeakPostParametersEncoding4OrStr
from ..enums.v2_speak_post_parameters_encoding5 import V2SpeakPostParametersEncoding5OrStr
from ..enums.v2_speak_post_parameters_encoding6 import V2SpeakPostParametersEncoding6OrStr

V2SpeakPostParametersEncoding: TypeAlias = (
    V2SpeakPostParametersEncoding0OrStr
    | V2SpeakPostParametersEncoding1OrStr
    | V2SpeakPostParametersEncoding2OrStr
    | V2SpeakPostParametersEncoding3OrStr
    | V2SpeakPostParametersEncoding4OrStr
    | V2SpeakPostParametersEncoding5OrStr
    | V2SpeakPostParametersEncoding6OrStr
)

V2SpeakPostParametersEncodingDict: TypeAlias = (
    V2SpeakPostParametersEncoding0OrStr
    | V2SpeakPostParametersEncoding1OrStr
    | V2SpeakPostParametersEncoding2OrStr
    | V2SpeakPostParametersEncoding3OrStr
    | V2SpeakPostParametersEncoding4OrStr
    | V2SpeakPostParametersEncoding5OrStr
    | V2SpeakPostParametersEncoding6OrStr
)
