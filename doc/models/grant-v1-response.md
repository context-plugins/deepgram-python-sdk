
# Grant V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GrantV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_token` | `str` | Required | JSON Web Token (JWT) |
| `expires_in` | `float` | Optional | Time in seconds until the JWT expires |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.grant_v_1_response import GrantV1Response

grant_v_1_response = GrantV1Response(
    access_token='access_token0',
    expires_in=120.12,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

