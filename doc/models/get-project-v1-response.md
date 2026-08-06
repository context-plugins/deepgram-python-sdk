
# Get Project V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GetProjectV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Optional | The unique identifier of the project |
| `mip_opt_out` | `bool` | Optional | Model Improvement Program opt-out |
| `name` | `str` | Optional | The name of the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.get_project_v_1_response import GetProjectV1Response

get_project_v_1_response = GetProjectV1Response(
    project_id='project_id0',
    mip_opt_out=False,
    name='name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

