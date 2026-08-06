
# Get Project Distribution Credentials V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GetProjectDistributionCredentialsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member` | [`GetProjectDistributionCredentialsV1ResponseMember`](../../doc/models/get-project-distribution-credentials-v1-response-member.md) | Required | - |
| `distribution_credentials` | [`GetProjectDistributionCredentialsV1ResponseDistributionCredentials`](../../doc/models/get-project-distribution-credentials-v1-response-distribution-credentials.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.get_project_distribution_credentials_v_1_response import GetProjectDistributionCredentialsV1Response
from deepgram.models.get_project_distribution_credentials_v_1_response_distribution_credentials import GetProjectDistributionCredentialsV1ResponseDistributionCredentials
from deepgram.models.get_project_distribution_credentials_v_1_response_member import GetProjectDistributionCredentialsV1ResponseMember

get_project_distribution_credentials_v_1_response = GetProjectDistributionCredentialsV1Response(
    member=GetProjectDistributionCredentialsV1ResponseMember(
        member_id='00001922-0000-0000-0000-000000000000',
        email='email0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    distribution_credentials=GetProjectDistributionCredentialsV1ResponseDistributionCredentials(
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

