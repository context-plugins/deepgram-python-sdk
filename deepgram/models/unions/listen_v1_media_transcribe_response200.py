from __future__ import annotations

from typing import TypeAlias

from ..listen_v1_accepted_response import ListenV1AcceptedResponse, ListenV1AcceptedResponseDict
from ..listen_v1_response import ListenV1Response, ListenV1ResponseDict

ListenV1MediaTranscribeResponse200: TypeAlias = ListenV1Response | ListenV1AcceptedResponse

ListenV1MediaTranscribeResponse200Dict: TypeAlias = ListenV1ResponseDict | ListenV1AcceptedResponseDict
