# Manage V1 Projects Usage Fields

```python
manage_v_1_projects_usage_fields_api = client.manage_v_1_projects_usage_fields
```

## Class Name

`ManageV1ProjectsUsageFieldsApi`


# List

Lists the features, models, tags, languages, and processing method used for requests in the specified project

```python
def list(self,
        project_id,
        start=None,
        end=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `start` | `date` | Query, Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| `end` | `date` | Query, Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |

## Response Type

**200**: A list of fields for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UsageFieldsV1Response`](../../doc/models/usage-fields-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_usage_fields_api.list(project_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

