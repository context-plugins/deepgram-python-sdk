
# Error Response Modern Error

*This model accepts additional fields of type Any.*

## Structure

`ErrorResponseModernError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `category` | `str` | Optional | The category of the error |
| `message` | `str` | Optional | A message about the error |
| `details` | `str` | Optional | A description of the error |
| `request_id` | `str` | Optional | The unique identifier of the request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.error_response_modern_error import ErrorResponseModernError

error_response_modern_error = ErrorResponseModernError(
    category='category4',
    message='message6',
    details='details6',
    request_id='request_id2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

