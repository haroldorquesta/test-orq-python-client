# Chat
(*chat*)

## Overview

Chat Completion API.

### Available Operations

* [chat_completion_v1_chat_completions_post](#chat_completion_v1_chat_completions_post) - Chat Completion

## chat_completion_v1_chat_completions_post

Chat Completion

### Example Usage

```python
import os
import test_sdk
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.chat.chat_completion_v1_chat_completions_post(request={
    "model": "mistral-small-latest",
    "messages": [
        {
            "content": "Who is the best French painter? Answer in one short sentence.",
            "role": test_sdk.UserMessageRole.USER,
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.ChatCompletionRequest](../../models/chatcompletionrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.ChatCompletionV1ChatCompletionsPostResponse](../../models/chatcompletionv1chatcompletionspostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |