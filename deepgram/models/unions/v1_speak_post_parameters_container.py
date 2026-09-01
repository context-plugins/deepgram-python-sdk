from __future__ import annotations

from typing import TypeAlias

from ..enums.v1_speak_post_parameters_container0 import V1SpeakPostParametersContainer0OrStr
from ..enums.v1_speak_post_parameters_container1 import V1SpeakPostParametersContainer1OrStr
from ..enums.v1_speak_post_parameters_container2 import V1SpeakPostParametersContainer2OrStr
from ..enums.v1_speak_post_parameters_container3 import V1SpeakPostParametersContainer3OrStr
from ..enums.v1_speak_post_parameters_container4 import V1SpeakPostParametersContainer4OrStr

V1SpeakPostParametersContainer: TypeAlias = (
    V1SpeakPostParametersContainer0OrStr
    | V1SpeakPostParametersContainer1OrStr
    | V1SpeakPostParametersContainer2OrStr
    | V1SpeakPostParametersContainer3OrStr
    | V1SpeakPostParametersContainer4OrStr
)

V1SpeakPostParametersContainerDict: TypeAlias = (
    V1SpeakPostParametersContainer0OrStr
    | V1SpeakPostParametersContainer1OrStr
    | V1SpeakPostParametersContainer2OrStr
    | V1SpeakPostParametersContainer3OrStr
    | V1SpeakPostParametersContainer4OrStr
)
