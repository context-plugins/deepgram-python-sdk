from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1ListenPostParametersModel0(str, Enum):
    """Our public models available to all accounts"""

    NOVA_3 = "nova-3"
    NOVA_3_GENERAL = "nova-3-general"
    NOVA_3_MEDICAL = "nova-3-medical"
    NOVA_2 = "nova-2"
    NOVA_2_GENERAL = "nova-2-general"
    NOVA_2_MEETING = "nova-2-meeting"
    NOVA_2_FINANCE = "nova-2-finance"
    NOVA_2_CONVERSATIONALAI = "nova-2-conversationalai"
    NOVA_2_VOICEMAIL = "nova-2-voicemail"
    NOVA_2_VIDEO = "nova-2-video"
    NOVA_2_MEDICAL = "nova-2-medical"
    NOVA_2_DRIVETHRU = "nova-2-drivethru"
    NOVA_2_AUTOMOTIVE = "nova-2-automotive"
    NOVA = "nova"
    NOVA_GENERAL = "nova-general"
    NOVA_PHONECALL = "nova-phonecall"
    NOVA_MEDICAL = "nova-medical"
    ENHANCED = "enhanced"
    ENHANCED_GENERAL = "enhanced-general"
    ENHANCED_MEETING = "enhanced-meeting"
    ENHANCED_PHONECALL = "enhanced-phonecall"
    ENHANCED_FINANCE = "enhanced-finance"
    BASE = "base"
    MEETING = "meeting"
    PHONECALL = "phonecall"
    FINANCE = "finance"
    CONVERSATIONALAI = "conversationalai"
    VOICEMAIL = "voicemail"
    VIDEO = "video"

    __str__ = str.__str__


V1ListenPostParametersModel0OrStr: TypeAlias = Annotated[
    V1ListenPostParametersModel0 | str, open_enum_validator(V1ListenPostParametersModel0)
]
