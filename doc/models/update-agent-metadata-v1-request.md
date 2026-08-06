
# Update Agent Metadata V1 Request

Request body for updating agent configuration metadata

*This model accepts additional fields of type Any.*

## Structure

`UpdateAgentMetadataV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | `Dict[str, str]` | Required | A map of string key-value pairs to associate with this agent configuration |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.update_agent_metadata_v_1_request import UpdateAgentMetadataV1Request

update_agent_metadata_v_1_request = UpdateAgentMetadataV1Request(
    metadata={
        'key0': 'metadata5',
        'key1': 'metadata6'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

