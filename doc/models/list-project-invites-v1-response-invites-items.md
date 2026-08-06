
# List Project Invites V1 Response Invites Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectInvitesV1ResponseInvitesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The email address of the invitee |
| `scope` | `str` | Optional | The scope of the invitee |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_project_invites_v_1_response_invites_items import ListProjectInvitesV1ResponseInvitesItems

list_project_invites_v_1_response_invites_items = ListProjectInvitesV1ResponseInvitesItems(
    email='email6',
    scope='scope2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

