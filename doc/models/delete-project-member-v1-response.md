
# Delete Project Member V1 Response

*This model accepts additional fields of type Any.*

## Structure

`DeleteProjectMemberV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.delete_project_member_v_1_response import DeleteProjectMemberV1Response

delete_project_member_v_1_response = DeleteProjectMemberV1Response(
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

