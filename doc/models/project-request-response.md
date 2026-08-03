
# Project Request Response

A single request

*This model accepts additional fields of type Any.*

## Structure

`ProjectRequestResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | The unique identifier of the request |
| `project_uuid` | `str` | Optional | The unique identifier of the project |
| `created` | `datetime` | Optional | The date and time the request was created |
| `path` | `str` | Optional | The API path of the request |
| `api_key_id` | `str` | Optional | The unique identifier of the API key |
| `response` | `Any` | Optional | The response of the request |
| `code` | `float` | Optional | The response code of the request |
| `deployment` | `str` | Optional | The deployment type |
| `callback` | `str` | Optional | The callback URL for the request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.project_request_response import ProjectRequestResponse

project_request_response = ProjectRequestResponse(
    request_id='request_id6',
    project_uuid='project_uuid4',
    created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    path='path8',
    api_key_id='api_key_id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

