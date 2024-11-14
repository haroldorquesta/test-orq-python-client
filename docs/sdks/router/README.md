# Router
(*router*)

## Overview

### Available Operations

* [rerank](#rerank) - rerank route

## rerank

For sending requests to rerank models

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.router.rerank()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `request`                                                                 | [models.RouterRerankRequestBody](../../models/routerrerankrequestbody.md) | :heavy_check_mark:                                                        | The request object to use for the request.                                |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.RouterRerankResponseBody](../../models/routerrerankresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |