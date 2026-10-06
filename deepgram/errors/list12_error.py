from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

List12ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _List12Error:
    def map(self, status_code: int, content: bytes) -> List12ErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


list12_error_mapper: Final[ErrorMapper[List12ErrorBody]] = _List12Error()
