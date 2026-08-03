
# Shared Intents Results Intents

*This model accepts additional fields of type Any.*

## Structure

`SharedIntentsResultsIntents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[SharedIntentsResultsIntentsSegmentsItems]`](../../doc/models/shared-intents-results-intents-segments-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_intents_results_intents import SharedIntentsResultsIntents
from restapi.models.shared_intents_results_intents_segments_items import SharedIntentsResultsIntentsSegmentsItems
from restapi.models.shared_intents_results_intents_segments_items_intents_items import SharedIntentsResultsIntentsSegmentsItemsIntentsItems

shared_intents_results_intents = SharedIntentsResultsIntents(
    segments=[
        SharedIntentsResultsIntentsSegmentsItems(
            text='text6',
            start_word=4.96,
            end_word=219.1,
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
        ),
        SharedIntentsResultsIntentsSegmentsItems(
            text='text6',
            start_word=4.96,
            end_word=219.1,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

