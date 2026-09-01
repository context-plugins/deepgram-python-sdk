from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

Delete3ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _Delete3Error:
    def map(self, response: HttpResponse) -> Delete3ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


delete3_error_mapper: Final[ErrorMapper[Delete3ErrorBody]] = _Delete3Error()
