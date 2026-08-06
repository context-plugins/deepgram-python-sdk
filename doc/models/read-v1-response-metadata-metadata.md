
# Read V1 Response Metadata Metadata

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadataMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Optional | - |
| `created` | `datetime` | Optional | - |
| `language` | `str` | Optional | - |
| `summary_info` | [`ReadV1ResponseMetadataMetadataSummaryInfo`](../../doc/models/read-v1-response-metadata-metadata-summary-info.md) | Optional | - |
| `sentiment_info` | [`ReadV1ResponseMetadataMetadataSentimentInfo`](../../doc/models/read-v1-response-metadata-metadata-sentiment-info.md) | Optional | - |
| `topics_info` | [`ReadV1ResponseMetadataMetadataTopicsInfo`](../../doc/models/read-v1-response-metadata-metadata-topics-info.md) | Optional | - |
| `intents_info` | [`ReadV1ResponseMetadataMetadataIntentsInfo`](../../doc/models/read-v1-response-metadata-metadata-intents-info.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.read_v_1_response_metadata_metadata import ReadV1ResponseMetadataMetadata
from deepgram.models.read_v_1_response_metadata_metadata_sentiment_info import ReadV1ResponseMetadataMetadataSentimentInfo
from deepgram.models.read_v_1_response_metadata_metadata_summary_info import ReadV1ResponseMetadataMetadataSummaryInfo

read_v_1_response_metadata_metadata = ReadV1ResponseMetadataMetadata(
    request_id='00000106-0000-0000-0000-000000000000',
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    language='language8',
    summary_info=ReadV1ResponseMetadataMetadataSummaryInfo(
        model_uuid='00000e32-0000-0000-0000-000000000000',
        input_tokens=120,
        output_tokens=120,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sentiment_info=ReadV1ResponseMetadataMetadataSentimentInfo(
        model_uuid='00001640-0000-0000-0000-000000000000',
        input_tokens=86,
        output_tokens=86,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

