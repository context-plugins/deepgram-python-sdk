
# Billing Breakdown V1 Response Results Items

*This model accepts additional fields of type Any.*

## Structure

`BillingBreakdownV1ResponseResultsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dollars` | `float` | Required | USD cost of the billing for this grouping |
| `grouping` | [`BillingBreakdownV1ResponseResultsItemsGrouping`](../../doc/models/billing-breakdown-v1-response-results-items-grouping.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.billing_breakdown_v_1_response_results_items import BillingBreakdownV1ResponseResultsItems
from restapi.models.billing_breakdown_v_1_response_results_items_grouping import BillingBreakdownV1ResponseResultsItemsGrouping

billing_breakdown_v_1_response_results_items = BillingBreakdownV1ResponseResultsItems(
    dollars=165.44,
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
```

