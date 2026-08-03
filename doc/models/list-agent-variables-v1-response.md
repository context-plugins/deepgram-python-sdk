
# List Agent Variables V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListAgentVariablesV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `variables` | [`List[AgentVariableV1]`](../../doc/models/agent-variable-v1.md) | Optional | A list of agent variables for the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.agent_variable_v_1 import AgentVariableV1
from restapi.models.list_agent_variables_v_1_response import ListAgentVariablesV1Response

list_agent_variables_v_1_response = ListAgentVariablesV1Response(
    variables=[
        AgentVariableV1(
            variable_id='variable_id6',
            key='key2',
            value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AgentVariableV1(
            variable_id='variable_id6',
            key='key2',
            value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        AgentVariableV1(
            variable_id='variable_id6',
            key='key2',
            value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
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

