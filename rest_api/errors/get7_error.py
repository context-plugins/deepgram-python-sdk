from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

Get7ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _Get7Error:
    def map(self, response: HttpResponse) -> Get7ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


get7_error_mapper: Final[ErrorMapper[Get7ErrorBody]] = _Get7Error()
