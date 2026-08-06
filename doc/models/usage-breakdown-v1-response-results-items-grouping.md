
# Usage Breakdown V1 Response Results Items Grouping

*This model accepts additional fields of type Any.*

## Structure

`UsageBreakdownV1ResponseResultsItemsGrouping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `date` | Optional | Start date for this group |
| `end` | `date` | Optional | End date for this group |
| `accessor` | `str` | Optional | Optional accessor identifier |
| `endpoint` | `str` | Optional | Optional endpoint identifier |
| `feature_set` | `str` | Optional | Optional feature set identifier |
| `models` | `List[str]` | Optional | - |
| `method` | `str` | Optional | Optional method identifier |
| `tags` | `List[str]` | Optional | Optional list of tags, null unless grouped by tags. |
| `deployment` | `str` | Optional | Optional deployment identifier |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.usage_breakdown_v_1_response_results_items_grouping import UsageBreakdownV1ResponseResultsItemsGrouping

usage_breakdown_v_1_response_results_items_grouping = UsageBreakdownV1ResponseResultsItemsGrouping(
    start=dateutil.parser.parse('2016-03-13').date(),
    end=dateutil.parser.parse('2016-03-13').date(),
    accessor='accessor0',
    endpoint='endpoint0',
    feature_set='feature_set8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

