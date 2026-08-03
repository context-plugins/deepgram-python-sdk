
# Get Project Key V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GetProjectKeyV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item` | [`GetProjectKeyV1ResponseItem`](../../doc/models/get-project-key-v1-response-item.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.get_project_key_v_1_response import GetProjectKeyV1Response
from restapi.models.get_project_key_v_1_response_item import GetProjectKeyV1ResponseItem
from restapi.models.get_project_key_v_1_response_item_member import GetProjectKeyV1ResponseItemMember
from restapi.models.get_project_key_v_1_response_item_member_api_key import GetProjectKeyV1ResponseItemMemberApiKey

get_project_key_v_1_response = GetProjectKeyV1Response(
    item=GetProjectKeyV1ResponseItem(
        member=GetProjectKeyV1ResponseItemMember(
            member_id='member_id4',
            email='email0',
            first_name='first_name6',
            last_name='last_name4',
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

