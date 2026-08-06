
# Speak V1 Request

Request body for text-to-speech conversion

*This model accepts additional fields of type Any.*

## Structure

`SpeakV1Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `text` | `str` | Required | The text content to be converted to speech |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.speak_v_1_request import SpeakV1Request

speak_v_1_request = SpeakV1Request(
    text='text2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

