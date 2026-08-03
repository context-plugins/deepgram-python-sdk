
# Read V1 Response Metadata Metadata Intents Info

*This model accepts additional fields of type Any.*

## Structure

`ReadV1ResponseMetadataMetadataIntentsInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model_uuid` | `uuid\|str` | Optional | - |
| `input_tokens` | `int` | Optional | - |
| `output_tokens` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from restapi.models.read_v_1_response_metadata_metadata_intents_info import ReadV1ResponseMetadataMetadataIntentsInfo

read_v_1_response_metadata_metadata_intents_info = ReadV1ResponseMetadataMetadataIntentsInfo(
    model_uuid='00002036-0000-0000-0000-000000000000',
    input_tokens=212,
    output_tokens=212,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

