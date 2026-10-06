from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

List4ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _List4Error:
    def map(self, status_code: int, content: bytes) -> List4ErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


list4_error_mapper: Final[ErrorMapper[List4ErrorBody]] = _List4Error()
