# Manage V1 Projects Members Invites

```python
manage_v_1_projects_members_invites_api = client.manage_v_1_projects_members_invites
```

## Class Name

`ManageV1ProjectsMembersInvitesApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-members-invites.md#list)
* [Create](../../doc/controllers/manage-v1-projects-members-invites.md#create)
* [Delete](../../doc/controllers/manage-v1-projects-members-invites.md#delete)


# List

Generates a list of invites for a specific project

```python
def list(self,
        project_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |

## Response Type

**200**: A list of invites for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectInvitesV1Response`](../../doc/models/list-project-invites-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_members_invites_api.list(project_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |


# Create

Generates an invite for a specific project

```python
def create(self,
          project_id,
          body=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `body` | [`CreateProjectInviteV1Request`](../../doc/models/create-project-invite-v1-request.md) | Body, Optional | email to invite to the project |

## Response Type

**200**: The invite was successfully generated

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateProjectInviteV1Response`](../../doc/models/create-project-invite-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_members_invites_api.create(project_id)

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

Deletes an invite for a specific project

```python
def delete(self,
          project_id,
          email)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `email` | `str` | Template, Required | The email address of the member |

## Response Type

**200**: The invite was successfully deleted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeleteProjectInviteV1Response`](../../doc/models/delete-project-invite-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

email = 'email6'

result = manage_v_1_projects_members_invites_api.delete(
    project_id,
    email
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

