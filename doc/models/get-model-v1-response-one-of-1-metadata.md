
# Get Model V1 Response One of 1 Metadata

*This model accepts additional fields of type Any.*

## Structure

`GetModelV1ResponseOneOf1Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accent` | `str` | Optional | - |
| `age` | `str` | Optional | - |
| `color` | `str` | Optional | - |
| `image` | `str` | Optional | - |
| `sample` | `str` | Optional | - |
| `tags` | `List[str]` | Optional | - |
| `use_cases` | `List[str]` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.get_model_v_1_response_one_of_1_metadata import GetModelV1ResponseOneOf1Metadata

get_model_v_1_response_one_of_1_metadata = GetModelV1ResponseOneOf1Metadata(
    accent='accent2',
    age='age6',
    color='color8',
    image='image8',
    sample='sample0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

