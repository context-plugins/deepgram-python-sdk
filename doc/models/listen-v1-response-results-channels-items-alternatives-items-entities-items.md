
# Listen V1 Response Results Channels Items Alternatives Items Entities Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `label` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `raw_value` | `str` | Optional | - |
| `confidence` | `float` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_entities_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems

listen_v_1_response_results_channels_items_alternatives_items_entities_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
    label='label2',
    value='value4',
    raw_value='raw_value8',
    confidence=254.06,
    start_word=16.22,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

