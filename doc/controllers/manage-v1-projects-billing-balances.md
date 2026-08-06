# Manage V1 Projects Billing Balances

```python
manage_v_1_projects_billing_balances_api = client.manage_v_1_projects_billing_balances
```

## Class Name

`ManageV1ProjectsBillingBalancesApi`

## Methods

* [List](../../doc/controllers/manage-v1-projects-billing-balances.md#list)
* [Get](../../doc/controllers/manage-v1-projects-billing-balances.md#get)


# List

Generates a list of outstanding balances for the specified project

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

**200**: A list of outstanding balances

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectBalancesV1Response`](../../doc/models/list-project-balances-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_billing_balances_api.list(project_id)

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

Retrieves details about the specified balance

```python
def get(self,
       project_id,
       balance_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `balance_id` | `str` | Template, Required | The unique identifier of the balance |

## Response Type

**200**: A specific balance

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectBalanceV1Response`](../../doc/models/get-project-balance-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

balance_id = 'balance_id2'

result = manage_v_1_projects_billing_balances_api.get(
    project_id,
    balance_id
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

