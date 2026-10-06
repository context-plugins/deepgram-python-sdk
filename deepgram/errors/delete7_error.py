from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

Delete7ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _Delete7Error:
    def map(self, status_code: int, content: bytes) -> Delete7ErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


delete7_error_mapper: Final[ErrorMapper[Delete7ErrorBody]] = _Delete7Error()
