
# Shared Sentiments Segments Items

*This model accepts additional fields of type Any.*

## Structure

`SharedSentimentsSegmentsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `sentiment` | `str` | Optional | - |
| `sentiment_score` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_sentiments_segments_items import SharedSentimentsSegmentsItems

shared_sentiments_segments_items = SharedSentimentsSegmentsItems(
    text='text2',
    start_word=75.18,
    end_word=33.32,
    sentiment='sentiment8',
    sentiment_score=147,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

