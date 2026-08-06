
# Listen V1 Response Metadata Summary Info

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseMetadataSummaryInfo`

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

from deepgram.models.listen_v_1_response_metadata_summary_info import ListenV1ResponseMetadataSummaryInfo

listen_v_1_response_metadata_summary_info = ListenV1ResponseMetadataSummaryInfo(
    model_uuid='model_uuid0',
    input_tokens=70,
    output_tokens=70,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

