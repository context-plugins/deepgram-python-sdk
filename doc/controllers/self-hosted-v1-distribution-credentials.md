# Self Hosted V1 Distribution Credentials

```python
self_hosted_v_1_distribution_credentials_api = client.self_hosted_v_1_distribution_credentials
```

## Class Name

`SelfHostedV1DistributionCredentialsApi`

## Methods

* [List](../../doc/controllers/self-hosted-v1-distribution-credentials.md#list)
* [Create](../../doc/controllers/self-hosted-v1-distribution-credentials.md#create)
* [Get](../../doc/controllers/self-hosted-v1-distribution-credentials.md#get)
* [Delete](../../doc/controllers/self-hosted-v1-distribution-credentials.md#delete)


# List

Lists sets of distribution credentials for the specified project

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

**200**: A list of distribution credentials for a specific project

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListProjectDistributionCredentialsV1Response`](../../doc/models/list-project-distribution-credentials-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = self_hosted_v_1_distribution_credentials_api.list(project_id)

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

Creates a set of distribution credentials for the specified project

```python
def create(self,
          project_id,
          scopes=None,
          provider="quay",
          body=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `scopes` | [`List[V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersScopesSchemaItems]`](../../doc/models/v1-projects-project-id-self-hosted-distribution-credentials-post-parameters-scopes-schema-items.md) | Query, Optional | List of permission scopes for the credentials |
| `provider` | [`V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProvider`](../../doc/models/v1-projects-project-id-self-hosted-distribution-credentials-post-parameters-provider.md) | Query, Optional | The provider of the distribution service<br><br>**Default**: `"quay"` |
| `body` | [`CreateProjectDistributionCredentialsV1Request`](../../doc/models/create-project-distribution-credentials-v1-request.md) | Body, Optional | The set of distribution credentials to create |

## Response Type

**200**: Single distribution credential

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CreateProjectDistributionCredentialsV1Response`](../../doc/models/create-project-distribution-credentials-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

provider = V1ProjectsProjectIdSelfHostedDistributionCredentialsPostParametersProvider.QUAY

result = self_hosted_v_1_distribution_credentials_api.create(
    project_id,
    provider=provider
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

Returns a set of distribution credentials for the specified project

```python
def get(self,
       project_id,
       distribution_credentials_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `distribution_credentials_id` | `str` | Template, Required | The UUID of the distribution credentials |

## Response Type

**200**: Single distribution credential

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectDistributionCredentialsV1Response`](../../doc/models/get-project-distribution-credentials-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

distribution_credentials_id = 'distribution_credentials_id0'

result = self_hosted_v_1_distribution_credentials_api.get(
    project_id,
    distribution_credentials_id
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

Deletes a set of distribution credentials for the specified project

```python
def delete(self,
          project_id,
          distribution_credentials_id)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `distribution_credentials_id` | `str` | Template, Required | The UUID of the distribution credentials |

## Response Type

**200**: Single distribution credential

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProjectDistributionCredentialsV1Response`](../../doc/models/get-project-distribution-credentials-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

distribution_credentials_id = 'distribution_credentials_id0'

result = self_hosted_v_1_distribution_credentials_api.delete(
    project_id,
    distribution_credentials_id
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

