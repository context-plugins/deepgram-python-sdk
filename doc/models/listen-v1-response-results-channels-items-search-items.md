
# Listen V1 Response Results Channels Items Search Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsSearchItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query` | `str` | Optional | - |
| `hits` | [`List[ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems]`](../../doc/models/listen-v1-response-results-channels-items-search-items-hits-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_search_items import ListenV1ResponseResultsChannelsItemsSearchItems
from restapi.models.listen_v_1_response_results_channels_items_search_items_hits_items import ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems

listen_v_1_response_results_channels_items_search_items = ListenV1ResponseResultsChannelsItemsSearchItems(
    query='query6',
    hits=[
        ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(
            confidence=144.74,
            start=146.64,
            end=190.58,
            snippet='snippet0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(
            confidence=144.74,
            start=146.64,
            end=190.58,
            snippet='snippet0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

