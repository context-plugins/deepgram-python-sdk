
# Create Agent Configuration V1 Response

*This model accepts additional fields of type Any.*

## Structure

`CreateAgentConfigurationV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agent_id` | `str` | Required | The unique identifier of the newly created agent configuration |
| `config` | `Any` | Required | The parsed agent configuration object |
| `metadata` | `Dict[str, str]` | Optional | Metadata associated with the agent configuration |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.create_agent_configuration_v_1_response import CreateAgentConfigurationV1Response

create_agent_configuration_v_1_response = CreateAgentConfigurationV1Response(
    agent_id='agent_id8',
    config=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    metadata={
        'key0': 'metadata3'
    },
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

