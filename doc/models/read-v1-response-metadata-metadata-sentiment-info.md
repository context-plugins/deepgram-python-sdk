
# Read V1 Response Metadata Metadata Sentiment Info

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadataMetadataSentimentInfo`

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

from deepgram.models.read_v_1_response_metadata_metadata_sentiment_info import ReadV1ResponseMetadataMetadataSentimentInfo

read_v_1_response_metadata_metadata_sentiment_info = ReadV1ResponseMetadataMetadataSentimentInfo(
    model_uuid='00000656-0000-0000-0000-000000000000',
    input_tokens=124,
    output_tokens=124,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

