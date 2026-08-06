
# Shared Intents Results Intents Segments Items

*This model accepts additional fields of type Any.*

## Structure

`SharedIntentsResultsIntentsSegmentsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `intents` | [`List[SharedIntentsResultsIntentsSegmentsItemsIntentsItems]`](../../doc/models/shared-intents-results-intents-segments-items-intents-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.shared_intents_results_intents_segments_items import SharedIntentsResultsIntentsSegmentsItems
from deepgram.models.shared_intents_results_intents_segments_items_intents_items import SharedIntentsResultsIntentsSegmentsItemsIntentsItems

shared_intents_results_intents_segments_items = SharedIntentsResultsIntentsSegmentsItems(
    text='text4',
    start_word=196.54,
    end_word=17.6,
    intents=[
        SharedIntentsResultsIntentsSegmentsItemsIntentsItems(
            intent='intent4',
            confidence_score=193.42,
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

