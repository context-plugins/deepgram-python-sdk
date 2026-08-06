
# Read V1 Request Url

*This model accepts additional fields of type Any.*

## Structure

`ReadV1RequestUrl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | A URL pointing to the text source |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.read_v_1_request_url import ReadV1RequestUrl

read_v_1_request_url = ReadV1RequestUrl(
    url='url4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

