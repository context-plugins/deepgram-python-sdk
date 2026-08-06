
# List Models V1 Response Tts Models

*This model accepts additional fields of type Any.*

## Structure

`ListModelsV1ResponseTtsModels`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `canonical_name` | `str` | Optional | - |
| `architecture` | `str` | Optional | - |
| `languages` | `List[str]` | Optional | - |
| `version` | `str` | Optional | - |
| `uuid` | `uuid\|str` | Optional | - |
| `metadata` | [`ListModelsV1ResponseTtsModelsMetadata`](../../doc/models/list-models-v1-response-tts-models-metadata.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_models_v_1_response_tts_models import ListModelsV1ResponseTtsModels

list_models_v_1_response_tts_models = ListModelsV1ResponseTtsModels(
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

