
# List Project Keys V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectKeysV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_keys` | [`List[ListProjectKeysV1ResponseApiKeysItems]`](../../doc/models/list-project-keys-v1-response-api-keys-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.list_project_keys_v_1_response import ListProjectKeysV1Response
from restapi.models.list_project_keys_v_1_response_api_keys_items import ListProjectKeysV1ResponseApiKeysItems
from restapi.models.list_project_keys_v_1_response_api_keys_items_api_key import ListProjectKeysV1ResponseApiKeysItemsApiKey
from restapi.models.list_project_keys_v_1_response_api_keys_items_member import ListProjectKeysV1ResponseApiKeysItemsMember

list_project_keys_v_1_response = ListProjectKeysV1Response(
    api_keys=[
        ListProjectKeysV1ResponseApiKeysItems(
            member=ListProjectKeysV1ResponseApiKeysItemsMember(
                member_id='member_id4',
                email='email0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            api_key=ListProjectKeysV1ResponseApiKeysItemsApiKey(
                api_key_id='api_key_id6',
                comment='comment6',
                scopes=[
                    'scopes4',
                    'scopes3'
                ],
                created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

