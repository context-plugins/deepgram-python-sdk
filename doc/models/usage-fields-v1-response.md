
# Usage Fields V1 Response

*This model accepts additional fields of type Any.*

## Structure

`UsageFieldsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | `List[str]` | Optional | List of tags associated with the project |
| `models` | [`List[UsageFieldsV1ResponseModelsItems]`](../../doc/models/usage-fields-v1-response-models-items.md) | Optional | List of models available for the project. |
| `processing_methods` | `List[str]` | Optional | Processing methods supported by the API |
| `features` | `List[str]` | Optional | API features available to the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.usage_fields_v_1_response import UsageFieldsV1Response
from deepgram.models.usage_fields_v_1_response_models_items import UsageFieldsV1ResponseModelsItems

usage_fields_v_1_response = UsageFieldsV1Response(
    tags=[
        'tags9',
        'tags0',
        'tags1'
    ],
    models=[
        UsageFieldsV1ResponseModelsItems(
            name='name4',
            language='language6',
            version='version0',
            model_id='model_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        UsageFieldsV1ResponseModelsItems(
            name='name4',
            language='language6',
            version='version0',
            model_id='model_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        UsageFieldsV1ResponseModelsItems(
            name='name4',
            language='language6',
            version='version0',
            model_id='model_id4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    processing_methods=[
        'processing_methods4'
    ],
    features=[
        'features5',
        'features6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

