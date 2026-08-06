
# Delete Project V1 Response

*This model accepts additional fields of type Any.*

## Structure

`DeleteProjectV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | Confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.delete_project_v_1_response import DeleteProjectV1Response

delete_project_v_1_response = DeleteProjectV1Response(
    message='message2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

