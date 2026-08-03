
# Listen V1 Response Error Exception

The standard transcription response

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metadata` | [`ListenV1ResponseMetadata`](../../doc/models/listen-v1-response-metadata.md) | Required | - |
| `results` | [`ListenV1ResponseResults`](../../doc/models/listen-v1-response-results.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except ListenV1ResponseErrorException as e:
    print(e)
except ApiException as e:
    print(e)
```

