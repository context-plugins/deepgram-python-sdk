
# List Project Balances V1 Response Balances Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectBalancesV1ResponseBalancesItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_id` | `str` | Optional | The unique identifier of the balance |
| `amount` | `float` | Optional | The amount of the balance<br><br>**Default**: `0` |
| `units` | `str` | Optional | The units of the balance, such as "USD" |
| `purchase_order_id` | `str` | Optional | Description or reference of the purchase |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_project_balances_v_1_response_balances_items import ListProjectBalancesV1ResponseBalancesItems

list_project_balances_v_1_response_balances_items = ListProjectBalancesV1ResponseBalancesItems(
    balance_id='balance_id6',
    amount=0,
    units='units8',
    purchase_order_id='purchase_order_id4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

