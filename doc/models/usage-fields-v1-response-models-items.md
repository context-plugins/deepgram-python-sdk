
# Usage Fields V1 Response Models Items

*This model accepts additional fields of type Any.*

## Structure

`UsageFieldsV1ResponseModelsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the model. |
| `language` | `str` | Optional | The language supported by the model (IETF language tag). |
| `version` | `str` | Optional | Version identifier of the model, typically with a date and a revision number. |
| `model_id` | `str` | Optional | Unique identifier for the model. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.usage_fields_v_1_response_models_items import UsageFieldsV1ResponseModelsItems

usage_fields_v_1_response_models_items = UsageFieldsV1ResponseModelsItems(
    name='name8',
    language='language0',
    version='version4',
    model_id='model_id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

