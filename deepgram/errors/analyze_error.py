from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.unions.error_response import ErrorResponse

AnalyzeErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _AnalyzeError:
    def map(self, status_code: int, content: bytes) -> AnalyzeErrorBody:
        match status_code:
            case 400:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


analyze_error_mapper: Final[ErrorMapper[AnalyzeErrorBody]] = _AnalyzeError()
