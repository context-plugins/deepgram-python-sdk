# Read V1 Text

```python
read_v_1_text_api = client.read_v_1_text
```

## Class Name

`ReadV1TextApi`


# Analyze

Analyze text content using Deepgrams text analysis API

:information_source: **Note** This endpoint does not require authentication.

```python
def analyze(self,
           authorization,
           callback=None,
           callback_method="POST",
           sentiment=False,
           summarize=None,
           tag=None,
           topics=False,
           custom_topic=None,
           custom_topic_mode="extended",
           intents=False,
           custom_intent=None,
           custom_intent_mode="extended",
           language="en",
           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization` | `str` | Header, Required | Use `Authorization: Token <API_KEY>`<br>Example: `Authorization: Token 12345abcdef` |
| `callback` | `str` | Query, Optional | URL to which we'll make the callback request |
| `callback_method` | [`V1ListenPostParametersCallbackMethod`](../../doc/models/v1-listen-post-parameters-callback-method.md) | Query, Optional | HTTP method by which the callback request will be made<br><br>**Default**: `"POST"` |
| `sentiment` | `bool` | Query, Optional | Recognizes the sentiment throughout a transcript or text<br><br>**Default**: `False` |
| `summarize` | [V1ReadPostParametersSummarize0](../../doc/models/v1-read-post-parameters-summarize-0.md) \| bool \| None | Query, Optional | Summarize content. For Listen API, supports string version option. For Read API, accepts boolean only. |
| `tag` | str \| List[str] \| None | Query, Optional | Label your requests for the purpose of identification during usage reporting |
| `topics` | `bool` | Query, Optional | Detect topics throughout a transcript or text<br><br>**Default**: `False` |
| `custom_topic` | str \| List[str] \| None | Query, Optional | Custom topics you want the model to detect within your input audio or text if present Submit up to `100`. |
| `custom_topic_mode` | [`V1ListenPostParametersCustomTopicMode`](../../doc/models/v1-listen-post-parameters-custom-topic-mode.md) | Query, Optional | Sets how the model will interpret strings submitted to the `custom_topic` param. When `strict`, the model will only return topics submitted using the `custom_topic` param. When `extended`, the model will return its own detected topics in addition to those submitted using the `custom_topic` param<br><br>**Default**: `"extended"` |
| `intents` | `bool` | Query, Optional | Recognizes speaker intent throughout a transcript or text<br><br>**Default**: `False` |
| `custom_intent` | str \| List[str] \| None | Query, Optional | Custom intents you want the model to detect within your input audio if present |
| `custom_intent_mode` | [`V1ListenPostParametersCustomTopicMode`](../../doc/models/v1-listen-post-parameters-custom-topic-mode.md) | Query, Optional | Sets how the model will interpret intents submitted to the `custom_intent` param. When `strict`, the model will only return intents submitted using the `custom_intent` param. When `extended`, the model will return its own detected intents in the `custom_intent` param.<br><br>**Default**: `"extended"` |
| `language` | `str` | Query, Optional | The [BCP-47 language tag](https://tools.ietf.org/html/bcp47) that hints at the primary spoken language. Depending on the Model and API endpoint you choose only certain languages are available<br><br>**Default**: `"en"` |
| `body` | [ReadV1RequestUrl](../../doc/models/read-v1-request-url.md) \| [ReadV1RequestText](../../doc/models/read-v1-request-text.md) \| None | Body, Optional | Analyze a text file |

## Response Type

**200**: Successful text analysis

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReadV1Response`](../../doc/models/read-v1-response.md).

## Example Usage

```python
authorization = 'Authorization8'

callback_method = V1ListenPostParametersCallbackMethod.POST

sentiment = False

summarize = False

topics = False

custom_topic_mode = V1ListenPostParametersCustomTopicMode.EXTENDED

intents = False

custom_intent_mode = V1ListenPostParametersCustomTopicMode.EXTENDED

language = 'en'

result = read_v_1_text_api.analyze(
    authorization,
    callback_method=callback_method,
    sentiment=sentiment,
    summarize=summarize,
    topics=topics,
    custom_topic_mode=custom_topic_mode,
    intents=intents,
    custom_intent_mode=custom_intent_mode,
    language=language
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

