# Feedback
(*feedback*)

## Overview

### Available Operations

* [create](#create) - Submit feedback

## create

Submit feedback for the LLM transaction via the API

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.feedback.create(property2="rating", value=[
    "good",
], trace_id="67HTZ65Z9W91HSF51CW68KK1QH")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                             | Type                                                                                                                                                  | Required                                                                                                                                              | Description                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `property2`                                                                                                                                           | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | A string describing the specific property or aspect rated.                                                                                            |
| `value`                                                                                                                                               | [models.Value](../../models/value.md)                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The feedback value. For single selection of multiple choice, the value should be an array of strings. For `correction`, the value should be a string. |
| `trace_id`                                                                                                                                            | *str*                                                                                                                                                 | :heavy_check_mark:                                                                                                                                    | The id returned by the [`get_config`]() or [`invoke`](https://docs.orq.ai/reference/post_deployments-invoke-1) endpoints                              |
| `retries`                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                      | :heavy_minus_sign:                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                   |

### Response

**[models.CreateFeedbackResponseBody](../../models/createfeedbackresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |