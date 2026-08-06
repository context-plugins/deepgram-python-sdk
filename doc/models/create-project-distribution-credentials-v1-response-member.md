
# Create Project Distribution Credentials V1 Response Member

*This model accepts additional fields of type Any.*

## Structure

`CreateProjectDistributionCredentialsV1ResponseMember`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_id` | `uuid\|str` | Required | Unique identifier for the member |
| `email` | `str` | Required | Email address of the member |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.create_project_distribution_credentials_v_1_response_member import CreateProjectDistributionCredentialsV1ResponseMember

create_project_distribution_credentials_v_1_response_member = CreateProjectDistributionCredentialsV1ResponseMember(
    member_id='000007a2-0000-0000-0000-000000000000',
    email='email0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

