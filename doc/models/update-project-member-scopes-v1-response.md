
# Update Project Member Scopes V1 Response

*This model accepts additional fields of type Any.*

## Structure

`UpdateProjectMemberScopesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | confirmation message |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.update_project_member_scopes_v_1_response import UpdateProjectMemberScopesV1Response

update_project_member_scopes_v_1_response = UpdateProjectMemberScopesV1Response(
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

