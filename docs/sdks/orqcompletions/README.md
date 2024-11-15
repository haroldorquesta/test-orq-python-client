# OrqCompletions
(*router.chat.completions*)

## Overview

### Available Operations

* [create](#create) - Chat

## create

For sending requests to chat completion models

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.router.chat.completions.create(model="Fiesta", messages=[
    {
        "role": "user",
        "content": "<value>",
    },
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "<value>",
            },
            {
                "type": "text",
                "text": "<value>",
            },
            {
                "type": "text",
                "text": "<value>",
            },
        ],
    },
])

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                                                                                                                  | Type                                                                                                                                                                                       | Required                                                                                                                                                                                   | Description                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `model`                                                                                                                                                                                    | *str*                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                         | ID of the model to use                                                                                                                                                                     |
| `messages`                                                                                                                                                                                 | List[[models.RouterChatCompletionsMessages](../../models/routerchatcompletionsmessages.md)]                                                                                                | :heavy_check_mark:                                                                                                                                                                         | A list of messages comprising the conversation so far.                                                                                                                                     |
| `frequency_penalty`                                                                                                                                                                        | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. |
| `max_tokens`                                                                                                                                                                               | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | The maximum number of tokens that can be generated in the chat completion.                                                                                                                 |
| `presence_penalty`                                                                                                                                                                         | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.              |
| `seed`                                                                                                                                                                                     | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same seed and parameters should return the same result.                 |
| `stream`                                                                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                         | If set, partial message deltas will be sent, like in ChatGPT.                                                                                                                              |
| `temperature`                                                                                                                                                                              | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.       |
| `top_p`                                                                                                                                                                                    | *OptionalNullable[float]*                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                         | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.                                     |
| `tools`                                                                                                                                                                                    | List[[models.Tools](../../models/tools.md)]                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                         | A list of tools the model may call.                                                                                                                                                        |
| `retries`                                                                                                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                         | Configuration to override the default retry behavior of the client.                                                                                                                        |

### Response

**[models.RouterChatCompletionsResponse](../../models/routerchatcompletionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |