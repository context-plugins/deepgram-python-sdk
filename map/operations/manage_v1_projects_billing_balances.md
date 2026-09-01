<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsBillingBalances — operations

Accessor: `client.manage_v1_projects_billing_balances` · Source: `deepgram/apis/manage_v1_projects_billing_balances.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_billing_balances.get10

- **Route**: `GET /v1/projects/{project_id}/balances/{balance_id}`
- **Auth**: `api_key_auth`
- **Signature**: `def get10(project_id: str, balance_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `balance_id`
- **Params**: `project_id` — path · `balance_id` — path
- **Returns (parsed)**: `GetProjectBalanceV1Response`
- **Returns (raw)**: `ApiResult[GetProjectBalanceV1Response, Get10ErrorBody]`
- **Error**: `Get10ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetProjectBalanceV1Response` | `deepgram/models/get_project_balance_v1_response.py` |
| `Get10ErrorBody` | `deepgram/errors/get10_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

### client.manage_v1_projects_billing_balances.list13

- **Route**: `GET /v1/projects/{project_id}/balances`
- **Auth**: `api_key_auth`
- **Signature**: `def list13(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path
- **Returns (parsed)**: `ListProjectBalancesV1Response`
- **Returns (raw)**: `ApiResult[ListProjectBalancesV1Response, List13ErrorBody]`
- **Error**: `List13ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListProjectBalancesV1Response` | `deepgram/models/list_project_balances_v1_response.py` |
| `List13ErrorBody` | `deepgram/errors/list13_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

