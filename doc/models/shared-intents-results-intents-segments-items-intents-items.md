
# Shared Intents Results Intents Segments Items Intents Items

*This model accepts additional fields of type Any.*

## Structure

`SharedIntentsResultsIntentsSegmentsItemsIntentsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `intent` | `str` | Optional | - |
| `confidence_score` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.shared_intents_results_intents_segments_items_intents_items import SharedIntentsResultsIntentsSegmentsItemsIntentsItems

shared_intents_results_intents_segments_items_intents_items = SharedIntentsResultsIntentsSegmentsItemsIntentsItems(
    intent='intent6',
    confidence_score=115.4,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

