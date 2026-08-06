
# Usage Breakdown V1 Response

*This model accepts additional fields of type Any.*

## Structure

`UsageBreakdownV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `date` | Required | Start date of the usage period |
| `end` | `date` | Required | End date of the usage period |
| `resolution` | [`UsageBreakdownV1ResponseResolution`](../../doc/models/usage-breakdown-v1-response-resolution.md) | Required | - |
| `results` | [`List[UsageBreakdownV1ResponseResultsItems]`](../../doc/models/usage-breakdown-v1-response-results-items.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.usage_breakdown_v_1_response import UsageBreakdownV1Response
from deepgram.models.usage_breakdown_v_1_response_resolution import UsageBreakdownV1ResponseResolution
from deepgram.models.usage_breakdown_v_1_response_results_items import UsageBreakdownV1ResponseResultsItems
from deepgram.models.usage_breakdown_v_1_response_results_items_grouping import UsageBreakdownV1ResponseResultsItemsGrouping

usage_breakdown_v_1_response = UsageBreakdownV1Response(
    start=dateutil.parser.parse('2016-03-13').date(),
    end=dateutil.parser.parse('2016-03-13').date(),
    resolution=UsageBreakdownV1ResponseResolution(
        units='units8',
        amount=98.28,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    results=[
        UsageBreakdownV1ResponseResultsItems(
            hours=127.36,
            total_hours=195.94,
            agent_hours=198.56,
            tokens_in=251.3,
            tokens_out=96.28,
            tts_characters=224.32,
            requests=144.02,
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

