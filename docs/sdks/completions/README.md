# Completions
(*router.completions*)

## Overview

### Available Operations

* [create](#create) - legacy completions route

## create

For sending requests to legacy completion models

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    open_ai=os.getenv("ORQ_OPEN_AI", ""),
)

res = s.router.completions.create()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.PostV2RouterCompletionsRequestBody](../../models/postv2routercompletionsrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.PostV2RouterCompletionsResponseBody](../../models/postv2routercompletionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |