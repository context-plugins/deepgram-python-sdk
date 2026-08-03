
# Read V1 Response Results Summary Results

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseResultsSummaryResults`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `summary` | [`ReadV1ResponseResultsSummaryResultsSummary`](../../doc/models/read-v1-response-results-summary-results-summary.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.read_v_1_response_results_summary_results import ReadV1ResponseResultsSummaryResults
from restapi.models.read_v_1_response_results_summary_results_summary import ReadV1ResponseResultsSummaryResultsSummary

read_v_1_response_results_summary_results = ReadV1ResponseResultsSummaryResults(
    summary=ReadV1ResponseResultsSummaryResultsSummary(
        text='text8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

