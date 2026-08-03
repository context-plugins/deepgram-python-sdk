
# Shared Topics Results Topics Segments Items Topics Items

*This model accepts additional fields of type Any.*

## Structure

`SharedTopicsResultsTopicsSegmentsItemsTopicsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `topic` | `str` | Optional | - |
| `confidence_score` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

shared_topics_results_topics_segments_items_topics_items = SharedTopicsResultsTopicsSegmentsItemsTopicsItems(
    topic='topic6',
    confidence_score=80.82,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

