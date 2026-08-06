
# Listen V1 Response Metadata

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_key` | `str` | Optional | **Default**: `"deprecated"` |
| `request_id` | `uuid\|str` | Required | - |
| `sha_256` | `str` | Required | - |
| `created` | `datetime` | Required | - |
| `duration` | `float` | Required | - |
| `channels` | `int` | Required | - |
| `models` | `List[str]` | Required | - |
| `model_info` | `Any` | Required | - |
| `summary_info` | [`ListenV1ResponseMetadataSummaryInfo`](../../doc/models/listen-v1-response-metadata-summary-info.md) | Optional | - |
| `sentiment_info` | [`ListenV1ResponseMetadataSentimentInfo`](../../doc/models/listen-v1-response-metadata-sentiment-info.md) | Optional | - |
| `topics_info` | [`ListenV1ResponseMetadataTopicsInfo`](../../doc/models/listen-v1-response-metadata-topics-info.md) | Optional | - |
| `intents_info` | [`ListenV1ResponseMetadataIntentsInfo`](../../doc/models/listen-v1-response-metadata-intents-info.md) | Optional | - |
| `tags` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.listen_v_1_response_metadata import ListenV1ResponseMetadata
from deepgram.models.listen_v_1_response_metadata_intents_info import ListenV1ResponseMetadataIntentsInfo
from deepgram.models.listen_v_1_response_metadata_sentiment_info import ListenV1ResponseMetadataSentimentInfo
from deepgram.models.listen_v_1_response_metadata_summary_info import ListenV1ResponseMetadataSummaryInfo
from deepgram.models.listen_v_1_response_metadata_topics_info import ListenV1ResponseMetadataTopicsInfo

listen_v_1_response_metadata = ListenV1ResponseMetadata(
    request_id='0000029e-0000-0000-0000-000000000000',
    sha_256='sha2560',
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    duration=194.14,
    channels=48,
    models=[
        'models4',
        'models5'
    ],
    model_info=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    transaction_key='deprecated',
    summary_info=ListenV1ResponseMetadataSummaryInfo(
        model_uuid='model_uuid4',
        input_tokens=120,
        output_tokens=120,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sentiment_info=ListenV1ResponseMetadataSentimentInfo(
        model_uuid='model_uuid6',
        input_tokens=86,
        output_tokens=86,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    topics_info=ListenV1ResponseMetadataTopicsInfo(
        model_uuid='model_uuid8',
        input_tokens=156,
        output_tokens=156,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    intents_info=ListenV1ResponseMetadataIntentsInfo(
        model_uuid='model_uuid6',
        input_tokens=198,
        output_tokens=198,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

