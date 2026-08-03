
# Error Response Legacy Error

*This model accepts additional fields of type Any.*

## Structure

`ErrorResponseLegacyError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `err_code` | `str` | Optional | The error code |
| `err_msg` | `str` | Optional | The error message |
| `request_id` | `str` | Optional | The request ID |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.error_response_legacy_error import ErrorResponseLegacyError

error_response_legacy_error = ErrorResponseLegacyError(
    err_code='err_code2',
    err_msg='err_msg4',
    request_id='request_id4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

