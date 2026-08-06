
# Listen V1 Accepted Response

Accepted response for asynchronous transcription requests

*This model accepts additional fields of type Any.*

## Structure

`ListenV1AcceptedResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required | Unique identifier for tracking the asynchronous request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_accepted_response import ListenV1AcceptedResponse

listen_v_1_accepted_response = ListenV1AcceptedResponse(
    request_id='0000054c-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

