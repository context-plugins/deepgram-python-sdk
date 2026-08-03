
# List Project Keys V1 Response Api Keys Items Api Key

*This model accepts additional fields of type Any.*

## Structure

`ListProjectKeysV1ResponseApiKeysItemsApiKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `api_key_id` | `str` | Optional | - |
| `comment` | `str` | Optional | - |
| `scopes` | `List[str]` | Optional | - |
| `created` | `datetime` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.list_project_keys_v_1_response_api_keys_items_api_key import ListProjectKeysV1ResponseApiKeysItemsApiKey

list_project_keys_v_1_response_api_keys_items_api_key = ListProjectKeysV1ResponseApiKeysItemsApiKey(
    api_key_id='api_key_id8',
    comment='comment8',
    scopes=[
        'scopes2',
        'scopes1'
    ],
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

