
# List Project Distribution Credentials V1 Response Distribution Credentials Items Member

*This model accepts additional fields of type Any.*

## Structure

`ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `uuid\|str` | Required | Unique identifier for the member |
| `email` | `str` | Required | Email address of the member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_project_distribution_credentials_v_1_response_distribution_credentials_items_member import ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember

list_project_distribution_credentials_v_1_response_distribution_credentials_items_member = ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember(
    member_id='000003a6-0000-0000-0000-000000000000',
    email='email0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

