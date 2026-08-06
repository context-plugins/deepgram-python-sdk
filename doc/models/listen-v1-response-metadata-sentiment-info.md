
# Listen V1 Response Metadata Sentiment Info

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseMetadataSentimentInfo`

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

from deepgram.models.listen_v_1_response_metadata_sentiment_info import ListenV1ResponseMetadataSentimentInfo

listen_v_1_response_metadata_sentiment_info = ListenV1ResponseMetadataSentimentInfo(
    model_uuid='model_uuid4',
    input_tokens=126,
    output_tokens=130,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

