from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, HttpResponse, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

AnalyzeErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _AnalyzeError:
    def map(self, response: HttpResponse) -> AnalyzeErrorBody:
        match response.status_code:
            case 400:
                return decode_json[ErrorResponse](response)
            case _:
                return RawError(response)


analyze_error_mapper: Final[ErrorMapper[AnalyzeErrorBody]] = _AnalyzeError()
