# Files
(*files*)

## Overview

### Available Operations

* [upload](#upload) - Upload file
* [bulk_upload](#bulk_upload) - Bulk upload file

## upload

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.files.upload()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.PostV2FilesRequestBody](../../models/postv2filesrequestbody.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PostV2FilesResponseBody](../../models/postv2filesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## bulk_upload

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
import orq_poc_python_client
from orq_poc_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.files.bulk_upload(request={
    "files": [
        {
            "file_name": "example.file",
            "content": open("example.file", "rb"),
        },
    ],
    "purpose": orq_poc_python_client.PostV2FilesBulkPurpose.RETRIEVAL,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `request`                                                                       | [models.PostV2FilesBulkRequestBody](../../models/postv2filesbulkrequestbody.md) | :heavy_check_mark:                                                              | The request object to use for the request.                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |