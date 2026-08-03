
# List Project Keys V1 Response Api Keys Items Member

*This model accepts additional fields of type Any.*

## Structure

`ListProjectKeysV1ResponseApiKeysItemsMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_project_keys_v_1_response_api_keys_items_member import ListProjectKeysV1ResponseApiKeysItemsMember

list_project_keys_v_1_response_api_keys_items_member = ListProjectKeysV1ResponseApiKeysItemsMember(
    member_id='member_id0',
    email='email6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

