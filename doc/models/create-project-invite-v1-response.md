
# Create Project Invite V1 Response

*This model accepts additional fields of type Any.*

## Structure

`CreateProjectInviteV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.create_project_invite_v_1_response import CreateProjectInviteV1Response

create_project_invite_v_1_response = CreateProjectInviteV1Response(
    message='message4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

