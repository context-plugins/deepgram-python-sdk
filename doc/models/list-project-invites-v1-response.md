
# List Project Invites V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectInvitesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invites` | [`List[ListProjectInvitesV1ResponseInvitesItems]`](../../doc/models/list-project-invites-v1-response-invites-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_project_invites_v_1_response import ListProjectInvitesV1Response
from restapi.models.list_project_invites_v_1_response_invites_items import ListProjectInvitesV1ResponseInvitesItems

list_project_invites_v_1_response = ListProjectInvitesV1Response(
    invites=[
        ListProjectInvitesV1ResponseInvitesItems(
            email='email8',
            scope='scope4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListProjectInvitesV1ResponseInvitesItems(
            email='email8',
            scope='scope4',
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

