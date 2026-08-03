
# Agent Think Models V1 Response Models Items 4

AWS Bedrock models (custom models accepted)

*This model accepts additional fields of type Any.*

## Structure

`AgentThinkModelsV1ResponseModelsItems4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the AWS Bedrock model (any model string accepted for BYO LLMs) |
| `name` | `str` | Required | The display name of the model |
| `provider` | `Any` | Required | The provider of the model |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.agent_think_models_v_1_response_models_items_4 import AgentThinkModelsV1ResponseModelsItems4

agent_think_models_v_1_response_models_items_4 = AgentThinkModelsV1ResponseModelsItems4(
    id='id0',
    name='name0',
    provider=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

