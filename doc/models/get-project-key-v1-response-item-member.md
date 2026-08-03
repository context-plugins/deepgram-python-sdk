
# Get Project Key V1 Response Item Member

*This model accepts additional fields of type Any.*

## Structure

`GetProjectKeyV1ResponseItemMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `api_key` | [`GetProjectKeyV1ResponseItemMemberApiKey`](../../doc/models/get-project-key-v1-response-item-member-api-key.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.get_project_key_v_1_response_item_member import GetProjectKeyV1ResponseItemMember
from restapi.models.get_project_key_v_1_response_item_member_api_key import GetProjectKeyV1ResponseItemMemberApiKey

get_project_key_v_1_response_item_member = GetProjectKeyV1ResponseItemMember(
    member_id='member_id0',
    email='email6',
    first_name='first_name0',
    last_name='last_name8',
    api_key=GetProjectKeyV1ResponseItemMemberApiKey(
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
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

