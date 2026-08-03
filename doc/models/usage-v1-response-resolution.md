
# Usage V1 Response Resolution

*This model accepts additional fields of type Any.*

## Structure

`UsageV1ResponseResolution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units` | `str` | Optional | - |
| `amount` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.usage_v_1_response_resolution import UsageV1ResponseResolution

usage_v_1_response_resolution = UsageV1ResponseResolution(
    units='units4',
    amount=36.62,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

