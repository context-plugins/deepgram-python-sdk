
# Get Project Request V1 Response

*This model accepts additional fields of type Any.*

## Structure

`GetProjectRequestV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request` | [`ProjectRequestResponse`](../../doc/models/project-request-response.md) | Optional | A single request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from deepgram.models.get_project_request_v_1_response import GetProjectRequestV1Response
from deepgram.models.project_request_response import ProjectRequestResponse

get_project_request_v_1_response = GetProjectRequestV1Response(
    request=ProjectRequestResponse(
        request_id='request_id2',
        project_uuid='project_uuid6',
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        path='path0',
        api_key_id='api_key_id0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

