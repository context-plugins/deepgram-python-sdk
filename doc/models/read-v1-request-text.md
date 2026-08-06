
# Read V1 Request Text

*This model accepts additional fields of type Any.*

## Structure

`ReadV1RequestText`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | The plain text to analyze |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.read_v_1_request_text import ReadV1RequestText

read_v_1_request_text = ReadV1RequestText(
    text='text6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

