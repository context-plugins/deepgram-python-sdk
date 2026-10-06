from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

Get8ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _Get8Error:
    def map(self, status_code: int, content: bytes) -> Get8ErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


get8_error_mapper: Final[ErrorMapper[Get8ErrorBody]] = _Get8Error()
