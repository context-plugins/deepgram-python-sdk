
# List Billing Fields V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListBillingFieldsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accessors` | `List[uuid\|str]` | Optional | List of accessor UUIDs for the time period |
| `deployments` | [`List[ListBillingFieldsV1ResponseDeploymentsItems]`](../../doc/models/list-billing-fields-v1-response-deployments-items.md) | Optional | List of deployment types for the time period |
| `tags` | `List[str]` | Optional | List of tags for the time period |
| `line_items` | `Dict[str, str]` | Optional | Map of line item names to human-readable descriptions for the time period |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.list_billing_fields_v_1_response import ListBillingFieldsV1Response
from restapi.models.list_billing_fields_v_1_response_deployments_items import ListBillingFieldsV1ResponseDeploymentsItems

list_billing_fields_v_1_response = ListBillingFieldsV1Response(
    accessors=[
        '0000051c-0000-0000-0000-000000000000',
        '0000051b-0000-0000-0000-000000000000'
    ],
    deployments=[
        ListBillingFieldsV1ResponseDeploymentsItems.DEDICATED
    ],
    tags=[
        'tags1',
        'tags2'
    ],
    line_items={
        'key0': 'line_items7',
        'key1': 'line_items6',
        'key2': 'line_items5'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

