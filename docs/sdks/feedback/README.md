# Feedback
(*feedback*)

## Overview

### Available Operations

* [post_feedback](#post_feedback) - Submit feedback

## post_feedback

Submit feedback for the LLM transaction via the API

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.feedback.post_feedback(request={
    "property": "rating",
    "value": [
        "good",
    ],
    "trace_id": "67HTZ65Z9W91HSF51CW68KK1QH",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.PostFeedbackRequestBody](../../models/postfeedbackrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.PostFeedbackResponseBody](../../models/postfeedbackresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |