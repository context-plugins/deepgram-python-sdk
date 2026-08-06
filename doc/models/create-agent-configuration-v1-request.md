
# Create Agent Configuration V1 Request

Request body for creating an agent configuration

*This model accepts additional fields of type Any.*

## Structure

`CreateAgentConfigurationV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `config` | `str` | Required | A valid JSON string representing the agent block of a Settings message |
| `metadata` | `Dict[str, str]` | Optional | A map of arbitrary key-value pairs for labeling or organizing the agent configuration |
| `api_version` | `int` | Optional | API version. Defaults to 1<br><br>**Default**: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.create_agent_configuration_v_1_request import CreateAgentConfigurationV1Request

create_agent_configuration_v_1_request = CreateAgentConfigurationV1Request(
    config='config8',
    metadata={
        'key0': 'metadata9',
        'key1': 'metadata8'
    },
    api_version=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

