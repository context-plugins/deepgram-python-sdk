
# Listen V1 Response Results Channels Items Alternatives Items Paragraphs Paragraphs Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sentences` | [`List[ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems]`](../../doc/models/listen-v1-response-results-channels-items-alternatives-items-paragraphs-paragraphs-items-sentences-items.md) | Optional | - |
| `speaker` | `int` | Optional | - |
| `num_words` | `int` | Optional | - |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems

listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
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
    speaker=194,
    num_words=130,
    start=37.66,
    end=81.6,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

