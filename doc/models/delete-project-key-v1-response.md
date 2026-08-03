
# Delete Project Key V1 Response

*This model accepts additional fields of type Any.*

## Structure

`DeleteProjectKeyV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.delete_project_key_v_1_response import DeleteProjectKeyV1Response

delete_project_key_v_1_response = DeleteProjectKeyV1Response(
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

