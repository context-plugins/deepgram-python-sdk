
# Update Project Member Scopes V1 Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateProjectMemberScopesV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scope` | `str` | Required | A scope to update |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.update_project_member_scopes_v_1_request import UpdateProjectMemberScopesV1Request

update_project_member_scopes_v_1_request = UpdateProjectMemberScopesV1Request(
    scope='scope6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

