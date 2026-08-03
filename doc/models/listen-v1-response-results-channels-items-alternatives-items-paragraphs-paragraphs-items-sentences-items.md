
# Listen V1 Response Results Channels Items Alternatives Items Paragraphs Paragraphs Items Sentences Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems

listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items = ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
    text='text2',
    start=247.96,
    end=35.9,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

