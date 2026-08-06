
# Listen V1 Response Metadata Intents Info

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseMetadataIntentsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_uuid` | `str` | Optional | - |
| `input_tokens` | `int` | Optional | - |
| `output_tokens` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_response_metadata_intents_info import ListenV1ResponseMetadataIntentsInfo

listen_v_1_response_metadata_intents_info = ListenV1ResponseMetadataIntentsInfo(
    model_uuid='model_uuid2',
    input_tokens=226,
    output_tokens=226,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

