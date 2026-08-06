
# Billing Breakdown V1 Response Results Items Grouping

*This model accepts additional fields of type Any.*

## Structure

`BillingBreakdownV1ResponseResultsItemsGrouping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `date` | Optional | Start date for this group |
| `end` | `date` | Optional | End date for this group |
| `accessor` | `str` | Optional | Optional accessor identifier, null unless grouped by accessor. |
| `deployment` | `str` | Optional | Optional deployment identifier, null unless grouped by deployment. |
| `line_item` | `str` | Optional | Optional line item identifier, null unless grouped by line item. |
| `tags` | `List[str]` | Optional | Optional list of tags, null unless grouped by tags. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.billing_breakdown_v_1_response_results_items_grouping import BillingBreakdownV1ResponseResultsItemsGrouping

billing_breakdown_v_1_response_results_items_grouping = BillingBreakdownV1ResponseResultsItemsGrouping(
    start=dateutil.parser.parse('2016-03-13').date(),
    end=dateutil.parser.parse('2016-03-13').date(),
    accessor='accessor4',
    deployment='deployment4',
    line_item='line_item0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

