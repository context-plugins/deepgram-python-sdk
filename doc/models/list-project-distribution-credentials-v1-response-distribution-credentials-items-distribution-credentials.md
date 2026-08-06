
# List Project Distribution Credentials V1 Response Distribution Credentials Items Distribution Credentials

*This model accepts additional fields of type Any.*

## Structure

`ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials`

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

from deepgram.models.list_project_distribution_credentials_v_1_response_distribution_credentials_items_distribution_credentials import ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials

list_project_distribution_credentials_v_1_response_distribution_credentials_items_distribution_credentials = ListProjectDistributionCredentialsV1ResponseDistributionCredentialsItemsDistributionCredentials(
    distribution_credentials_id='000011ca-0000-0000-0000-000000000000',
    provider='provider2',
    scopes=[
        'scopes4'
    ],
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    comment='comment0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

