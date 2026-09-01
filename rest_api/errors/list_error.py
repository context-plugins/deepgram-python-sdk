from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

ListErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ListError:
    def map(self, response: HttpResponse) -> ListErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


list_error_mapper: Final[ErrorMapper[ListErrorBody]] = _ListError()
