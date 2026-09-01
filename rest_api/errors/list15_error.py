from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

List15ErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _List15Error:
    def map(self, response: HttpResponse) -> List15ErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


list15_error_mapper: Final[ErrorMapper[List15ErrorBody]] = _List15Error()
