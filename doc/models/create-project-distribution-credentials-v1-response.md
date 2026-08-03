
# Create Project Distribution Credentials V1 Response

*This model accepts additional fields of type Any.*

## Structure

`CreateProjectDistributionCredentialsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member` | [`CreateProjectDistributionCredentialsV1ResponseMember`](../../doc/models/create-project-distribution-credentials-v1-response-member.md) | Required | - |
| `distribution_credentials` | [`CreateProjectDistributionCredentialsV1ResponseDistributionCredentials`](../../doc/models/create-project-distribution-credentials-v1-response-distribution-credentials.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.create_project_distribution_credentials_v_1_response import CreateProjectDistributionCredentialsV1Response
from restapi.models.create_project_distribution_credentials_v_1_response_distribution_credentials import CreateProjectDistributionCredentialsV1ResponseDistributionCredentials
from restapi.models.create_project_distribution_credentials_v_1_response_member import CreateProjectDistributionCredentialsV1ResponseMember

create_project_distribution_credentials_v_1_response = CreateProjectDistributionCredentialsV1Response(
    member=CreateProjectDistributionCredentialsV1ResponseMember(
        member_id='00001922-0000-0000-0000-000000000000',
        email='email0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    distribution_credentials=CreateProjectDistributionCredentialsV1ResponseDistributionCredentials(
        distribution_credentials_id='00000560-0000-0000-0000-000000000000',
        provider='provider4',
        scopes=[
            'scopes8',
            'scopes9'
        ],
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        comment='comment2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

