
# List Projects V1 Response

*This model accepts additional fields of type Any.*

## Structure

`ListProjectsV1Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `projects` | [`List[ListProjectsV1ResponseProjectsItems]`](../../doc/models/list-projects-v1-response-projects-items.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_projects_v_1_response import ListProjectsV1Response
from deepgram.models.list_projects_v_1_response_projects_items import ListProjectsV1ResponseProjectsItems

list_projects_v_1_response = ListProjectsV1Response(
    projects=[
        ListProjectsV1ResponseProjectsItems(
            project_id='project_id4',
            name='name2',
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

