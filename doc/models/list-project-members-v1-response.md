
# List Project Members V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectMembersV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | [`List[ListProjectMembersV1ResponseMembersItems]`](../../doc/models/list-project-members-v1-response-members-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_project_members_v_1_response import ListProjectMembersV1Response
from restapi.models.list_project_members_v_1_response_members_items import ListProjectMembersV1ResponseMembersItems

list_project_members_v_1_response = ListProjectMembersV1Response(
    members=[
        ListProjectMembersV1ResponseMembersItems(
            member_id='member_id2',
            scopes=[
                'scopes4',
                'scopes5',
                'scopes6'
            ],
            email='email8',
            first_name='first_name8',
            last_name='last_name6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

