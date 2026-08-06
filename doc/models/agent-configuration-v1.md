
# Agent Configuration V1

A reusable agent configuration

*This model accepts additional fields of type Any.*

## Structure

`AgentConfigurationV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agent_id` | `str` | Required | The unique identifier of the agent configuration |
| `config` | `Any` | Required | The agent configuration object |
| `metadata` | `Dict[str, str]` | Optional | A map of arbitrary key-value pairs for labeling or organizing the agent configuration |
| `created_at` | `datetime` | Optional | Timestamp when the configuration was created |
| `updated_at` | `datetime` | Optional | Timestamp when the configuration was last updated |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.agent_configuration_v_1 import AgentConfigurationV1

agent_configuration_v_1 = AgentConfigurationV1(
    agent_id='agent_id4',
    config=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    metadata={
        'key0': 'metadata3',
        'key1': 'metadata2'
    },
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

