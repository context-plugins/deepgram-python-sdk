
# Read V1 Response Results

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseResults`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summary` | [`ReadV1ResponseResultsSummary`](../../doc/models/read-v1-response-results-summary.md) | Optional | Output whenever `summary=true` is used |
| `topics` | [`SharedTopics`](../../doc/models/shared-topics.md) | Optional | Output whenever `topics=true` is used |
| `intents` | [`SharedIntents`](../../doc/models/shared-intents.md) | Optional | Output whenever `intents=true` is used |
| `sentiments` | [`SharedSentiments`](../../doc/models/shared-sentiments.md) | Optional | Output whenever `sentiment=true` is used |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.read_v_1_response_results import ReadV1ResponseResults
from restapi.models.read_v_1_response_results_summary import ReadV1ResponseResultsSummary
from restapi.models.read_v_1_response_results_summary_results import ReadV1ResponseResultsSummaryResults
from restapi.models.read_v_1_response_results_summary_results_summary import ReadV1ResponseResultsSummaryResultsSummary
from restapi.models.shared_intents import SharedIntents
from restapi.models.shared_intents_results import SharedIntentsResults
from restapi.models.shared_intents_results_intents import SharedIntentsResultsIntents
from restapi.models.shared_intents_results_intents_segments_items import SharedIntentsResultsIntentsSegmentsItems
from restapi.models.shared_intents_results_intents_segments_items_intents_items import SharedIntentsResultsIntentsSegmentsItemsIntentsItems
from restapi.models.shared_sentiments import SharedSentiments
from restapi.models.shared_sentiments_average import SharedSentimentsAverage
from restapi.models.shared_sentiments_segments_items import SharedSentimentsSegmentsItems
from restapi.models.shared_topics import SharedTopics
from restapi.models.shared_topics_results import SharedTopicsResults
from restapi.models.shared_topics_results_topics import SharedTopicsResultsTopics
from restapi.models.shared_topics_results_topics_segments_items import SharedTopicsResultsTopicsSegmentsItems
from restapi.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

read_v_1_response_results = ReadV1ResponseResults(
    summary=ReadV1ResponseResultsSummary(
        results=ReadV1ResponseResultsSummaryResults(
            summary=ReadV1ResponseResultsSummaryResultsSummary(
                text='text8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    topics=SharedTopics(
        results=SharedTopicsResults(
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
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    intents=SharedIntents(
        results=SharedIntentsResults(
            intents=SharedIntentsResultsIntents(
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
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sentiments=SharedSentiments(
        segments=[
            SharedSentimentsSegmentsItems(
                text='text6',
                start_word=4.96,
                end_word=219.1,
                sentiment='sentiment6',
                sentiment_score=76.78,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        average=SharedSentimentsAverage(
            sentiment='sentiment8',
            sentiment_score=2.7,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

