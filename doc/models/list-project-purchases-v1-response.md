
# List Project Purchases V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectPurchasesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `orders` | [`List[ListProjectPurchasesV1ResponseOrdersItems]`](../../doc/models/list-project-purchases-v1-response-orders-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.list_project_purchases_v_1_response import ListProjectPurchasesV1Response
from restapi.models.list_project_purchases_v_1_response_orders_items import ListProjectPurchasesV1ResponseOrdersItems

list_project_purchases_v_1_response = ListProjectPurchasesV1Response(
    orders=[
        ListProjectPurchasesV1ResponseOrdersItems(
            order_id='00000d9e-0000-0000-0000-000000000000',
            expiration=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            amount=244.94,
            units='units2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListProjectPurchasesV1ResponseOrdersItems(
            order_id='00000d9e-0000-0000-0000-000000000000',
            expiration=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            amount=244.94,
            units='units2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListProjectPurchasesV1ResponseOrdersItems(
            order_id='00000d9e-0000-0000-0000-000000000000',
            expiration=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            amount=244.94,
            units='units2',
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

