
# Get Project Key V1 Response Item Member Api Key

*This model accepts additional fields of type Any.*

## Structure

`GetProjectKeyV1ResponseItemMemberApiKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key_id` | `str` | Optional | - |
| `comment` | `str` | Optional | - |
| `scopes` | `List[str]` | Optional | - |
| `tags` | `List[str]` | Optional | - |
| `expiration_date` | `datetime` | Optional | - |
| `created` | `datetime` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.get_project_key_v_1_response_item_member_api_key import GetProjectKeyV1ResponseItemMemberApiKey

get_project_key_v_1_response_item_member_api_key = GetProjectKeyV1ResponseItemMemberApiKey(
    api_key_id='api_key_id6',
    comment='comment6',
    scopes=[
        'scopes4',
        'scopes3'
    ],
    tags=[
        'tags7',
        'tags8',
        'tags9'
    ],
    expiration_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

