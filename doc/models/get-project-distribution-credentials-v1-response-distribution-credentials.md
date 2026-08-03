
# Get Project Distribution Credentials V1 Response Distribution Credentials

*This model accepts additional fields of type Any.*

## Structure

`GetProjectDistributionCredentialsV1ResponseDistributionCredentials`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distribution_credentials_id` | `uuid\|str` | Required | Unique identifier for the distribution credentials |
| `provider` | `str` | Required | The provider of the distribution service |
| `comment` | `str` | Optional | Optional comment about the credentials |
| `scopes` | `List[str]` | Required | List of permission scopes for the credentials |
| `created` | `datetime` | Required | Timestamp when the credentials were created |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.get_project_distribution_credentials_v_1_response_distribution_credentials import GetProjectDistributionCredentialsV1ResponseDistributionCredentials

get_project_distribution_credentials_v_1_response_distribution_credentials = GetProjectDistributionCredentialsV1ResponseDistributionCredentials(
    distribution_credentials_id='00000ea2-0000-0000-0000-000000000000',
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
)
```

