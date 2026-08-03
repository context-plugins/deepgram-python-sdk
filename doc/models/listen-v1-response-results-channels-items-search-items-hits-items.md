
# Listen V1 Response Results Channels Items Search Items Hits Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `confidence` | `float` | Optional | - |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `snippet` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_search_items_hits_items import ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems

listen_v_1_response_results_channels_items_search_items_hits_items = ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(
    confidence=54.38,
    start=56.28,
    end=100.22,
    snippet='snippet4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

