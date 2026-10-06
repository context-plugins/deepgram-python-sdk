from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.listen_v1_response import ListenV1Response

TranscribeErrorBody: TypeAlias = ListenV1Response | RawError


@dataclass(frozen=True, slots=True)
class _TranscribeError:
    def map(self, status_code: int, content: bytes) -> TranscribeErrorBody:
        match status_code:
            case 400:
                return decode_json[ListenV1Response](content)
            case _:
                return RawError(status_code, content)


transcribe_error_mapper: Final[ErrorMapper[TranscribeErrorBody]] = _TranscribeError()
