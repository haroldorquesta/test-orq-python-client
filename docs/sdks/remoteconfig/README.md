# Remoteconfig
(*remoteconfig*)

## Overview

### Available Operations

* [post_v2_remoteconfigs](#post_v2_remoteconfigs)

## post_v2_remoteconfigs

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.remoteconfig.post_v2_remoteconfigs()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.PostV2RemoteconfigsRequestBody](../../models/postv2remoteconfigsrequestbody.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.PostV2RemoteconfigsResponseBody](../../models/postv2remoteconfigsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |