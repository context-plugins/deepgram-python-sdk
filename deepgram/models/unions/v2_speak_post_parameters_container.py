from __future__ import annotations

from typing import TypeAlias

from ..enums.v2_speak_post_parameters_container0 import V2SpeakPostParametersContainer0OrStr
from ..enums.v2_speak_post_parameters_container1 import V2SpeakPostParametersContainer1OrStr
from ..enums.v2_speak_post_parameters_container2 import V2SpeakPostParametersContainer2OrStr
from ..enums.v2_speak_post_parameters_container3 import V2SpeakPostParametersContainer3OrStr
from ..enums.v2_speak_post_parameters_container4 import V2SpeakPostParametersContainer4OrStr

V2SpeakPostParametersContainer: TypeAlias = (
    V2SpeakPostParametersContainer0OrStr
    | V2SpeakPostParametersContainer1OrStr
    | V2SpeakPostParametersContainer2OrStr
    | V2SpeakPostParametersContainer3OrStr
    | V2SpeakPostParametersContainer4OrStr
)

V2SpeakPostParametersContainerDict: TypeAlias = (
    V2SpeakPostParametersContainer0OrStr
    | V2SpeakPostParametersContainer1OrStr
    | V2SpeakPostParametersContainer2OrStr
    | V2SpeakPostParametersContainer3OrStr
    | V2SpeakPostParametersContainer4OrStr
)
