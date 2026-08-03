# Manage V1 Projects Members

```python
manage_v_1_projects_members_api = client.manage_v_1_projects_members
```

## Class Name

`ManageV1ProjectsMembersApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-members.md#list)
* [Delete](../../doc/controllers/manage-v1-projects-members.md#delete)


# List

Retrieves a list of members for a given project

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

**200**: A list of members for a given project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectMembersV1Response`](../../doc/models/list-project-members-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = manage_v_1_projects_members_api.list(
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


# Delete

Removes a member from the project using their unique member ID

:information_source: **Note** This endpoint does not require authentication.

```python
def delete(self,
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

**200**: Delete the specific member from the project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeleteProjectMemberV1Response`](../../doc/models/delete-project-member-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

member_id = 'member_id0'

authorization = 'Authorization8'

result = manage_v_1_projects_members_api.delete(
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

