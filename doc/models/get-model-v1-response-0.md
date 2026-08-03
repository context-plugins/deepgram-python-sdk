
# Get Model V1 Response 0

*This model accepts additional fields of type Any.*

## Structure

`GetModelV1Response0`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `canonical_name` | `str` | Optional | - |
| `architecture` | `str` | Optional | - |
| `languages` | `List[str]` | Optional | - |
| `version` | `str` | Optional | - |
| `uuid` | `uuid\|str` | Optional | - |
| `batch` | `bool` | Optional | - |
| `streaming` | `bool` | Optional | - |
| `formatted_output` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.get_model_v_1_response_0 import GetModelV1Response0

get_model_v_1_response_0 = GetModelV1Response0(
    name='name8',
    canonical_name='canonical_name6',
    architecture='architecture6',
    languages=[
        'languages5',
        'languages6'
    ],
    version='version4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

