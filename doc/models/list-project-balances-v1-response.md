
# List Project Balances V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectBalancesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balances` | [`List[ListProjectBalancesV1ResponseBalancesItems]`](../../doc/models/list-project-balances-v1-response-balances-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_project_balances_v_1_response import ListProjectBalancesV1Response
from deepgram.models.list_project_balances_v_1_response_balances_items import ListProjectBalancesV1ResponseBalancesItems

list_project_balances_v_1_response = ListProjectBalancesV1Response(
    balances=[
        ListProjectBalancesV1ResponseBalancesItems(
            balance_id='balance_id2',
            amount=149.62,
            units='units4',
            purchase_order_id='purchase_order_id0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListProjectBalancesV1ResponseBalancesItems(
            balance_id='balance_id2',
            amount=149.62,
            units='units4',
            purchase_order_id='purchase_order_id0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ListProjectBalancesV1ResponseBalancesItems(
            balance_id='balance_id2',
            amount=149.62,
            units='units4',
            purchase_order_id='purchase_order_id0',
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

