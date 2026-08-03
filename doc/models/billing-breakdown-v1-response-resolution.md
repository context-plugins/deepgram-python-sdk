
# Billing Breakdown V1 Response Resolution

*This model accepts additional fields of type Any.*

## Structure

`BillingBreakdownV1ResponseResolution`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `units` | `str` | Required | Time unit for the resolution |
| `amount` | `float` | Required | Amount of units |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.billing_breakdown_v_1_response_resolution import BillingBreakdownV1ResponseResolution

billing_breakdown_v_1_response_resolution = BillingBreakdownV1ResponseResolution(
    units='units6',
    amount=178.6,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

