
# Shared Topics Results

*This model accepts additional fields of type Any.*

## Structure

`SharedTopicsResults`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `topics` | [`SharedTopicsResultsTopics`](../../doc/models/shared-topics-results-topics.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.shared_topics_results import SharedTopicsResults
from restapi.models.shared_topics_results_topics import SharedTopicsResultsTopics
from restapi.models.shared_topics_results_topics_segments_items import SharedTopicsResultsTopicsSegmentsItems
from restapi.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

shared_topics_results = SharedTopicsResults(
    topics=SharedTopicsResultsTopics(
        segments=[
            SharedTopicsResultsTopicsSegmentsItems(
                text='text6',
                start_word=4.96,
                end_word=219.1,
                topics=[
                    SharedTopicsResultsTopicsSegmentsItemsTopicsItems(
                        topic='topic2',
                        confidence_score=42.46,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
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
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

