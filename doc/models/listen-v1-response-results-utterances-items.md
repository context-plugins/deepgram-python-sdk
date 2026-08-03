
# Listen V1 Response Results Utterances Items

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsUtterancesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `float` | Optional | - |
| `end` | `float` | Optional | - |
| `confidence` | `float` | Optional | - |
| `channel` | `int` | Optional | - |
| `transcript` | `str` | Optional | - |
| `words` | [`List[ListenV1ResponseResultsUtterancesItemsWordsItems]`](../../doc/models/listen-v1-response-results-utterances-items-words-items.md) | Optional | - |
| `speaker` | `int` | Optional | - |
| `id` | `uuid\|str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_utterances_items import ListenV1ResponseResultsUtterancesItems

listen_v_1_response_results_utterances_items = ListenV1ResponseResultsUtterancesItems(
    start=177.6,
    end=221.54,
    confidence=175.7,
    channel=236,
    transcript='transcript8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

