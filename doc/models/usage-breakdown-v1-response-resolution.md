
# Usage Breakdown V1 Response Resolution

*This model accepts additional fields of type Any.*

## Structure

`UsageBreakdownV1ResponseResolution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units` | `str` | Required | Time unit for the resolution |
| `amount` | `float` | Required | Amount of units |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.usage_breakdown_v_1_response_resolution import UsageBreakdownV1ResponseResolution

usage_breakdown_v_1_response_resolution = UsageBreakdownV1ResponseResolution(
    units='units2',
    amount=165.84,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

