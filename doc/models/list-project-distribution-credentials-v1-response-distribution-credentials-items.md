
# List Project Distribution Credentials V1 Response Distribution Credentials Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member` | [`ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember`](../../doc/models/list-project-distribution-credentials-v1-response-distribution-credentials-items-member.md) | Required | - |
| `distribution_credentials` | [`ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials`](../../doc/models/list-project-distribution-credentials-v1-response-distribution-credentials-items-distribution-credentials.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.list_project_distribution_credentials_v_1_response_distribution_credentials_items import ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItems
from deepgram.models.list_project_distribution_credentials_v_1_response_distribution_credentials_items_distribution_credentials import ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials
from deepgram.models.list_project_distribution_credentials_v_1_response_distribution_credentials_items_member import ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember

list_project_distribution_credentials_v_1_response_distribution_credentials_items = ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItems(
    member=ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsMember(
        member_id='00001922-0000-0000-0000-000000000000',
        email='email0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    distribution_credentials=ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials(
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

