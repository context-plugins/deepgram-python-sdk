
# List Project Requests V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectRequestsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `float` | Optional | The page number of the paginated response |
| `limit` | `float` | Optional | The number of results per page |
| `requests` | [`List[ProjectRequestResponse]`](../../doc/models/project-request-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from restapi.models.list_project_requests_v_1_response import ListProjectRequestsV1Response
from restapi.models.project_request_response import ProjectRequestResponse

list_project_requests_v_1_response = ListProjectRequestsV1Response(
    page=104.54,
    limit=24.6,
    requests=[
        ProjectRequestResponse(
            request_id='request_id0',
            project_uuid='project_uuid8',
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            path='path2',
            api_key_id='api_key_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ProjectRequestResponse(
            request_id='request_id0',
            project_uuid='project_uuid8',
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            path='path2',
            api_key_id='api_key_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ProjectRequestResponse(
            request_id='request_id0',
            project_uuid='project_uuid8',
            created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            path='path2',
            api_key_id='api_key_id2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

