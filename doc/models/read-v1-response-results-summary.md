
# Read V1 Response Results Summary

Output whenever `summary=true` is used

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseResultsSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `results` | [`ReadV1ResponseResultsSummaryResults`](../../doc/models/read-v1-response-results-summary-results.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.read_v_1_response_results_summary import ReadV1ResponseResultsSummary
from restapi.models.read_v_1_response_results_summary_results import ReadV1ResponseResultsSummaryResults
from restapi.models.read_v_1_response_results_summary_results_summary import ReadV1ResponseResultsSummaryResultsSummary

read_v_1_response_results_summary = ReadV1ResponseResultsSummary(
    results=ReadV1ResponseResultsSummaryResults(
        summary=ReadV1ResponseResultsSummaryResultsSummary(
            text='text8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

