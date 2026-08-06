
# Read V1 Response Metadata Metadata Summary Info

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadataMetadataSummaryInfo`

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

from deepgram.models.read_v_1_response_metadata_metadata_summary_info import ReadV1ResponseMetadataMetadataSummaryInfo

read_v_1_response_metadata_metadata_summary_info = ReadV1ResponseMetadataMetadataSummaryInfo(
    model_uuid='00001f56-0000-0000-0000-000000000000',
    input_tokens=92,
    output_tokens=164,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

