from __future__ import annotations

from typing import TypeAlias

from ..error_response_legacy_error import ErrorResponseLegacyError, ErrorResponseLegacyErrorDict
from ..error_response_modern_error import ErrorResponseModernError, ErrorResponseModernErrorDict

ErrorResponse: TypeAlias = str | ErrorResponseLegacyError | ErrorResponseModernError

ErrorResponseDict: TypeAlias = str | ErrorResponseLegacyErrorDict | ErrorResponseModernErrorDict
