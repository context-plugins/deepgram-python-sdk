
# Listen V1 Response Results Channels Items Alternatives Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transcript` | `str` | Optional | - |
| `confidence` | `float` | Optional | - |
| `words` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-words-items.md) | Optional | - |
| `paragraphs` | [`ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-paragraphs.md) | Optional | - |
| `entities` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-entities-items.md) | Optional | - |
| `summaries` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsSummariesItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-summaries-items.md) | Optional | - |
| `topics` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsTopicsItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-topics-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items import ListenV1ResponseResultsChannelsItemsAlternativesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_entities_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_words_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems

listen_v_1_response_results_channels_items_alternatives_items = ListenV1ResponseResultsChannelsItemsAlternativesItems(
    transcript='transcript0',
    confidence=198.92,
    words=[
        ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
            word='word0',
            start=58.62,
            end=102.56,
            confidence=56.72,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    paragraphs=ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs(
        transcript='transcript2',
        paragraphs=[
            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                sentences=[
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                speaker=128,
                num_words=60,
                start=34.44,
                end=78.38,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                sentences=[
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                speaker=128,
                num_words=60,
                start=34.44,
                end=78.38,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                sentences=[
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                        text='text2',
                        start=16.92,
                        end=60.86,
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                speaker=128,
                num_words=60,
                start=34.44,
                end=78.38,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    entities=[
        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
            label='label0',
            value='value2',
            raw_value='raw_value6',
            confidence=136.04,
            start_word=101.8,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
            label='label0',
            value='value2',
            raw_value='raw_value6',
            confidence=136.04,
            start_word=101.8,
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

