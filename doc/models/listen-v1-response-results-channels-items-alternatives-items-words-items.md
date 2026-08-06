
# Listen V1 Response Results Channels Items Alternatives Items Words Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `str` | Optional | - |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `confidence` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_words_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems

listen_v_1_response_results_channels_items_alternatives_items_words_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
    word='word4',
    start=94.46,
    end=138.4,
    confidence=92.56,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

