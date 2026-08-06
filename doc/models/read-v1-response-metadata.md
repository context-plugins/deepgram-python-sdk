
# Read V1 Response Metadata

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`ReadV1ResponseMetadataMetadata`](../../doc/models/read-v1-response-metadata-metadata.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.read_v_1_response_metadata import ReadV1ResponseMetadata
from deepgram.models.read_v_1_response_metadata_metadata import ReadV1ResponseMetadataMetadata
from deepgram.models.read_v_1_response_metadata_metadata_sentiment_info import ReadV1ResponseMetadataMetadataSentimentInfo
from deepgram.models.read_v_1_response_metadata_metadata_summary_info import ReadV1ResponseMetadataMetadataSummaryInfo

read_v_1_response_metadata = ReadV1ResponseMetadata(
    metadata=ReadV1ResponseMetadataMetadata(
        request_id='000018ae-0000-0000-0000-000000000000',
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

