
# Update Project V1 Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateProjectV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | The name of the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.update_project_v_1_request import UpdateProjectV1Request

update_project_v_1_request = UpdateProjectV1Request(
    name='name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

