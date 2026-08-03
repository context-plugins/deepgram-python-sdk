# Voice Agent Variables

```python
voice_agent_variables_api = client.voice_agent_variables
```

## Class Name

`VoiceAgentVariablesApi`

## Methods

* [Create](../../doc/controllers/voice-agent-variables.md#create)
* [List](../../doc/controllers/voice-agent-variables.md#list)
* [Get](../../doc/controllers/voice-agent-variables.md#get)
* [Update](../../doc/controllers/voice-agent-variables.md#update)
* [Delete](../../doc/controllers/voice-agent-variables.md#delete)


# Create

Creates a new template variable. Variables follow the `DG_<VARIABLE_NAME>` naming format and can substitute any JSON value in an agent configuration.

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
| `body` | [`CreateAgentVariableV1Request`](../../doc/models/create-agent-variable-v1-request.md) | Body, Optional | Agent variable details |

## Response Type

**200**: Agent variable created successfully

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentVariableV1`](../../doc/models/agent-variable-v1.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

body = CreateAgentVariableV1Request(
    key='key6',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    api_version=1
)

result = voice_agent_variables_api.create(
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

Returns all template variables for the specified project

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

**200**: A list of agent variables

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListAgentVariablesV1Response`](../../doc/models/list-agent-variables-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = voice_agent_variables_api.list(
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

Returns the specified template variable

:information_source: **Note** This endpoint does not require authentication.

```python
def get(self,
       project_id,
       variable_id,
       authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `variable_id` | `str` | Template, Required | The unique identifier of the agent variable |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: An agent variable

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentVariableV1`](../../doc/models/agent-variable-v1.md).

## Example Usage

```python
project_id = 'project_id6'

variable_id = 'variable_id8'

authorization = 'Authorization8'

result = voice_agent_variables_api.get(
    project_id,
    variable_id,
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

Updates the value of an existing template variable

:information_source: **Note** This endpoint does not require authentication.

```python
def update(self,
          project_id,
          variable_id,
          authorization,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `variable_id` | `str` | Template, Required | The unique identifier of the agent variable |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`UpdateAgentVariableV1Request`](../../doc/models/update-agent-variable-v1-request.md) | Body, Optional | Updated value for the agent variable |

## Response Type

**200**: Agent variable updated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AgentVariableV1`](../../doc/models/agent-variable-v1.md).

## Example Usage

```python
project_id = 'project_id6'

variable_id = 'variable_id8'

authorization = 'Authorization8'

result = voice_agent_variables_api.update(
    project_id,
    variable_id,
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

Deletes the specified template variable

:information_source: **Note** This endpoint does not require authentication.

```python
def delete(self,
          project_id,
          variable_id,
          authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `variable_id` | `str` | Template, Required | The unique identifier of the agent variable |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: Agent variable deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
project_id = 'project_id6'

variable_id = 'variable_id8'

authorization = 'Authorization8'

result = voice_agent_variables_api.delete(
    project_id,
    variable_id,
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

