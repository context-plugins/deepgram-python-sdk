
# Listen V1 Response Metadata Topics Info

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseMetadataTopicsInfo`

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

from restapi.models.listen_v_1_response_metadata_topics_info import ListenV1ResponseMetadataTopicsInfo

listen_v_1_response_metadata_topics_info = ListenV1ResponseMetadataTopicsInfo(
    model_uuid='model_uuid6',
    input_tokens=4,
    output_tokens=252,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

