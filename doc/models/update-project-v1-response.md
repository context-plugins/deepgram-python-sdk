
# Update Project V1 Response

*This model accepts additional fields of type Any.*

## Structure

`UpdateProjectV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.update_project_v_1_response import UpdateProjectV1Response

update_project_v_1_response = UpdateProjectV1Response(
    message='message2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

