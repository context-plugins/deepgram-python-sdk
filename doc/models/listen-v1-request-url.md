
# Listen V1 Request Url

Audio file URL to transcribe

*This model accepts additional fields of type Any.*

## Structure

`ListenV1RequestUrl`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_request_url import ListenV1RequestUrl

listen_v_1_request_url = ListenV1RequestUrl(
    url='url2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

