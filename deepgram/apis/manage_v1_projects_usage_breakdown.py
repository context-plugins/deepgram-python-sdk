from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    Date,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
)
from ..errors.get9_error import Get9ErrorBody, get9_error_mapper
from ..models.enums.v1_projects_project_id_usage_breakdown_get_parameters_deployment import (
    V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr,
)
from ..models.enums.v1_projects_project_id_usage_breakdown_get_parameters_endpoint import (
    V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr,
)
from ..models.enums.v1_projects_project_id_usage_breakdown_get_parameters_grouping import (
    V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr,
)
from ..models.enums.v1_projects_project_id_usage_breakdown_get_parameters_method import (
    V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr,
)
from ..models.usage_breakdown_v1_response import UsageBreakdownV1Response
from ..server.server import Server


class ManageV1ProjectsUsageBreakdown:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageV1ProjectsUsageBreakdownWithRawResponse(client, server, auth)

    def get9(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        grouping: V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None = None,
        accessor: str | None = None,
        alternatives: bool | None = None,
        callback_method: bool | None = None,
        callback: bool | None = None,
        channels: bool | None = None,
        custom_intent_mode: bool | None = None,
        custom_intent: bool | None = None,
        custom_topic_mode: bool | None = None,
        custom_topic: bool | None = None,
        deployment: V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None = None,
        detect_entities: bool | None = None,
        detect_language: bool | None = None,
        diarize: bool | None = None,
        dictation: bool | None = None,
        encoding: bool | None = None,
        endpoint: V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None = None,
        extra: bool | None = None,
        filler_words: bool | None = None,
        intents: bool | None = None,
        keyterm: bool | None = None,
        keywords: bool | None = None,
        language: bool | None = None,
        measurements: bool | None = None,
        method: V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None = None,
        model: str | None = None,
        multichannel: bool | None = None,
        numerals: bool | None = None,
        paragraphs: bool | None = None,
        profanity_filter: bool | None = None,
        punctuate: bool | None = None,
        redact: bool | None = None,
        replace: bool | None = None,
        sample_rate: bool | None = None,
        search: bool | None = None,
        sentiment: bool | None = None,
        smart_format: bool | None = None,
        summarize: bool | None = None,
        tag: str | None = None,
        topics: bool | None = None,
        utt_split: bool | None = None,
        utterances: bool | None = None,
        version: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageBreakdownV1Response:
        """Retrieves the usage breakdown for a specific project, with various filter options by API feature or by
        groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false
        excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND
        logic.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            grouping: Common usage grouping parameters
            accessor: Filter for requests where a specific accessor was used
            alternatives: Filter for requests where alternatives were used
            callback_method: Filter for requests where callback method was used
            callback: Filter for requests where callback was used
            channels: Filter for requests where channels were used
            custom_intent_mode: Filter for requests where custom intent mode was used
            custom_intent: Filter for requests where custom intent was used
            custom_topic_mode: Filter for requests where custom topic mode was used
            custom_topic: Filter for requests where custom topic was used
            deployment: Filter for requests where a specific deployment was used
            detect_entities: Filter for requests where detect entities was used
            detect_language: Filter for requests where detect language was used
            diarize: Filter for requests where diarize was used
            dictation: Filter for requests where dictation was used
            encoding: Filter for requests where encoding was used
            endpoint: Filter for requests where a specific endpoint was used
            extra: Filter for requests where extra was used
            filler_words: Filter for requests where filler words was used
            intents: Filter for requests where intents was used
            keyterm: Filter for requests where keyterm was used
            keywords: Filter for requests where keywords was used
            language: Filter for requests where language was used
            measurements: Filter for requests where measurements were used
            method: Filter for requests where a specific method was used
            model: Filter for requests where a specific model uuid was used
            multichannel: Filter for requests where multichannel was used
            numerals: Filter for requests where numerals were used
            paragraphs: Filter for requests where paragraphs were used
            profanity_filter: Filter for requests where profanity filter was used
            punctuate: Filter for requests where punctuate was used
            redact: Filter for requests where redact was used
            replace: Filter for requests where replace was used
            sample_rate: Filter for requests where sample rate was used
            search: Filter for requests where search was used
            sentiment: Filter for requests where sentiment was used
            smart_format: Filter for requests where smart format was used
            summarize: Filter for requests where summarize was used
            tag: Filter for requests where a specific tag was used
            topics: Filter for requests where topics was used
            utt_split: Filter for requests where utt split was used
            utterances: Filter for requests where utterances was used
            version: Filter for requests where version was used
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Usage breakdown response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return self._with_raw_response.get9(
            project_id,
            start=start,
            end=end,
            grouping=grouping,
            accessor=accessor,
            alternatives=alternatives,
            callback_method=callback_method,
            callback=callback,
            channels=channels,
            custom_intent_mode=custom_intent_mode,
            custom_intent=custom_intent,
            custom_topic_mode=custom_topic_mode,
            custom_topic=custom_topic,
            deployment=deployment,
            detect_entities=detect_entities,
            detect_language=detect_language,
            diarize=diarize,
            dictation=dictation,
            encoding=encoding,
            endpoint=endpoint,
            extra=extra,
            filler_words=filler_words,
            intents=intents,
            keyterm=keyterm,
            keywords=keywords,
            language=language,
            measurements=measurements,
            method=method,
            model=model,
            multichannel=multichannel,
            numerals=numerals,
            paragraphs=paragraphs,
            profanity_filter=profanity_filter,
            punctuate=punctuate,
            redact=redact,
            replace=replace,
            sample_rate=sample_rate,
            search=search,
            sentiment=sentiment,
            smart_format=smart_format,
            summarize=summarize,
            tag=tag,
            topics=topics,
            utt_split=utt_split,
            utterances=utterances,
            version=version,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageV1ProjectsUsageBreakdownWithRawResponse:
        return self._with_raw_response


class AsyncManageV1ProjectsUsageBreakdown:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageV1ProjectsUsageBreakdownWithRawResponse(client, server, auth)

    async def get9(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        grouping: V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None = None,
        accessor: str | None = None,
        alternatives: bool | None = None,
        callback_method: bool | None = None,
        callback: bool | None = None,
        channels: bool | None = None,
        custom_intent_mode: bool | None = None,
        custom_intent: bool | None = None,
        custom_topic_mode: bool | None = None,
        custom_topic: bool | None = None,
        deployment: V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None = None,
        detect_entities: bool | None = None,
        detect_language: bool | None = None,
        diarize: bool | None = None,
        dictation: bool | None = None,
        encoding: bool | None = None,
        endpoint: V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None = None,
        extra: bool | None = None,
        filler_words: bool | None = None,
        intents: bool | None = None,
        keyterm: bool | None = None,
        keywords: bool | None = None,
        language: bool | None = None,
        measurements: bool | None = None,
        method: V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None = None,
        model: str | None = None,
        multichannel: bool | None = None,
        numerals: bool | None = None,
        paragraphs: bool | None = None,
        profanity_filter: bool | None = None,
        punctuate: bool | None = None,
        redact: bool | None = None,
        replace: bool | None = None,
        sample_rate: bool | None = None,
        search: bool | None = None,
        sentiment: bool | None = None,
        smart_format: bool | None = None,
        summarize: bool | None = None,
        tag: str | None = None,
        topics: bool | None = None,
        utt_split: bool | None = None,
        utterances: bool | None = None,
        version: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageBreakdownV1Response:
        """Retrieves the usage breakdown for a specific project, with various filter options by API feature or by
        groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false
        excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND
        logic.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            grouping: Common usage grouping parameters
            accessor: Filter for requests where a specific accessor was used
            alternatives: Filter for requests where alternatives were used
            callback_method: Filter for requests where callback method was used
            callback: Filter for requests where callback was used
            channels: Filter for requests where channels were used
            custom_intent_mode: Filter for requests where custom intent mode was used
            custom_intent: Filter for requests where custom intent was used
            custom_topic_mode: Filter for requests where custom topic mode was used
            custom_topic: Filter for requests where custom topic was used
            deployment: Filter for requests where a specific deployment was used
            detect_entities: Filter for requests where detect entities was used
            detect_language: Filter for requests where detect language was used
            diarize: Filter for requests where diarize was used
            dictation: Filter for requests where dictation was used
            encoding: Filter for requests where encoding was used
            endpoint: Filter for requests where a specific endpoint was used
            extra: Filter for requests where extra was used
            filler_words: Filter for requests where filler words was used
            intents: Filter for requests where intents was used
            keyterm: Filter for requests where keyterm was used
            keywords: Filter for requests where keywords was used
            language: Filter for requests where language was used
            measurements: Filter for requests where measurements were used
            method: Filter for requests where a specific method was used
            model: Filter for requests where a specific model uuid was used
            multichannel: Filter for requests where multichannel was used
            numerals: Filter for requests where numerals were used
            paragraphs: Filter for requests where paragraphs were used
            profanity_filter: Filter for requests where profanity filter was used
            punctuate: Filter for requests where punctuate was used
            redact: Filter for requests where redact was used
            replace: Filter for requests where replace was used
            sample_rate: Filter for requests where sample rate was used
            search: Filter for requests where search was used
            sentiment: Filter for requests where sentiment was used
            smart_format: Filter for requests where smart format was used
            summarize: Filter for requests where summarize was used
            tag: Filter for requests where a specific tag was used
            topics: Filter for requests where topics was used
            utt_split: Filter for requests where utt split was used
            utterances: Filter for requests where utterances was used
            version: Filter for requests where version was used
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Usage breakdown response

        Raises:
            ApiError: Invalid Request ``error`` is ``ErrorResponse | RawError``."""
        return (
            await self._with_raw_response.get9(
                project_id,
                start=start,
                end=end,
                grouping=grouping,
                accessor=accessor,
                alternatives=alternatives,
                callback_method=callback_method,
                callback=callback,
                channels=channels,
                custom_intent_mode=custom_intent_mode,
                custom_intent=custom_intent,
                custom_topic_mode=custom_topic_mode,
                custom_topic=custom_topic,
                deployment=deployment,
                detect_entities=detect_entities,
                detect_language=detect_language,
                diarize=diarize,
                dictation=dictation,
                encoding=encoding,
                endpoint=endpoint,
                extra=extra,
                filler_words=filler_words,
                intents=intents,
                keyterm=keyterm,
                keywords=keywords,
                language=language,
                measurements=measurements,
                method=method,
                model=model,
                multichannel=multichannel,
                numerals=numerals,
                paragraphs=paragraphs,
                profanity_filter=profanity_filter,
                punctuate=punctuate,
                redact=redact,
                replace=replace,
                sample_rate=sample_rate,
                search=search,
                sentiment=sentiment,
                smart_format=smart_format,
                summarize=summarize,
                tag=tag,
                topics=topics,
                utt_split=utt_split,
                utterances=utterances,
                version=version,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageV1ProjectsUsageBreakdownWithRawResponse:
        return self._with_raw_response


class ManageV1ProjectsUsageBreakdownWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get9(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        grouping: V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None = None,
        accessor: str | None = None,
        alternatives: bool | None = None,
        callback_method: bool | None = None,
        callback: bool | None = None,
        channels: bool | None = None,
        custom_intent_mode: bool | None = None,
        custom_intent: bool | None = None,
        custom_topic_mode: bool | None = None,
        custom_topic: bool | None = None,
        deployment: V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None = None,
        detect_entities: bool | None = None,
        detect_language: bool | None = None,
        diarize: bool | None = None,
        dictation: bool | None = None,
        encoding: bool | None = None,
        endpoint: V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None = None,
        extra: bool | None = None,
        filler_words: bool | None = None,
        intents: bool | None = None,
        keyterm: bool | None = None,
        keywords: bool | None = None,
        language: bool | None = None,
        measurements: bool | None = None,
        method: V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None = None,
        model: str | None = None,
        multichannel: bool | None = None,
        numerals: bool | None = None,
        paragraphs: bool | None = None,
        profanity_filter: bool | None = None,
        punctuate: bool | None = None,
        redact: bool | None = None,
        replace: bool | None = None,
        sample_rate: bool | None = None,
        search: bool | None = None,
        sentiment: bool | None = None,
        smart_format: bool | None = None,
        summarize: bool | None = None,
        tag: str | None = None,
        topics: bool | None = None,
        utt_split: bool | None = None,
        utterances: bool | None = None,
        version: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageBreakdownV1Response, Get9ErrorBody]:
        """Retrieves the usage breakdown for a specific project, with various filter options by API feature or by
        groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false
        excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND
        logic.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            grouping: Common usage grouping parameters
            accessor: Filter for requests where a specific accessor was used
            alternatives: Filter for requests where alternatives were used
            callback_method: Filter for requests where callback method was used
            callback: Filter for requests where callback was used
            channels: Filter for requests where channels were used
            custom_intent_mode: Filter for requests where custom intent mode was used
            custom_intent: Filter for requests where custom intent was used
            custom_topic_mode: Filter for requests where custom topic mode was used
            custom_topic: Filter for requests where custom topic was used
            deployment: Filter for requests where a specific deployment was used
            detect_entities: Filter for requests where detect entities was used
            detect_language: Filter for requests where detect language was used
            diarize: Filter for requests where diarize was used
            dictation: Filter for requests where dictation was used
            encoding: Filter for requests where encoding was used
            endpoint: Filter for requests where a specific endpoint was used
            extra: Filter for requests where extra was used
            filler_words: Filter for requests where filler words was used
            intents: Filter for requests where intents was used
            keyterm: Filter for requests where keyterm was used
            keywords: Filter for requests where keywords was used
            language: Filter for requests where language was used
            measurements: Filter for requests where measurements were used
            method: Filter for requests where a specific method was used
            model: Filter for requests where a specific model uuid was used
            multichannel: Filter for requests where multichannel was used
            numerals: Filter for requests where numerals were used
            paragraphs: Filter for requests where paragraphs were used
            profanity_filter: Filter for requests where profanity filter was used
            punctuate: Filter for requests where punctuate was used
            redact: Filter for requests where redact was used
            replace: Filter for requests where replace was used
            sample_rate: Filter for requests where sample rate was used
            search: Filter for requests where search was used
            sentiment: Filter for requests where sentiment was used
            smart_format: Filter for requests where smart format was used
            summarize: Filter for requests where summarize was used
            tag: Filter for requests where a specific tag was used
            topics: Filter for requests where topics was used
            utt_split: Filter for requests where utt split was used
            utterances: Filter for requests where utterances was used
            version: Filter for requests where version was used
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/usage/breakdown"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[Date | None]("start", start),
                param[Date | None]("end", end),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None]("grouping", grouping),
                param[str | None]("accessor", accessor),
                param[bool | None]("alternatives", alternatives),
                param[bool | None]("callback_method", callback_method),
                param[bool | None]("callback", callback),
                param[bool | None]("channels", channels),
                param[bool | None]("custom_intent_mode", custom_intent_mode),
                param[bool | None]("custom_intent", custom_intent),
                param[bool | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("custom_topic", custom_topic),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[bool | None]("detect_entities", detect_entities),
                param[bool | None]("detect_language", detect_language),
                param[bool | None]("diarize", diarize),
                param[bool | None]("dictation", dictation),
                param[bool | None]("encoding", encoding),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None]("endpoint", endpoint),
                param[bool | None]("extra", extra),
                param[bool | None]("filler_words", filler_words),
                param[bool | None]("intents", intents),
                param[bool | None]("keyterm", keyterm),
                param[bool | None]("keywords", keywords),
                param[bool | None]("language", language),
                param[bool | None]("measurements", measurements),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None]("method", method),
                param[str | None]("model", model),
                param[bool | None]("multichannel", multichannel),
                param[bool | None]("numerals", numerals),
                param[bool | None]("paragraphs", paragraphs),
                param[bool | None]("profanity_filter", profanity_filter),
                param[bool | None]("punctuate", punctuate),
                param[bool | None]("redact", redact),
                param[bool | None]("replace", replace),
                param[bool | None]("sample_rate", sample_rate),
                param[bool | None]("search", search),
                param[bool | None]("sentiment", sentiment),
                param[bool | None]("smart_format", smart_format),
                param[bool | None]("summarize", summarize),
                param[str | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[bool | None]("utt_split", utt_split),
                param[bool | None]("utterances", utterances),
                param[bool | None]("version", version),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=json_decoder[UsageBreakdownV1Response],
            error_mapper=get9_error_mapper,
            request_options=request_options,
        )


class AsyncManageV1ProjectsUsageBreakdownWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get9(
        self,
        project_id: str,
        *,
        start: Date | None = None,
        end: Date | None = None,
        grouping: V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None = None,
        accessor: str | None = None,
        alternatives: bool | None = None,
        callback_method: bool | None = None,
        callback: bool | None = None,
        channels: bool | None = None,
        custom_intent_mode: bool | None = None,
        custom_intent: bool | None = None,
        custom_topic_mode: bool | None = None,
        custom_topic: bool | None = None,
        deployment: V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None = None,
        detect_entities: bool | None = None,
        detect_language: bool | None = None,
        diarize: bool | None = None,
        dictation: bool | None = None,
        encoding: bool | None = None,
        endpoint: V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None = None,
        extra: bool | None = None,
        filler_words: bool | None = None,
        intents: bool | None = None,
        keyterm: bool | None = None,
        keywords: bool | None = None,
        language: bool | None = None,
        measurements: bool | None = None,
        method: V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None = None,
        model: str | None = None,
        multichannel: bool | None = None,
        numerals: bool | None = None,
        paragraphs: bool | None = None,
        profanity_filter: bool | None = None,
        punctuate: bool | None = None,
        redact: bool | None = None,
        replace: bool | None = None,
        sample_rate: bool | None = None,
        search: bool | None = None,
        sentiment: bool | None = None,
        smart_format: bool | None = None,
        summarize: bool | None = None,
        tag: str | None = None,
        topics: bool | None = None,
        utt_split: bool | None = None,
        utterances: bool | None = None,
        version: bool | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageBreakdownV1Response, Get9ErrorBody]:
        """Retrieves the usage breakdown for a specific project, with various filter options by API feature or by
        groupings. Setting a feature (e.g. diarize) to true includes requests that used that feature, while false
        excludes requests that used it. Multiple true filters are combined with OR logic, while false filters use AND
        logic.

        Args:
            project_id: The unique identifier of the project
            start: Start date of the requested date range. Format accepted is YYYY-MM-DD
            end: End date of the requested date range. Format accepted is YYYY-MM-DD
            grouping: Common usage grouping parameters
            accessor: Filter for requests where a specific accessor was used
            alternatives: Filter for requests where alternatives were used
            callback_method: Filter for requests where callback method was used
            callback: Filter for requests where callback was used
            channels: Filter for requests where channels were used
            custom_intent_mode: Filter for requests where custom intent mode was used
            custom_intent: Filter for requests where custom intent was used
            custom_topic_mode: Filter for requests where custom topic mode was used
            custom_topic: Filter for requests where custom topic was used
            deployment: Filter for requests where a specific deployment was used
            detect_entities: Filter for requests where detect entities was used
            detect_language: Filter for requests where detect language was used
            diarize: Filter for requests where diarize was used
            dictation: Filter for requests where dictation was used
            encoding: Filter for requests where encoding was used
            endpoint: Filter for requests where a specific endpoint was used
            extra: Filter for requests where extra was used
            filler_words: Filter for requests where filler words was used
            intents: Filter for requests where intents was used
            keyterm: Filter for requests where keyterm was used
            keywords: Filter for requests where keywords was used
            language: Filter for requests where language was used
            measurements: Filter for requests where measurements were used
            method: Filter for requests where a specific method was used
            model: Filter for requests where a specific model uuid was used
            multichannel: Filter for requests where multichannel was used
            numerals: Filter for requests where numerals were used
            paragraphs: Filter for requests where paragraphs were used
            profanity_filter: Filter for requests where profanity filter was used
            punctuate: Filter for requests where punctuate was used
            redact: Filter for requests where redact was used
            replace: Filter for requests where replace was used
            sample_rate: Filter for requests where sample rate was used
            search: Filter for requests where search was used
            sentiment: Filter for requests where sentiment was used
            smart_format: Filter for requests where smart format was used
            summarize: Filter for requests where summarize was used
            tag: Filter for requests where a specific tag was used
            topics: Filter for requests where topics was used
            utt_split: Filter for requests where utt split was used
            utterances: Filter for requests where utterances was used
            version: Filter for requests where version was used
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{project_id}/usage/breakdown"),
            path_params=[param[str]("project_id", project_id)],
            query_params=[
                param[Date | None]("start", start),
                param[Date | None]("end", end),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersGroupingOrStr | None]("grouping", grouping),
                param[str | None]("accessor", accessor),
                param[bool | None]("alternatives", alternatives),
                param[bool | None]("callback_method", callback_method),
                param[bool | None]("callback", callback),
                param[bool | None]("channels", channels),
                param[bool | None]("custom_intent_mode", custom_intent_mode),
                param[bool | None]("custom_intent", custom_intent),
                param[bool | None]("custom_topic_mode", custom_topic_mode),
                param[bool | None]("custom_topic", custom_topic),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersDeploymentOrStr | None]("deployment", deployment),
                param[bool | None]("detect_entities", detect_entities),
                param[bool | None]("detect_language", detect_language),
                param[bool | None]("diarize", diarize),
                param[bool | None]("dictation", dictation),
                param[bool | None]("encoding", encoding),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersEndpointOrStr | None]("endpoint", endpoint),
                param[bool | None]("extra", extra),
                param[bool | None]("filler_words", filler_words),
                param[bool | None]("intents", intents),
                param[bool | None]("keyterm", keyterm),
                param[bool | None]("keywords", keywords),
                param[bool | None]("language", language),
                param[bool | None]("measurements", measurements),
                param[V1ProjectsProjectIdUsageBreakdownGetParametersMethodOrStr | None]("method", method),
                param[str | None]("model", model),
                param[bool | None]("multichannel", multichannel),
                param[bool | None]("numerals", numerals),
                param[bool | None]("paragraphs", paragraphs),
                param[bool | None]("profanity_filter", profanity_filter),
                param[bool | None]("punctuate", punctuate),
                param[bool | None]("redact", redact),
                param[bool | None]("replace", replace),
                param[bool | None]("sample_rate", sample_rate),
                param[bool | None]("search", search),
                param[bool | None]("sentiment", sentiment),
                param[bool | None]("smart_format", smart_format),
                param[bool | None]("summarize", summarize),
                param[str | None]("tag", tag),
                param[bool | None]("topics", topics),
                param[bool | None]("utt_split", utt_split),
                param[bool | None]("utterances", utterances),
                param[bool | None]("version", version),
            ],
            auth_scheme=self._auth.api_key_auth,
            decoder=async_json_decoder[UsageBreakdownV1Response],
            error_mapper=get9_error_mapper,
            request_options=request_options,
        )
