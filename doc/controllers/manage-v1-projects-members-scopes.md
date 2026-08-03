# Manage V1 Projects Members Scopes

```python
manage_v_1_projects_members_scopes_api = client.manage_v_1_projects_members_scopes
```

## Class Name

`ManageV1ProjectsMembersScopesApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-members-scopes.md#list)
* [Update](../../doc/controllers/manage-v1-projects-members-scopes.md#update)


# List

Retrieves a list of scopes for a specific member

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        project_id,
        member_id,
        authorization)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `member_id` | `str` | Template, Required | The unique identifier of the Member |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |

## Response Type

**200**: A list of scopes for a specific member

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectMemberScopesV1Response`](../../doc/models/list-project-member-scopes-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

member_id = 'member_id0'

authorization = 'Authorization8'

result = manage_v_1_projects_members_scopes_api.list(
    project_id,
    member_id,
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

Updates the scopes for a specific member

:information_source: **Note** This endpoint does not require authentication.

```python
def update(self,
          project_id,
          member_id,
          authorization,
          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `member_id` | `str` | Template, Required | The unique identifier of the Member |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `body` | [`UpdateProjectMemberScopesV1Request`](../../doc/models/update-project-member-scopes-v1-request.md) | Body, Optional | A scope to update |

## Response Type

**200**: Updated the scopes for a specific member

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateProjectMemberScopesV1Response`](../../doc/models/update-project-member-scopes-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

member_id = 'member_id0'

authorization = 'Authorization8'

result = manage_v_1_projects_members_scopes_api.update(
    project_id,
    member_id,
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

