
# Usage V1 Response

*This model accepts additional fields of type Any.*

## Structure

`UsageV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start` | `date` | Optional | - |
| `end` | `date` | Optional | - |
| `resolution` | [`UsageV1ResponseResolution`](../../doc/models/usage-v1-response-resolution.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.usage_v_1_response import UsageV1Response
from restapi.models.usage_v_1_response_resolution import UsageV1ResponseResolution

usage_v_1_response = UsageV1Response(
    start=dateutil.parser.parse('2016-03-13').date(),
    end=dateutil.parser.parse('2016-03-13').date(),
    resolution=UsageV1ResponseResolution(
        units='units8',
        amount=98.28,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

