
# Billing Breakdown V1 Response

*This model accepts additional fields of type Any.*

## Structure

`BillingBreakdownV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `date` | Required | Start date of the billing summmary period |
| `end` | `date` | Required | End date of the billing summary period |
| `resolution` | [`BillingBreakdownV1ResponseResolution`](../../doc/models/billing-breakdown-v1-response-resolution.md) | Required | - |
| `results` | [`List[BillingBreakdownV1ResponseResultsItems]`](../../doc/models/billing-breakdown-v1-response-results-items.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.billing_breakdown_v_1_response import BillingBreakdownV1Response
from deepgram.models.billing_breakdown_v_1_response_resolution import BillingBreakdownV1ResponseResolution
from deepgram.models.billing_breakdown_v_1_response_results_items import BillingBreakdownV1ResponseResultsItems
from deepgram.models.billing_breakdown_v_1_response_results_items_grouping import BillingBreakdownV1ResponseResultsItemsGrouping

billing_breakdown_v_1_response = BillingBreakdownV1Response(
    start=dateutil.parser.parse('2016-03-13').date(),
    end=dateutil.parser.parse('2016-03-13').date(),
    resolution=BillingBreakdownV1ResponseResolution(
        units='units8',
        amount=98.28,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    results=[
        BillingBreakdownV1ResponseResultsItems(
            dollars=41.68,
            grouping=BillingBreakdownV1ResponseResultsItemsGrouping(
                start=dateutil.parser.parse('2016-03-13').date(),
                end=dateutil.parser.parse('2016-03-13').date(),
                accessor='accessor6',
                deployment='deployment6',
                line_item='line_item8',
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

