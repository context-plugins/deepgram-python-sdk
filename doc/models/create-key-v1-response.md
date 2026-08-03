
# Create Key V1 Response

API key created

*This model accepts additional fields of type Any.*

## Structure

`CreateKeyV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key_id` | `str` | Optional | The unique identifier of the API key |
| `key` | `str` | Optional | The API key |
| `comment` | `str` | Optional | A comment for the API key |
| `scopes` | `List[str]` | Optional | The scopes for the API key |
| `tags` | `List[str]` | Optional | The tags for the API key |
| `expiration_date` | `datetime` | Optional | The expiration date of the API key |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.create_key_v_1_response import CreateKeyV1Response

create_key_v_1_response = CreateKeyV1Response(
    api_key_id='api_key_id2',
    key='key8',
    comment='comment2',
    scopes=[
        'scopes6',
        'scopes5'
    ],
    tags=[
        'tags3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

