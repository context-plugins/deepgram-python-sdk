
# Get Project Distribution Credentials V1 Response Member

*This model accepts additional fields of type Any.*

## Structure

`GetProjectDistributionCredentialsV1ResponseMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `uuid\|str` | Required | Unique identifier for the member |
| `email` | `str` | Required | Email address of the member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.get_project_distribution_credentials_v_1_response_member import GetProjectDistributionCredentialsV1ResponseMember

get_project_distribution_credentials_v_1_response_member = GetProjectDistributionCredentialsV1ResponseMember(
    member_id='00000f3a-0000-0000-0000-000000000000',
    email='email2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

