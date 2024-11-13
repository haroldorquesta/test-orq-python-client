# OrqCompletions
(*router.chat.completions*)

## Overview

### Available Operations

* [create](#create) - Chat

## create

For sending requests to chat completion models

### Example Usage

```python
import orq_poc_python_client
from orq_poc_python_client import Orq
import os

s = Orq(
    open_ai=os.getenv("ORQ_OPEN_AI", ""),
)

res = s.router.chat.completions.create(request={
    "model": "Land Cruiser",
    "messages": [
        {
            "role": orq_poc_python_client.PostV2RouterChatCompletionsMessagesRouterChatCompletionsRequestRole.TOOL,
            "tool_call_id": "<id>",
            "content": "<value>",
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.PostV2RouterChatCompletionsRequestBody](../../models/postv2routerchatcompletionsrequestbody.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.PostV2RouterChatCompletionsResponse](../../models/postv2routerchatcompletionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |