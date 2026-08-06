
# Get Project Balance V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GetProjectBalanceV1Response`

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

from deepgram.models.get_project_balance_v_1_response import GetProjectBalanceV1Response

get_project_balance_v_1_response = GetProjectBalanceV1Response(
    balance_id='balance_id4',
    amount=0,
    units='units6',
    purchase_order_id='purchase_order_id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

