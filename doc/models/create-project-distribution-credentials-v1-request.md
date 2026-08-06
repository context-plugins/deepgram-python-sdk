
# Create Project Distribution Credentials V1 Request

Request body for creating distribution credentials

*This model accepts additional fields of type Any.*

## Structure

`CreateProjectDistributionCredentialsV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `comment` | `str` | Optional | Optional comment about the credentials |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.create_project_distribution_credentials_v_1_request import CreateProjectDistributionCredentialsV1Request

create_project_distribution_credentials_v_1_request = CreateProjectDistributionCredentialsV1Request(
    comment='comment6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

