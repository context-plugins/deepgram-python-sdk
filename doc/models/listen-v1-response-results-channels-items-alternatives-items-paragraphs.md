
# Listen V1 Response Results Channels Items Alternatives Items Paragraphs

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transcript` | `str` | Optional | - |
| `paragraphs` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-paragraphs-paragraphs-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems

listen_v_1_response_results_channels_items_alternatives_items_paragraphs = ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs(
    transcript='transcript6',
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

