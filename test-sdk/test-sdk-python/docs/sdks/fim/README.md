# Fim
(*fim*)

## Overview

Fill-in-the-middle API.

### Available Operations

* [fim_completion_v1_fim_completions_post](#fim_completion_v1_fim_completions_post) - Fim Completion

## fim_completion_v1_fim_completions_post

FIM completion.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fim.fim_completion_v1_fim_completions_post(request={
    "model": "codestral-2405",
    "prompt": "def",
    "suffix": "return a+b",
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.FIMCompletionRequest](../../models/fimcompletionrequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.FimCompletionV1FimCompletionsPostResponse](../../models/fimcompletionv1fimcompletionspostresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |