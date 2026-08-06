
# Shared Sentiments Average

*This model accepts additional fields of type Any.*

## Structure

`SharedSentimentsAverage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sentiment` | `str` | Optional | - |
| `sentiment_score` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.shared_sentiments_average import SharedSentimentsAverage

shared_sentiments_average = SharedSentimentsAverage(
    sentiment='sentiment4',
    sentiment_score=132.86,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

