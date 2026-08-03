
# Listen V1 Response Results Summary

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResultsSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | `str` | Optional | - |
| `short` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.listen_v_1_response_results_summary import ListenV1ResponseResultsSummary

listen_v_1_response_results_summary = ListenV1ResponseResultsSummary(
    result='result0',
    short='short2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

