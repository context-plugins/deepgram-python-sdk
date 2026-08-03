
# Listen V1 Response Results Utterances Items Words Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsUtterancesItemsWordsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `word` | `str` | Optional | - |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `confidence` | `float` | Optional | - |
| `speaker` | `int` | Optional | - |
| `speaker_confidence` | `float` | Optional | - |
| `punctuated_word` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_utterances_items_words_items import ListenV1ResponseResultsUtterancesItemsWordsItems

listen_v_1_response_results_utterances_items_words_items = ListenV1ResponseResultsUtterancesItemsWordsItems(
    word='word6',
    start=244.48,
    end=32.42,
    confidence=242.58,
    speaker=140,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

