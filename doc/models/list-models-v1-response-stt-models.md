
# List Models V1 Response Stt Models

*This model accepts additional fields of type Any.*

## Structure

`ListModelsV1ResponseSttModels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `canonical_name` | `str` | Optional | - |
| `architecture` | `str` | Optional | - |
| `languages` | `List[str]` | Optional | - |
| `version` | `str` | Optional | - |
| `uuid` | `str` | Optional | - |
| `batch` | `bool` | Optional | - |
| `streaming` | `bool` | Optional | - |
| `formatted_output` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_models_v_1_response_stt_models import ListModelsV1ResponseSttModels

list_models_v_1_response_stt_models = ListModelsV1ResponseSttModels(
    name='name0',
    canonical_name='canonical_name4',
    architecture='architecture8',
    languages=[
        'languages7',
        'languages8',
        'languages9'
    ],
    version='version6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

