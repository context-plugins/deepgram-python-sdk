
# Shared Sentiments

Output whenever `sentiment=true` is used

*This model accepts additional fields of type Any.*

## Structure

`SharedSentiments`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[SharedSentimentsSegmentsItems]`](../../doc/models/shared-sentiments-segments-items.md) | Optional | - |
| `average` | [`SharedSentimentsAverage`](../../doc/models/shared-sentiments-average.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_sentiments import SharedSentiments
from restapi.models.shared_sentiments_average import SharedSentimentsAverage
from restapi.models.shared_sentiments_segments_items import SharedSentimentsSegmentsItems

shared_sentiments = SharedSentiments(
    segments=[
        SharedSentimentsSegmentsItems(
            text='text6',
            start_word=4.96,
            end_word=219.1,
            sentiment='sentiment6',
            sentiment_score=76.78,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SharedSentimentsSegmentsItems(
            text='text6',
            start_word=4.96,
            end_word=219.1,
            sentiment='sentiment6',
            sentiment_score=76.78,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        SharedSentimentsSegmentsItems(
            text='text6',
            start_word=4.96,
            end_word=219.1,
            sentiment='sentiment6',
            sentiment_score=76.78,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    average=SharedSentimentsAverage(
        sentiment='sentiment8',
        sentiment_score=2.7,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

