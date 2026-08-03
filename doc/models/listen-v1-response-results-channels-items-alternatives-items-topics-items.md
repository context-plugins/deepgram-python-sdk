
# Listen V1 Response Results Channels Items Alternatives Items Topics Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `topics` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_topics_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems

listen_v_1_response_results_channels_items_alternatives_items_topics_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems(
    text='text0',
    start_word=98.6,
    end_word=115.54,
    topics=[
        'topics9'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

