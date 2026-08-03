
# Listen V1 Media Transcribe Response 200

## Data Type

`ListenV1Response | ListenV1AcceptedResponse`

## Cases

| Type |
|  --- |
| [`ListenV1Response`](../../../doc/models/listen-v1-response.md) |
| [`ListenV1AcceptedResponse`](../../../doc/models/listen-v1-accepted-response.md) |

## ListenV1Response

### Initialization Code

#### Example

```python
value = ListenV1Response(
    metadata=ListenV1ResponseMetadata(
        request_id='000018ae-0000-0000-0000-000000000000',
        sha_256='sha2568',
        created=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        duration=108.02,
        channels=44,
        models=[
            'models2'
        ],
        model_info=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        transaction_key='deprecated'
    ),
    results=ListenV1ResponseResults(
        channels=[
            ListenV1ResponseResultsChannelsItems()
        ]
    )
)
```

## ListenV1AcceptedResponse

### Initialization Code

#### Example

```python
value = ListenV1AcceptedResponse(
    request_id='00000e36-0000-0000-0000-000000000000'
)
```

