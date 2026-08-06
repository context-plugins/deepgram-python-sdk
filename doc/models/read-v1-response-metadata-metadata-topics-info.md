
# Read V1 Response Metadata Metadata Topics Info

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadataMetadataTopicsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_uuid` | `uuid\|str` | Optional | - |
| `input_tokens` | `int` | Optional | - |
| `output_tokens` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.read_v_1_response_metadata_metadata_topics_info import ReadV1ResponseMetadataMetadataTopicsInfo

read_v_1_response_metadata_metadata_topics_info = ReadV1ResponseMetadataMetadataTopicsInfo(
    model_uuid='000013cc-0000-0000-0000-000000000000',
    input_tokens=210,
    output_tokens=46,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

