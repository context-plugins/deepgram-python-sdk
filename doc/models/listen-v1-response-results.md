
# Listen V1 Response Results

*This model accepts additional fields of type Any.*

## Structure

`ListenV1ResponseResults`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channels` | [`List[ListenV1ResponseResultsChannelsItems]`](../../doc/models/listen-v1-response-results-channels-items.md) | Required | - |
| `utterances` | [`List[ListenV1ResponseResultsUtterancesItems]`](../../doc/models/listen-v1-response-results-utterances-items.md) | Optional | - |
| `summary` | [`ListenV1ResponseResultsSummary`](../../doc/models/listen-v1-response-results-summary.md) | Optional | - |
| `topics` | [`SharedTopics`](../../doc/models/shared-topics.md) | Optional | Output whenever `topics=true` is used |
| `intents` | [`SharedIntents`](../../doc/models/shared-intents.md) | Optional | Output whenever `intents=true` is used |
| `sentiments` | [`SharedSentiments`](../../doc/models/shared-sentiments.md) | Optional | Output whenever `sentiment=true` is used |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from deepgram.models.listen_v_1_response_results import ListenV1ResponseResults
from deepgram.models.listen_v_1_response_results_channels_items import ListenV1ResponseResultsChannelsItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items import ListenV1ResponseResultsChannelsItemsAlternativesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_entities_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_paragraphs_paragraphs_items_sentences_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems
from deepgram.models.listen_v_1_response_results_channels_items_alternatives_items_words_items import ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems
from deepgram.models.listen_v_1_response_results_channels_items_search_items import ListenV1ResponseResultsChannelsItemsSearchItems
from deepgram.models.listen_v_1_response_results_channels_items_search_items_hits_items import ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems
from deepgram.models.listen_v_1_response_results_summary import ListenV1ResponseResultsSummary
from deepgram.models.listen_v_1_response_results_utterances_items import ListenV1ResponseResultsUtterancesItems
from deepgram.models.shared_intents import SharedIntents
from deepgram.models.shared_intents_results import SharedIntentsResults
from deepgram.models.shared_intents_results_intents import SharedIntentsResultsIntents
from deepgram.models.shared_intents_results_intents_segments_items import SharedIntentsResultsIntentsSegmentsItems
from deepgram.models.shared_intents_results_intents_segments_items_intents_items import SharedIntentsResultsIntentsSegmentsItemsIntentsItems
from deepgram.models.shared_sentiments import SharedSentiments
from deepgram.models.shared_sentiments_average import SharedSentimentsAverage
from deepgram.models.shared_sentiments_segments_items import SharedSentimentsSegmentsItems
from deepgram.models.shared_topics import SharedTopics
from deepgram.models.shared_topics_results import SharedTopicsResults
from deepgram.models.shared_topics_results_topics import SharedTopicsResultsTopics
from deepgram.models.shared_topics_results_topics_segments_items import SharedTopicsResultsTopicsSegmentsItems
from deepgram.models.shared_topics_results_topics_segments_items_topics_items import SharedTopicsResultsTopicsSegmentsItemsTopicsItems

listen_v_1_response_results = ListenV1ResponseResults(
    channels=[
        ListenV1ResponseResultsChannelsItems(
            search=[
                ListenV1ResponseResultsChannelsItemsSearchItems(
                    query='query2',
                    hits=[
                        ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(
                            confidence=144.74,
                            start=146.64,
                            end=190.58,
                            snippet='snippet0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ListenV1ResponseResultsChannelsItemsSearchItems(
                    query='query2',
                    hits=[
                        ListenV1ResponseResultsChannelsItemsSearchItemsHitsItems(
                            confidence=144.74,
                            start=146.64,
                            end=190.58,
                            snippet='snippet0',
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            alternatives=[
                ListenV1ResponseResultsChannelsItemsAlternativesItems(
                    transcript='transcript6',
                    confidence=34.78,
                    words=[
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
                            word='word0',
                            start=58.62,
                            end=102.56,
                            confidence=56.72,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
                            word='word0',
                            start=58.62,
                            end=102.56,
                            confidence=56.72,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    paragraphs=ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs(
                        transcript='transcript2',
                        paragraphs=[
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        ],
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    entities=[
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                ListenV1ResponseResultsChannelsItemsAlternativesItems(
                    transcript='transcript6',
                    confidence=34.78,
                    words=[
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
                            word='word0',
                            start=58.62,
                            end=102.56,
                            confidence=56.72,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsWordsItems(
                            word='word0',
                            start=58.62,
                            end=102.56,
                            confidence=56.72,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    paragraphs=ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphs(
                        transcript='transcript2',
                        paragraphs=[
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItems(
                                sentences=[
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    ),
                                    ListenV1ResponseResultsChannelsItemsAlternativesItemsParagraphsParagraphsItemsSentencesItems(
                                        text='text2',
                                        start=16.92,
                                        end=60.86,
                                        additional_properties={
                                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                        }
                                    )
                                ],
                                speaker=128,
                                num_words=60,
                                start=34.44,
                                end=78.38,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        ],
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    ),
                    entities=[
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        ),
                        ListenV1ResponseResultsChannelsItemsAlternativesItemsEntitiesItems(
                            label='label0',
                            value='value2',
                            raw_value='raw_value6',
                            confidence=136.04,
                            start_word=101.8,
                            additional_properties={
                                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                            }
                        )
                    ],
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            detected_language='detected_language0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    utterances=[
        ListenV1ResponseResultsUtterancesItems(
            start=249.82,
            end=37.76,
            confidence=247.92,
            channel=182,
            transcript='transcript0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    summary=ListenV1ResponseResultsSummary(
        result='result4',
        short='short8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    topics=SharedTopics(
        results=SharedTopicsResults(
            topics=SharedTopicsResultsTopics(
                segments=[
                    SharedTopicsResultsTopicsSegmentsItems(
                        text='text6',
                        start_word=4.96,
                        end_word=219.1,
                        topics=[
                            SharedTopicsResultsTopicsSegmentsItemsTopicsItems(
                                topic='topic2',
                                confidence_score=42.46,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            ),
                            SharedTopicsResultsTopicsSegmentsItemsTopicsItems(
                                topic='topic2',
                                confidence_score=42.46,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        ],
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    intents=SharedIntents(
        results=SharedIntentsResults(
            intents=SharedIntentsResultsIntents(
                segments=[
                    SharedIntentsResultsIntentsSegmentsItems(
                        text='text6',
                        start_word=4.96,
                        end_word=219.1,
                        intents=[
                            SharedIntentsResultsIntentsSegmentsItemsIntentsItems(
                                intent='intent4',
                                confidence_score=193.42,
                                additional_properties={
                                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                                }
                            )
                        ],
                        additional_properties={
                            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                        }
                    )
                ],
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sentiments=SharedSentiments(
        segments=[
            SharedSentimentsSegmentsItems(
                text='text6',
                start_word=4.96,
                end_word=219.1,
                sentiment='sentiment6',
                sentiment_score=76.78,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        average=SharedSentimentsAverage(
            sentiment='sentiment8',
            sentiment_score=2.7,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

