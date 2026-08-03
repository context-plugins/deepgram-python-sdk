# Voice Agent Configurations

```python
voice_agent_configurations_api = client.voice_agent_configurations
```

## Class Name

`VoiceAgentConfigurationsApi`

## Methods

* [Create](../../doc/controllers/voice-agent-configurations.md#create)
* [List](../../doc/controllers/voice-agent-configurations.md#list)
* [Get](../../doc/controllers/voice-agent-configurations.md#get)
* [Update](../../doc/controllers/voice-agent-configurations.md#update)
* [Delete](../../doc/controllers/voice-agent-configurations.md#delete)


# Create

Creates a new reusable agent configuration. The `config` field must be a valid JSON string representing the `agent` block of a Settings message. The returned `agent_id` can be passed in place of the full `agent` object in future Settings messages.

:information_source: **Note** This endpoint does not require authentication.

```python
def create(self,
          project_id,
          authorization,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`CreateAgentConfigurationV1Request`](../../doc/models/create-agent-configuration-v1-request.md) | Body, Optional | Agent configuration details |

## Response Type

**200**: Agent configuration created successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateAgentConfigurationV1Response`](../../doc/models/create-agent-configuration-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

body = CreateAgentConfigurationV1Request(
    config='config2',
    api_version=1
)

result = voice_agent_configurations_api.create(
    project_id,
    authorization,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# List

Returns all agent configurations for the specified project. Configurations are returned in their uninterpolated form—template variable placeholders appear as-is rather than with their substituted values.

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        project_id,
        authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A list of agent configurations

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListAgentConfigurationsV1Response`](../../doc/models/list-agent-configurations-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = voice_agent_configurations_api.list(
    project_id,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Get

Returns the specified agent configuration in its uninterpolated form

:information_source: **Note** This endpoint does not require authentication.

```python
def get(self,
       project_id,
       agent_id,
       authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `agent_id` | `str` | Template, Required | The unique identifier of the agent configuration |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: An agent configuration

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentConfigurationV1`](../../doc/models/agent-configuration-v1.md).

## Example Usage

```python
project_id = 'project_id6'

agent_id = 'agent_id8'

authorization = 'Authorization8'

result = voice_agent_configurations_api.get(
    project_id,
    agent_id,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Update

Updates the metadata associated with an agent configuration. The config itself is immutable—to change the configuration, delete the existing agent and create a new one.

:information_source: **Note** This endpoint does not require authentication.

```python
def update(self,
          project_id,
          agent_id,
          authorization,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `agent_id` | `str` | Template, Required | The unique identifier of the agent configuration |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`UpdateAgentMetadataV1Request`](../../doc/models/update-agent-metadata-v1-request.md) | Body, Optional | Updated metadata for the agent configuration |

## Response Type

**200**: Agent configuration updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentConfigurationV1`](../../doc/models/agent-configuration-v1.md).

## Example Usage

```python
project_id = 'project_id6'

agent_id = 'agent_id8'

authorization = 'Authorization8'

result = voice_agent_configurations_api.update(
    project_id,
    agent_id,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Delete

Deletes the specified agent configuration. Deleting an agent configuration can cause a production outage if your service references this agent UUID. Migrate all active sessions to a new configuration before deleting.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete(self,
          project_id,
          agent_id,
          authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `agent_id` | `str` | Template, Required | The unique identifier of the agent configuration |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: Agent configuration deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
project_id = 'project_id6'

agent_id = 'agent_id8'

authorization = 'Authorization8'

result = voice_agent_configurations_api.delete(
    project_id,
    agent_id,
    authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

