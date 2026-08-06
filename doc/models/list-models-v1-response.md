
# List Models V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListModelsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stt` | [`List[ListModelsV1ResponseSttModels]`](../../doc/models/list-models-v1-response-stt-models.md) | Optional | - |
| `tts` | [`List[ListModelsV1ResponseTtsModels]`](../../doc/models/list-models-v1-response-tts-models.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_models_v_1_response import ListModelsV1Response
from deepgram.models.list_models_v_1_response_stt_models import ListModelsV1ResponseSttModels
from deepgram.models.list_models_v_1_response_tts_models import ListModelsV1ResponseTtsModels

list_models_v_1_response = ListModelsV1Response(
    stt=[
        ListModelsV1ResponseSttModels(
            name='name6',
            canonical_name='canonical_name8',
            architecture='architecture4',
            languages=[
                'languages3',
                'languages4',
                'languages5'
            ],
            version='version2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    tts=[
        ListModelsV1ResponseTtsModels(
            name='name2',
            canonical_name='canonical_name2',
            architecture='architecture0',
            languages=[
                'languages1'
            ],
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListModelsV1ResponseTtsModels(
            name='name2',
            canonical_name='canonical_name2',
            architecture='architecture0',
            languages=[
                'languages1'
            ],
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListModelsV1ResponseTtsModels(
            name='name2',
            canonical_name='canonical_name2',
            architecture='architecture0',
            languages=[
                'languages1'
            ],
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

