# Manage V1 Projects Billing Breakdown

```python
manage_v_1_projects_billing_breakdown_api = client.manage_v_1_projects_billing_breakdown
```

## Class Name

`ManageV1ProjectsBillingBreakdownApi`


# List

Retrieves the billing summary for a specific project, with various filter options or by grouping options.

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        project_id,
        authorization,
        start=None,
        end=None,
        accessor=None,
        deployment=None,
        tag=None,
        line_item=None,
        grouping=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `start` | `date` | Query, Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| `end` | `date` | Query, Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |
| `accessor` | `str` | Query, Optional | Filter for requests where a specific accessor was used |
| `deployment` | [`V1ProjectsProjectIdBillingBreakdownGetParametersDeployment`](../../doc/models/v1-projects-project-id-billing-breakdown-get-parameters-deployment.md) | Query, Optional | Filter for requests where a specific deployment was used |
| `tag` | `str` | Query, Optional | Filter for requests where a specific tag was used |
| `line_item` | `str` | Query, Optional | Filter requests by line item (e.g. streaming::nova-3) |
| `grouping` | [`List[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItems]`](../../doc/models/v1-projects-project-id-billing-breakdown-get-parameters-grouping-schema-items.md) | Query, Optional | Group billing breakdown by one or more dimensions (accessor, deployment, line_item, tags) |

## Response Type

**200**: Billing breakdown response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingBreakdownV1Response`](../../doc/models/billing-breakdown-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

result = manage_v_1_projects_billing_breakdown_api.list(
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

