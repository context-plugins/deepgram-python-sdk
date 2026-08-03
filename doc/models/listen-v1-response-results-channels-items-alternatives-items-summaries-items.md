
# Listen V1 Response Results Channels Items Alternatives Items Summaries Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summary` | `str` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_summaries_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems

listen_v_1_response_results_channels_items_alternatives_items_summaries_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems(
    summary='summary4',
    start_word=88.02,
    end_word=46.16,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

