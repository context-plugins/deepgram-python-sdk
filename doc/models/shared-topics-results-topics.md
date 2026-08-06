
# Shared Topics Results Topics

*This model accepts additional fields of type Any.*

## Structure

`SharedTopicsResultsTopics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segments` | [`List[SharedTopicsResultsTopicsSegmentsItems]`](../../doc/models/shared-topics-results-topics-segments-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.shared_topics_results_topics import SharedTopicsResultsTopics
from deepgram.models.shared_topics_results_topics_segments_items import SharedTopicsResultsTopicsSegmentsItems
from deepgram.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

shared_topics_results_topics = SharedTopicsResultsTopics(
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
        ),
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
        ),
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
)
```

