
# Agent Think Models V1 Response Models Items 3

Groq models

*This model accepts additional fields of type Any.*

## Structure

`AgentThinkModelsV1ResponseModelsItems3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | [`AgentThinkModelsV1ResponseModelsItemsOneOf3Id`](../../doc/models/agent-think-models-v1-response-models-items-one-of-3-id.md) | Required | The unique identifier of the Groq model |
| `name` | `str` | Required | The display name of the model |
| `provider` | `Any` | Required | The provider of the model |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.agent_think_models_v_1_response_models_items_3 import AgentThinkModelsV1ResponseModelsItems3
from deepgram.models.agent_think_models_v_1_response_models_items_one_of_3_id import AgentThinkModelsV1ResponseModelsItemsOneOf3Id

agent_think_models_v_1_response_models_items_3 = AgentThinkModelsV1ResponseModelsItems3(
    id=AgentThinkModelsV1ResponseModelsItemsOneOf3Id.ENUM_OPENAIGPTOSS20B,
    name='name2',
    provider=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

