# Manage V1 Projects Billing Fields

```python
manage_v_1_projects_billing_fields_api = client.manage_v_1_projects_billing_fields
```

## Class Name

`ManageV1ProjectsBillingFieldsApi`


# List

Lists the accessors, deployment types, tags, and line items used for billing data in the specified time period. Use this endpoint if you want to filter your results from the Billing Breakdown endpoint and want to know what filters are available.

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

**200**: A list of billing fields for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListBillingFieldsV1Response`](../../doc/models/list-billing-fields-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_billing_fields_api.list(project_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

