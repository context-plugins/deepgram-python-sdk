
# Agent Think Models V1 Response

*This model accepts additional fields of type Any.*

## Structure

`AgentThinkModelsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `models` | List[[AgentThinkModelsV1ResponseModelsItems0](../../doc/models/agent-think-models-v1-response-models-items-0.md) \| [AgentThinkModelsV1ResponseModelsItems1](../../doc/models/agent-think-models-v1-response-models-items-1.md) \| [AgentThinkModelsV1ResponseModelsItems2](../../doc/models/agent-think-models-v1-response-models-items-2.md) \| [AgentThinkModelsV1ResponseModelsItems3](../../doc/models/agent-think-models-v1-response-models-items-3.md) \| [AgentThinkModelsV1ResponseModelsItems4](../../doc/models/agent-think-models-v1-response-models-items-4.md)] | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.agent_think_models_v_1_response import AgentThinkModelsV1Response
from deepgram.models.agent_think_models_v_1_response_models_items_0 import AgentThinkModelsV1ResponseModelsItems0
from deepgram.models.agent_think_models_v_1_response_models_items_one_of_0_id import AgentThinkModelsV1ResponseModelsItemsOneOf0Id

agent_think_models_v_1_response = AgentThinkModelsV1Response(
    models=[
        AgentThinkModelsV1ResponseModelsItems0(
            id=AgentThinkModelsV1ResponseModelsItemsOneOf0Id.GPT4O,
            name='name0',
            provider=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
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

