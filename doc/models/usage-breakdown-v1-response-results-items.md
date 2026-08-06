
# Usage Breakdown V1 Response Results Items

*This model accepts additional fields of type Any.*

## Structure

`UsageBreakdownV1ResponseResultsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hours` | `float` | Required | Audio hours processed |
| `total_hours` | `float` | Required | Total hours including all processing |
| `agent_hours` | `float` | Required | Agent hours used |
| `tokens_in` | `float` | Required | Number of input tokens |
| `tokens_out` | `float` | Required | Number of output tokens |
| `tts_characters` | `float` | Required | Number of text-to-speech characters processed |
| `requests` | `float` | Required | Number of requests |
| `grouping` | [`UsageBreakdownV1ResponseResultsItemsGrouping`](../../doc/models/usage-breakdown-v1-response-results-items-grouping.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.usage_breakdown_v_1_response_results_items import UsageBreakdownV1ResponseResultsItems
from deepgram.models.usage_breakdown_v_1_response_results_items_grouping import UsageBreakdownV1ResponseResultsItemsGrouping

usage_breakdown_v_1_response_results_items = UsageBreakdownV1ResponseResultsItems(
    hours=183.64,
    total_hours=139.66,
    agent_hours=142.28,
    tokens_in=195.02,
    tokens_out=40,
    tts_characters=168.04,
    requests=200.3,
    grouping=UsageBreakdownV1ResponseResultsItemsGrouping(
        start=dateutil.parser.parse('2016-03-13').date(),
        end=dateutil.parser.parse('2016-03-13').date(),
        accessor='accessor6',
        endpoint='endpoint6',
        feature_set='feature_set2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

