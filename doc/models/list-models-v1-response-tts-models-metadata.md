
# List Models V1 Response Tts Models Metadata

*This model accepts additional fields of type Any.*

## Structure

`ListModelsV1ResponseTtsModelsMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accent` | `str` | Optional | - |
| `age` | `str` | Optional | - |
| `color` | `str` | Optional | - |
| `image` | `str` | Optional | - |
| `sample` | `str` | Optional | - |
| `tags` | `List[str]` | Optional | - |
| `use_cases` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_models_v_1_response_tts_models_metadata import ListModelsV1ResponseTtsModelsMetadata

list_models_v_1_response_tts_models_metadata = ListModelsV1ResponseTtsModelsMetadata(
    accent='accent0',
    age='age4',
    color='color0',
    image='image0',
    sample='sample2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

