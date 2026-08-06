
# List Projects V1 Response Projects Items

*This model accepts additional fields of type Any.*

## Structure

`ListProjectsV1ResponseProjectsItems`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `project_id` | `str` | Optional | The unique identifier of the project |
| `name` | `str` | Optional | The name of the project |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.list_projects_v_1_response_projects_items import ListProjectsV1ResponseProjectsItems

list_projects_v_1_response_projects_items = ListProjectsV1ResponseProjectsItems(
    project_id='project_id0',
    name='name6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

