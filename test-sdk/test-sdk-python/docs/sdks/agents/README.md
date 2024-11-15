# Agents
(*agents*)

## Overview

Agents API.

### Available Operations

* [agents_completion_v1_agents_completions_post](#agents_completion_v1_agents_completions_post) - Agents Completion

## agents_completion_v1_agents_completions_post

Agents Completion

### Example Usage

```python
import os
import test_sdk
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.agents.agents_completion_v1_agents_completions_post(request={
    "messages": [
        {
            "content": "Who is the best French painter? Answer in one short sentence.",
            "role": test_sdk.UserMessageRole.USER,
        },
    ],
    "agent_id": "<id>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.AgentsCompletionRequest](../../models/agentscompletionrequest.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.ChatCompletionResponse](../../models/chatcompletionresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |