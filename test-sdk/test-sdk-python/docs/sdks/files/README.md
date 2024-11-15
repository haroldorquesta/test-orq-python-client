# Files
(*files*)

## Overview

Files API

### Available Operations

* [files_api_routes_upload_file](#files_api_routes_upload_file) - Upload File
* [files_api_routes_list_files](#files_api_routes_list_files) - List Files
* [files_api_routes_retrieve_file](#files_api_routes_retrieve_file) - Retrieve File
* [files_api_routes_delete_file](#files_api_routes_delete_file) - Delete File
* [files_api_routes_download_file](#files_api_routes_download_file) - Download File

## files_api_routes_upload_file

Upload a file that can be used across various endpoints.

The size of individual files can be a maximum of 512 MB. The Fine-tuning API only supports .jsonl files.

Please contact us if you need to increase these storage limits.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.files.files_api_routes_upload_file(request={
    "file": {
        "file_name": "example.file",
        "content": open("example.file", "rb"),
    },
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                         | Type                                                                                                              | Required                                                                                                          | Description                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                         | [models.FilesAPIRoutesUploadFileMultiPartBodyParams](../../models/filesapiroutesuploadfilemultipartbodyparams.md) | :heavy_check_mark:                                                                                                | The request object to use for the request.                                                                        |
| `retries`                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                  | :heavy_minus_sign:                                                                                                | Configuration to override the default retry behavior of the client.                                               |

### Response

**[models.UploadFileOut](../../models/uploadfileout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## files_api_routes_list_files

Returns a list of files that belong to the user's organization.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.files.files_api_routes_list_files()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.FilesAPIRoutesListFilesRequest](../../models/filesapirouteslistfilesrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.ListFilesOut](../../models/listfilesout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## files_api_routes_retrieve_file

Returns information about a specific file.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.files.files_api_routes_retrieve_file(file_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.RetrieveFileOut](../../models/retrievefileout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## files_api_routes_delete_file

Delete a file.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.files.files_api_routes_delete_file(file_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteFileOut](../../models/deletefileout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## files_api_routes_download_file

Download a file

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.files.files_api_routes_download_file(file_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `file_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |