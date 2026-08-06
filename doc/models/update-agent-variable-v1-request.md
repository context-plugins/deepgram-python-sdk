
# Update Agent Variable V1 Request

Request body for updating an agent variable

*This model accepts additional fields of type Any.*

## Structure

`UpdateAgentVariableV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `value` | `Any` | Required | The new value to substitute |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.update_agent_variable_v_1_request import UpdateAgentVariableV1Request

update_agent_variable_v_1_request = UpdateAgentVariableV1Request(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

