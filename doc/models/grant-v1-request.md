
# Grant V1 Request

*This model accepts additional fields of type Any.*

## Structure

`GrantV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ttl_seconds` | `float` | Optional | Time to live in seconds for the token. Defaults to 30 seconds. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.grant_v_1_request import GrantV1Request

grant_v_1_request = GrantV1Request(
    ttl_seconds=138.18,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

