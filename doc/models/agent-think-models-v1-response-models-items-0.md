
# Agent Think Models V1 Response Models Items 0

OpenAI models

*This model accepts additional fields of type Any.*

## Structure

`AgentThinkModelsV1ResponseModelsItems0`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | [`AgentThinkModelsV1ResponseModelsItemsOneOf0Id`](../../doc/models/agent-think-models-v1-response-models-items-one-of-0-id.md) | Required | The unique identifier of the OpenAI model |
| `name` | `str` | Required | The display name of the model |
| `provider` | `Any` | Required | The provider of the model |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.agent_think_models_v_1_response_models_items_0 import AgentThinkModelsV1ResponseModelsItems0
from restapi.models.agent_think_models_v_1_response_models_items_one_of_0_id import AgentThinkModelsV1ResponseModelsItemsOneOf0Id

agent_think_models_v_1_response_models_items_0 = AgentThinkModelsV1ResponseModelsItems0(
    id=AgentThinkModelsV1ResponseModelsItemsOneOf0Id.GPT5,
    name='name8',
    provider=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

