# Manage V1 Projects Billing Purchases

```python
manage_v_1_projects_billing_purchases_api = client.manage_v_1_projects_billing_purchases
```

## Class Name

`ManageV1ProjectsBillingPurchasesApi`


# List

Returns the original purchased amount on an order transaction

:information_source: **Note** This endpoint does not require authentication.

```python
def list(self,
        project_id,
        authorization,
        limit=10)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `limit` | `float` | Query, Optional | Number of results to return per page. Default 10. Range [1,1000]<br><br>**Default**: `10` |

## Response Type

**200**: A list of purchases for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectPurchasesV1Response`](../../doc/models/list-project-purchases-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

authorization = 'Authorization8'

limit = 10

result = manage_v_1_projects_billing_purchases_api.list(
    project_id,
    authorization,
    limit=limit
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

