from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

Get3ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _Get3Error:
    def map(self, status_code: int, content: bytes) -> Get3ErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


get3_error_mapper: Final[ErrorMapper[Get3ErrorBody]] = _Get3Error()
