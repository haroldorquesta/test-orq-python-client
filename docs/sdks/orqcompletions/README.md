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
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.router.chat.completions.create(request={
    "model": "Fiesta",
    "messages": [
        {
            "role": orq_poc_python_client.RouterChatCompletionsMessagesRole.USER,
            "content": "<value>",
        },
        {
            "role": orq_poc_python_client.MessagesRole.SYSTEM,
            "content": [
                {
                    "type": orq_poc_python_client.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
                {
                    "type": orq_poc_python_client.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
                {
                    "type": orq_poc_python_client.RouterChatCompletions2Type.TEXT,
                    "text": "<value>",
                },
            ],
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.RouterChatCompletionsRequestBody](../../models/routerchatcompletionsrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.RouterChatCompletionsResponse](../../models/routerchatcompletionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |