
# List Project Member Scopes V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectMemberScopesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scopes` | `List[str]` | Optional | The API scopes of the member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_project_member_scopes_v_1_response import ListProjectMemberScopesV1Response

list_project_member_scopes_v_1_response = ListProjectMemberScopesV1Response(
    scopes=[
        'scopes6',
        'scopes5'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

