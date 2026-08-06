
# Speak V2 Accepted Response

Accepted response returned when a callback URL is supplied; the audio is delivered asynchronously to that URL.

*This model accepts additional fields of type Any.*

## Structure

`SpeakV2AcceptedResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `uuid\|str` | Required | Unique identifier for tracking the asynchronous request |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.speak_v_2_accepted_response import SpeakV2AcceptedResponse

speak_v_2_accepted_response = SpeakV2AcceptedResponse(
    request_id='00000f7c-0000-0000-0000-000000000000',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

