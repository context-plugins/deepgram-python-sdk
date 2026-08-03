
# Agent Variable V1

A template variable for agent configurations

*This model accepts additional fields of type Any.*

## Structure

`AgentVariableV1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `variable_id` | `str` | Required | The unique identifier of the variable |
| `key` | `str` | Required | The variable name, following the DG_<VARIABLE_NAME> format |
| `value` | `Any` | Required | The value to substitute. Can be any valid JSON type |
| `created_at` | `datetime` | Optional | Timestamp when the variable was created |
| `updated_at` | `datetime` | Optional | Timestamp when the variable was last updated |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.agent_variable_v_1 import AgentVariableV1

agent_variable_v_1 = AgentVariableV1(
    variable_id='variable_id8',
    key='key6',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

