from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.listen_v1_response import ListenV1Response

TranscribeErrorBody: TypeAlias = ListenV1Response | RawError


@dataclass(frozen=True, slots=True)
class _TranscribeError:
    def map(self, response: HttpResponse) -> TranscribeErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ListenV1Response](response)
            case _:
                return RawError(response)


transcribe_error_mapper: Final[ErrorMapper[TranscribeErrorBody]] = _TranscribeError()
