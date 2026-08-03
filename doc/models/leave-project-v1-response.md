
# Leave Project V1 Response

*This model accepts additional fields of type Any.*

## Structure

`LeaveProjectV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.leave_project_v_1_response import LeaveProjectV1Response

leave_project_v_1_response = LeaveProjectV1Response(
    message='message0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

