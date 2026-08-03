
# List Project Members V1 Response Members Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectMembersV1ResponseMembersItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `str` | Optional | The unique identifier of the member |
| `scopes` | `List[str]` | Optional | The API scopes of the member |
| `email` | `str` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_project_members_v_1_response_members_items import ListProjectMembersV1ResponseMembersItems

list_project_members_v_1_response_members_items = ListProjectMembersV1ResponseMembersItems(
    member_id='member_id0',
    scopes=[
        'scopes6'
    ],
    email='email6',
    first_name='first_name0',
    last_name='last_name8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

