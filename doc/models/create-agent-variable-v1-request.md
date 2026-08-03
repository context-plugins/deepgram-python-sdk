
# Create Agent Variable V1 Request

Request body for creating an agent variable

*This model accepts additional fields of type Any.*

## Structure

`CreateAgentVariableV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Required | The variable name, following the DG_<VARIABLE_NAME> format |
| `value` | `Any` | Required | The value to substitute. Can be any valid JSON type (string, number, boolean, object, or array) |
| `api_version` | `int` | Optional | API version. Defaults to 1<br><br>**Default**: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.create_agent_variable_v_1_request import CreateAgentVariableV1Request

create_agent_variable_v_1_request = CreateAgentVariableV1Request(
    key='key4',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    api_version=1,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

