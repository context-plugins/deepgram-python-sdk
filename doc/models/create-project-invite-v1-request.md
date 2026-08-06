
# Create Project Invite V1 Request

Request body for creating a project invite

*This model accepts additional fields of type Any.*

## Structure

`CreateProjectInviteV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | The email address of the invitee |
| `scope` | `str` | Required | The scope of the invitee |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.create_project_invite_v_1_request import CreateProjectInviteV1Request

create_project_invite_v_1_request = CreateProjectInviteV1Request(
    email='email6',
    scope='scope8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

