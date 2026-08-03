
# List Project Purchases V1 Response Orders Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectPurchasesV1ResponseOrdersItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `order_id` | `uuid\|str` | Optional | - |
| `expiration` | `datetime` | Optional | - |
| `created` | `datetime` | Optional | - |
| `amount` | `float` | Optional | - |
| `units` | `str` | Optional | - |
| `order_type` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.list_project_purchases_v_1_response_orders_items import ListProjectPurchasesV1ResponseOrdersItems

list_project_purchases_v_1_response_orders_items = ListProjectPurchasesV1ResponseOrdersItems(
    order_id='00001500-0000-0000-0000-000000000000',
    expiration=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    amount=51.84,
    units='units8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

