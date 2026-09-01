<!-- Generated file — do not edit; regenerated with the SDK. -->

# ManageV1ProjectsBillingBreakdown — operations

Accessor: `client.manage_v1_projects_billing_breakdown` · Source: `deepgram/apis/manage_v1_projects_billing_breakdown.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.manage_v1_projects_billing_breakdown.list14

- **Route**: `GET /v1/projects/{project_id}/billing/breakdown`
- **Auth**: `api_key_auth`
- **Signature**: `def list14(project_id: str, *, start: Date | None = None, end: Date | None = None, accessor: str | None = None, deployment: V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr | None = None, tag: str | None = None, line_item: str | None = None, grouping: list[V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path · `start` — query · `end` — query · `accessor` — query · `deployment` — query · `tag` — query · `line_item` — query · `grouping` — query
- **Returns (parsed)**: `BillingBreakdownV1Response`
- **Returns (raw)**: `ApiResult[BillingBreakdownV1Response, List14ErrorBody]`
- **Error**: `List14ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `V1ProjectsProjectIdBillingBreakdownGetParametersDeploymentOrStr` | `deepgram/models/enums/v1_projects_project_id_billing_breakdown_get_parameters_deployment.py` |
| `V1ProjectsProjectIdBillingBreakdownGetParametersGroupingSchemaItemsOrStr` | `deepgram/models/enums/v1_projects_project_id_billing_breakdown_get_parameters_grouping_schema_items.py` |
| `BillingBreakdownV1Response` | `deepgram/models/billing_breakdown_v1_response.py` |
| `List14ErrorBody` | `deepgram/errors/list14_error.py` |
| `ErrorResponse` | `deepgram/models/unions/error_response.py` |

