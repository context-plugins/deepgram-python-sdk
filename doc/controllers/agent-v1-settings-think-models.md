# Agent V1 Settings Think Models

```python
agent_v_1_settings_think_models_api = client.agent_v_1_settings_think_models
```

## Class Name

`AgentV1SettingsThinkModelsApi`


# List

Retrieves the available think models that can be used for AI agent processing

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self)
```

## Response Type

**200**: List of available think models

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentThinkModelsV1Response`](../../doc/models/agent-think-models-v1-response.md).

## Example Usage

```python
result = agent_v_1_settings_think_models_api.list()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

