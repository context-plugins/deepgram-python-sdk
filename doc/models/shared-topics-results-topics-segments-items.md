
# Shared Topics Results Topics Segments Items

*This model accepts additional fields of type Any.*

## Structure

`SharedTopicsResultsTopicsSegmentsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `start_word` | `float` | Optional | - |
| `end_word` | `float` | Optional | - |
| `topics` | [`List[SharedTopicsResultsTopicsSegmentsItemsTopicsItems]`](../../doc/models/shared-topics-results-topics-segments-items-topics-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_topics_results_topics_segments_items import SharedTopicsResultsTopicsSegmentsItems
from restapi.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

shared_topics_results_topics_segments_items = SharedTopicsResultsTopicsSegmentsItems(
    text='text0',
    start_word=40.5,
    end_word=254.64,
    topics=[
        SharedTopicsResultsTopicsSegmentsItemsTopicsItems(
            topic='topic2',
            confidence_score=42.46,
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

