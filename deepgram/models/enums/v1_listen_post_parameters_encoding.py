from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersEncoding(str, Enum):
    LINEAR16 = "linear16"
    FLAC = "flac"
    MULAW = "mulaw"
    AMR_NB = "amr-nb"
    AMR_WB = "amr-wb"
    OPUS = "opus"
    SPEEX = "speex"
    G729 = "g729"

    __str__ = str.__str__


V1ListenPostParametersEncodingOrStr: TypeAlias = Annotated[
    V1ListenPostParametersEncoding | str, open_enum_validator(V1ListenPostParametersEncoding)
]
