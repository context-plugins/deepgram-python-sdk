
# List Agent Configurations V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListAgentConfigurationsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agents` | [`List[AgentConfigurationV1]`](../../doc/models/agent-configuration-v1.md) | Optional | A list of agent configurations for the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.agent_configuration_v_1 import AgentConfigurationV1
from deepgram.models.list_agent_configurations_v_1_response import ListAgentConfigurationsV1Response

list_agent_configurations_v_1_response = ListAgentConfigurationsV1Response(
    agents=[
        AgentConfigurationV1(
            agent_id='agent_id8',
            config=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            metadata={
                'key0': 'metadata3',
                'key1': 'metadata4'
            },
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AgentConfigurationV1(
            agent_id='agent_id8',
            config=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            metadata={
                'key0': 'metadata3',
                'key1': 'metadata4'
            },
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AgentConfigurationV1(
            agent_id='agent_id8',
            config=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            metadata={
                'key0': 'metadata3',
                'key1': 'metadata4'
            },
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

