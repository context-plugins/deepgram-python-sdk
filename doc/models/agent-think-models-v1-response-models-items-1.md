
# Agent Think Models V1 Response Models Items 1

Anthropic models

*This model accepts additional fields of type Any.*

## Structure

`AgentThinkModelsV1ResponseModelsItems1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | [`AgentThinkModelsV1ResponseModelsItemsOneOf1Id`](../../doc/models/agent-think-models-v1-response-models-items-one-of-1-id.md) | Required | The unique identifier of the Anthropic model |
| `name` | `str` | Required | The display name of the model |
| `provider` | `Any` | Required | The provider of the model |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.agent_think_models_v_1_response_models_items_1 import AgentThinkModelsV1ResponseModelsItems1
from deepgram.models.agent_think_models_v_1_response_models_items_one_of_1_id import AgentThinkModelsV1ResponseModelsItemsOneOf1Id

agent_think_models_v_1_response_models_items_1 = AgentThinkModelsV1ResponseModelsItems1(
    id=AgentThinkModelsV1ResponseModelsItemsOneOf1Id.CLAUDE35HAIKULATEST,
    name='name2',
    provider=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

