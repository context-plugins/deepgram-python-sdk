# Manage V1 Projects Usage Breakdown

```python
manage_v_1_projects_usage_breakdown_api = client.manage_v_1_projects_usage_breakdown
```

## Class Name

`ManageV1ProjectsUsageBreakdownApi`


# Get

Retrieves the usage breakdown for a specific project, with various filter options by API feature or by groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND logic.

```python
def get(self,
       project_id,
       start=None,
       end=None,
       grouping=None,
       accessor=None,
       alternatives=None,
       callback_method=None,
       callback=None,
       channels=None,
       custom_intent_mode=None,
       custom_intent=None,
       custom_topic_mode=None,
       custom_topic=None,
       deployment=None,
       detect_entities=None,
       detect_language=None,
       diarize=None,
       dictation=None,
       encoding=None,
       endpoint=None,
       extra=None,
       filler_words=None,
       intents=None,
       keyterm=None,
       keywords=None,
       language=None,
       measurements=None,
       method=None,
       model=None,
       multichannel=None,
       numerals=None,
       paragraphs=None,
       profanity_filter=None,
       punctuate=None,
       redact=None,
       replace=None,
       sample_rate=None,
       search=None,
       sentiment=None,
       smart_format=None,
       summarize=None,
       tag=None,
       topics=None,
       utt_split=None,
       utterances=None,
       version=None)
```

## Authentication

This endpoint requires [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Template, Required | The unique identifier of the project |
| `start` | `date` | Query, Optional | Start date of the requested date range. Format accepted is YYYY-MM-DD |
| `end` | `date` | Query, Optional | End date of the requested date range. Format accepted is YYYY-MM-DD |
| `grouping` | [`V1ProjectsProjectIdUsageBreakdownGetParametersGrouping`](../../doc/models/v1-projects-project-id-usage-breakdown-get-parameters-grouping.md) | Query, Optional | Common usage grouping parameters |
| `accessor` | `str` | Query, Optional | Filter for requests where a specific accessor was used |
| `alternatives` | `bool` | Query, Optional | Filter for requests where alternatives were used |
| `callback_method` | `bool` | Query, Optional | Filter for requests where callback method was used |
| `callback` | `bool` | Query, Optional | Filter for requests where callback was used |
| `channels` | `bool` | Query, Optional | Filter for requests where channels were used |
| `custom_intent_mode` | `bool` | Query, Optional | Filter for requests where custom intent mode was used |
| `custom_intent` | `bool` | Query, Optional | Filter for requests where custom intent was used |
| `custom_topic_mode` | `bool` | Query, Optional | Filter for requests where custom topic mode was used |
| `custom_topic` | `bool` | Query, Optional | Filter for requests where custom topic was used |
| `deployment` | [`V1ProjectsProjectIdUsageBreakdownGetParametersDeployment`](../../doc/models/v1-projects-project-id-usage-breakdown-get-parameters-deployment.md) | Query, Optional | Filter for requests where a specific deployment was used |
| `detect_entities` | `bool` | Query, Optional | Filter for requests where detect entities was used |
| `detect_language` | `bool` | Query, Optional | Filter for requests where detect language was used |
| `diarize` | `bool` | Query, Optional | Filter for requests where diarize was used |
| `dictation` | `bool` | Query, Optional | Filter for requests where dictation was used |
| `encoding` | `bool` | Query, Optional | Filter for requests where encoding was used |
| `endpoint` | [`V1ProjectsProjectIdUsageBreakdownGetParametersEndpoint`](../../doc/models/v1-projects-project-id-usage-breakdown-get-parameters-endpoint.md) | Query, Optional | Filter for requests where a specific endpoint was used |
| `extra` | `bool` | Query, Optional | Filter for requests where extra was used |
| `filler_words` | `bool` | Query, Optional | Filter for requests where filler words was used |
| `intents` | `bool` | Query, Optional | Filter for requests where intents was used |
| `keyterm` | `bool` | Query, Optional | Filter for requests where keyterm was used |
| `keywords` | `bool` | Query, Optional | Filter for requests where keywords was used |
| `language` | `bool` | Query, Optional | Filter for requests where language was used |
| `measurements` | `bool` | Query, Optional | Filter for requests where measurements were used |
| `method` | [`V1ProjectsProjectIdUsageBreakdownGetParametersMethod`](../../doc/models/v1-projects-project-id-usage-breakdown-get-parameters-method.md) | Query, Optional | Filter for requests where a specific method was used |
| `model` | `str` | Query, Optional | Filter for requests where a specific model uuid was used |
| `multichannel` | `bool` | Query, Optional | Filter for requests where multichannel was used |
| `numerals` | `bool` | Query, Optional | Filter for requests where numerals were used |
| `paragraphs` | `bool` | Query, Optional | Filter for requests where paragraphs were used |
| `profanity_filter` | `bool` | Query, Optional | Filter for requests where profanity filter was used |
| `punctuate` | `bool` | Query, Optional | Filter for requests where punctuate was used |
| `redact` | `bool` | Query, Optional | Filter for requests where redact was used |
| `replace` | `bool` | Query, Optional | Filter for requests where replace was used |
| `sample_rate` | `bool` | Query, Optional | Filter for requests where sample rate was used |
| `search` | `bool` | Query, Optional | Filter for requests where search was used |
| `sentiment` | `bool` | Query, Optional | Filter for requests where sentiment was used |
| `smart_format` | `bool` | Query, Optional | Filter for requests where smart format was used |
| `summarize` | `bool` | Query, Optional | Filter for requests where summarize was used |
| `tag` | `str` | Query, Optional | Filter for requests where a specific tag was used |
| `topics` | `bool` | Query, Optional | Filter for requests where topics was used |
| `utt_split` | `bool` | Query, Optional | Filter for requests where utt split was used |
| `utterances` | `bool` | Query, Optional | Filter for requests where utterances was used |
| `version` | `bool` | Query, Optional | Filter for requests where version was used |

## Response Type

**200**: Usage breakdown response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UsageBreakdownV1Response`](../../doc/models/usage-breakdown-v1-response.md).

## Example Usage

```python
project_id = 'project_id6'

result = manage_v_1_projects_usage_breakdown_api.get(project_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid Request | `ApiException` |

