
# Get Model V1 Response 1

*This model accepts additional fields of type Any.*

## Structure

`GetModelV1Response1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `canonical_name` | `str` | Optional | - |
| `architecture` | `str` | Optional | - |
| `languages` | `List[str]` | Optional | - |
| `version` | `str` | Optional | - |
| `uuid` | `uuid\|str` | Optional | - |
| `metadata` | [`GetModelV1ResponseOneOf1Metadata`](../../doc/models/get-model-v1-response-one-of-1-metadata.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.get_model_v_1_response_1 import GetModelV1Response1

get_model_v_1_response_1 = GetModelV1Response1(
    name='name4',
    canonical_name='canonical_name0',
    architecture='architecture2',
    languages=[
        'languages1',
        'languages2',
        'languages3'
    ],
    version='version0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

