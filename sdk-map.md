<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Deepgram (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Deepgram |
| Root package | `deepgram` |
| Distribution name | `deepgram` |
| Requires | Python 3.10 or later |
| API spec version | `1.0.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from deepgram import DeepgramClient

client = DeepgramClient(api_key_auth="YOUR_API_KEY", jwt_auth="YOUR_BEARER_TOKEN", environment="production")

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with DeepgramClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from deepgram import AsyncDeepgramClient


async def main() -> None:
    client = AsyncDeepgramClient(api_key_auth="YOUR_API_KEY", jwt_auth="YOUR_BEARER_TOKEN", environment="production")
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncDeepgramClient(...) as client:` closes the pool on exit.

`AsyncClient` (`deepgram/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `DeepgramClient` and `AsyncDeepgramClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.agent_v1_settings_think_models`). Every constructor argument is optional and keyword-only. Sources: `deepgram/client.py`, `deepgram/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `base_url` | `str \| None` | `str \| None` | `None` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `api_key_auth` | `str \| None` | `str \| None` | `None` |
| `jwt_auth` | `str \| None` | `str \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `deepgram.server` | `Literal` of the Environments table's names |
| `RetryOptionsOrDict` | `deepgram.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `HttpClient` | `deepgram.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `AsyncHttpClient` | `deepgram.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `deepgram/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`deepgram/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `deepgram/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`deepgram/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`deepgram/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `deepgram/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `deepgram/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `deepgram/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `deepgram/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.agent_v1_settings_think_models.list_()
except ApiError as e:
    # Case A — typed error: e.error is ListErrorBody
    if isinstance(e.error, ErrorResponse):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **50 operations**, **50 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (24 pages, 50 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries` or `status_codes_to_retry`; every signature ends with it | here (`deepgram/core/request_options.py`), Retries |
| **Base URL is the selected environment's** — this SDK's only server, one URL per `environment=`; override it with `base_url="https://…"` | Servers & auth |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.agent_v1_settings_think_models` | 1 | [map/operations/agent_v1_settings_think_models.md](map/operations/agent_v1_settings_think_models.md) |
| `client.auth_v1_tokens` | 1 | [map/operations/auth_v1_tokens.md](map/operations/auth_v1_tokens.md) |
| `client.listen_v1_media` | 1 | [map/operations/listen_v1_media.md](map/operations/listen_v1_media.md) |
| `client.manage_v1_models` | 2 | [map/operations/manage_v1_models.md](map/operations/manage_v1_models.md) |
| `client.manage_v1_projects` | 5 | [map/operations/manage_v1_projects.md](map/operations/manage_v1_projects.md) |
| `client.manage_v1_projects_billing_balances` | 2 | [map/operations/manage_v1_projects_billing_balances.md](map/operations/manage_v1_projects_billing_balances.md) |
| `client.manage_v1_projects_billing_breakdown` | 1 | [map/operations/manage_v1_projects_billing_breakdown.md](map/operations/manage_v1_projects_billing_breakdown.md) |
| `client.manage_v1_projects_billing_fields` | 1 | [map/operations/manage_v1_projects_billing_fields.md](map/operations/manage_v1_projects_billing_fields.md) |
| `client.manage_v1_projects_billing_purchases` | 1 | [map/operations/manage_v1_projects_billing_purchases.md](map/operations/manage_v1_projects_billing_purchases.md) |
| `client.manage_v1_projects_keys` | 4 | [map/operations/manage_v1_projects_keys.md](map/operations/manage_v1_projects_keys.md) |
| `client.manage_v1_projects_members` | 2 | [map/operations/manage_v1_projects_members.md](map/operations/manage_v1_projects_members.md) |
| `client.manage_v1_projects_members_invites` | 3 | [map/operations/manage_v1_projects_members_invites.md](map/operations/manage_v1_projects_members_invites.md) |
| `client.manage_v1_projects_members_scopes` | 2 | [map/operations/manage_v1_projects_members_scopes.md](map/operations/manage_v1_projects_members_scopes.md) |
| `client.manage_v1_projects_models` | 2 | [map/operations/manage_v1_projects_models.md](map/operations/manage_v1_projects_models.md) |
| `client.manage_v1_projects_requests` | 2 | [map/operations/manage_v1_projects_requests.md](map/operations/manage_v1_projects_requests.md) |
| `client.manage_v1_projects_usage` | 1 | [map/operations/manage_v1_projects_usage.md](map/operations/manage_v1_projects_usage.md) |
| `client.manage_v1_projects_usage_breakdown` | 1 | [map/operations/manage_v1_projects_usage_breakdown.md](map/operations/manage_v1_projects_usage_breakdown.md) |
| `client.manage_v1_projects_usage_fields` | 1 | [map/operations/manage_v1_projects_usage_fields.md](map/operations/manage_v1_projects_usage_fields.md) |
| `client.read_v1_text` | 1 | [map/operations/read_v1_text.md](map/operations/read_v1_text.md) |
| `client.self_hosted_v1_distribution_credentials` | 4 | [map/operations/self_hosted_v1_distribution_credentials.md](map/operations/self_hosted_v1_distribution_credentials.md) |
| `client.speak_v1_audio` | 1 | [map/operations/speak_v1_audio.md](map/operations/speak_v1_audio.md) |
| `client.speak_v2_audio` | 1 | [map/operations/speak_v2_audio.md](map/operations/speak_v2_audio.md) |
| `client.voice_agent_configurations` | 5 | [map/operations/voice_agent_configurations.md](map/operations/voice_agent_configurations.md) |
| `client.voice_agent_variables` | 5 | [map/operations/voice_agent_variables.md](map/operations/voice_agent_variables.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `deepgram/models/` declares one type plus its input companion, and every module under `deepgram/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AgentConfigurationV1` ↔ `agent_configuration_v1.py`; an error alias drops its `Body` suffix: `AnalyzeErrorBody` ↔ `analyze_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 139 | `deepgram/models/` |
| Enums (`Enum` over `str`) — Python member names + wire values | 73 | `deepgram/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 31 | `deepgram/models/unions/` |
| Error aliases (one per Case A operation) | 50 | `deepgram/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; in this SDK every field's wire name is its Python name — no field carries a `Field(alias=…)`. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`AgentConfigurationV1` ↔ `AgentConfigurationV1Dict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AgentThinkModelsV1ResponseModelsItemsOneOf0Id` ↔ `AgentThinkModelsV1ResponseModelsItemsOneOf0IdOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `deepgram` |
| Operation controllers | `deepgram.apis` |
| Models | `deepgram.models` |
| Enums | `deepgram.models.enums` |
| Unions | `deepgram.models.unions`, `deepgram.models` |
| Error aliases | `deepgram.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `deepgram.core` |

---

## Servers & auth

**API key (header `Authorization`).** Pass `api_key_auth="<api_key>"`; sent as the `Authorization` request header.

**Bearer token.** Pass `jwt_auth="<token>"`.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`deepgram/server/environment.py`); this SDK's one server (`deepgram/server/server_config.py`) has a base URL per environment:

| Environment | Base URL | Hosting | Override point |
| --- | --- | --- | --- |
| `"production"` *(default)* | `https://agent.deepgram.com` | Production | `base_url="https://…"` |
| `"environment2"` | `https://api.deepgram.com` | Base | `base_url="https://…"` |

Pick a row with `environment=`.

