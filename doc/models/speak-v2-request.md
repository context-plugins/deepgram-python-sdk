
# Speak V2 Request

Request body for Flux TTS batch (REST) text-to-speech conversion. The full block of text is synthesized in a single request and returned as one audio response.

*This model accepts additional fields of type Any.*

## Structure

`SpeakV2Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | The text content to be converted to speech. The server normalizes and preprocesses the text (e.g. stripping inline controls) before synthesis. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.speak_v_2_request import SpeakV2Request

speak_v_2_request = SpeakV2Request(
    text='text2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

