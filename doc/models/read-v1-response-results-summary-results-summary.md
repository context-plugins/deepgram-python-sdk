
# Read V1 Response Results Summary Results Summary

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseResultsSummaryResultsSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.read_v_1_response_results_summary_results_summary import ReadV1ResponseResultsSummaryResultsSummary

read_v_1_response_results_summary_results_summary = ReadV1ResponseResultsSummaryResultsSummary(
    text='text6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

