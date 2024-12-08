"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from enum import Enum
from orq_poc_python_client import models, utils
from orq_poc_python_client._hooks import HookContext
from orq_poc_python_client.types import OptionalNullable, UNSET
from orq_poc_python_client.utils import eventstreaming, get_security_from_env
from typing import List, Optional, Union


class CreateAcceptEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    TEXT_EVENT_STREAM = "text/event-stream"


class OrqCompletions(BaseSDK):
    def create(
        self,
        *,
        model: str,
        messages: Union[
            List[models.RouterChatCompletionsMessages],
            List[models.RouterChatCompletionsMessagesTypedDict],
        ],
        frequency_penalty: OptionalNullable[float] = 0,
        max_tokens: OptionalNullable[float] = UNSET,
        presence_penalty: OptionalNullable[float] = 0,
        seed: OptionalNullable[float] = UNSET,
        stream: OptionalNullable[bool] = False,
        temperature: OptionalNullable[float] = 1,
        top_p: OptionalNullable[float] = 1,
        tools: Optional[Union[List[models.Tools], List[models.ToolsTypedDict]]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[CreateAcceptEnum] = None,
    ) -> models.RouterChatCompletionsResponse:
        r"""Chat

        For sending requests to chat completion models

        :param model: ID of the model to use
        :param messages: A list of messages comprising the conversation so far.
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
        :param max_tokens: The maximum number of tokens that can be generated in the chat completion.
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
        :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.
        :param stream: If set, partial message deltas will be sent, like in ChatGPT.
        :param temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param top_p: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
        :param tools: A list of tools the model may call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if timeout_ms is None:
            timeout_ms = 600000

        if server_url is not None:
            base_url = server_url

        request = models.RouterChatCompletionsRequestBody(
            model=model,
            messages=utils.get_pydantic_model(
                messages, List[models.RouterChatCompletionsMessages]
            ),
            frequency_penalty=frequency_penalty,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty,
            seed=seed,
            stream=stream,
            temperature=temperature,
            top_p=top_p,
            tools=utils.get_pydantic_model(tools, Optional[List[models.Tools]]),
        )

        req = self.build_request(
            method="POST",
            path="/v2/router/chat/completions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/event-stream;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RouterChatCompletionsRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="RouterChatCompletions",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            http_response_text = utils.stream_to_text(http_res)
            return utils.unmarshal_json(
                http_response_text, models.RouterChatCompletionsResponseBody
            )
        if utils.match_response(http_res, "200", "text/event-stream"):
            return eventstreaming.stream_events(
                http_res,
                lambda raw: utils.unmarshal_json(
                    raw, models.RouterChatCompletionsRouterChatCompletionsResponseBody
                ),
                sentinel="[DONE]",
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def create_async(
        self,
        *,
        model: str,
        messages: Union[
            List[models.RouterChatCompletionsMessages],
            List[models.RouterChatCompletionsMessagesTypedDict],
        ],
        frequency_penalty: OptionalNullable[float] = 0,
        max_tokens: OptionalNullable[float] = UNSET,
        presence_penalty: OptionalNullable[float] = 0,
        seed: OptionalNullable[float] = UNSET,
        stream: OptionalNullable[bool] = False,
        temperature: OptionalNullable[float] = 1,
        top_p: OptionalNullable[float] = 1,
        tools: Optional[Union[List[models.Tools], List[models.ToolsTypedDict]]] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        accept_header_override: Optional[CreateAcceptEnum] = None,
    ) -> models.RouterChatCompletionsResponse:
        r"""Chat

        For sending requests to chat completion models

        :param model: ID of the model to use
        :param messages: A list of messages comprising the conversation so far.
        :param frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
        :param max_tokens: The maximum number of tokens that can be generated in the chat completion.
        :param presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
        :param seed: If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.
        :param stream: If set, partial message deltas will be sent, like in ChatGPT.
        :param temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
        :param top_p: An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
        :param tools: A list of tools the model may call.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param accept_header_override: Override the default accept header for this method
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if timeout_ms is None:
            timeout_ms = 600000

        if server_url is not None:
            base_url = server_url

        request = models.RouterChatCompletionsRequestBody(
            model=model,
            messages=utils.get_pydantic_model(
                messages, List[models.RouterChatCompletionsMessages]
            ),
            frequency_penalty=frequency_penalty,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty,
            seed=seed,
            stream=stream,
            temperature=temperature,
            top_p=top_p,
            tools=utils.get_pydantic_model(tools, Optional[List[models.Tools]]),
        )

        req = self.build_request_async(
            method="POST",
            path="/v2/router/chat/completions",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value=accept_header_override.value
            if accept_header_override is not None
            else "application/json;q=1, text/event-stream;q=0",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.RouterChatCompletionsRequestBody
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="RouterChatCompletions",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            stream=True,
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            http_response_text = await utils.stream_to_text_async(http_res)
            return utils.unmarshal_json(
                http_response_text, models.RouterChatCompletionsResponseBody
            )
        if utils.match_response(http_res, "200", "text/event-stream"):
            return eventstreaming.stream_events_async(
                http_res,
                lambda raw: utils.unmarshal_json(
                    raw, models.RouterChatCompletionsRouterChatCompletionsResponseBody
                ),
                sentinel="[DONE]",
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
