# Resources
(*resources*)

## Overview

### Available Operations

* [post_v2_resources_datasets](#post_v2_resources_datasets) - Create a dataset
* [get_v2_resources_datasets](#get_v2_resources_datasets) - Get all datasets
* [delete_v2_resources_datasets_dataset_id_](#delete_v2_resources_datasets_dataset_id_) - Delete a dataset
* [get_v2_resources_datasets_dataset_id_](#get_v2_resources_datasets_dataset_id_) - Get one  dataset
* [patch_v2_resources_datasets_dataset_id_](#patch_v2_resources_datasets_dataset_id_) - Update a dataset
* [post_v2_resources_datasets_dataset_id_rows_bulk](#post_v2_resources_datasets_dataset_id_rows_bulk) - Create a list of dataset rows
* [delete_v2_resources_datasets_dataset_id_rows_bulk](#delete_v2_resources_datasets_dataset_id_rows_bulk) - Delete a list of dataset rows
* [post_v2_resources_datasets_dataset_id_rows](#post_v2_resources_datasets_dataset_id_rows) - Create a dataset row
* [get_v2_resources_datasets_dataset_id_rows](#get_v2_resources_datasets_dataset_id_rows) - Retrieve all dataset rows
* [delete_v2_resources_datasets_dataset_id_rows_row_id_](#delete_v2_resources_datasets_dataset_id_rows_row_id_) - Delete a dataset row
* [get_v2_resources_datasets_dataset_id_rows_row_id_](#get_v2_resources_datasets_dataset_id_rows_row_id_) - Get one dataset row
* [patch_v2_resources_datasets_dataset_id_rows_row_id_](#patch_v2_resources_datasets_dataset_id_rows_row_id_) - Update a dataset row

## post_v2_resources_datasets

Create a dataset

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.post_v2_resources_datasets()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `request`                                                                                       | [models.PostV2ResourcesDatasetsRequestBody](../../models/postv2resourcesdatasetsrequestbody.md) | :heavy_check_mark:                                                                              | The request object to use for the request.                                                      |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.PostV2ResourcesDatasetsResponseBody](../../models/postv2resourcesdatasetsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_v2_resources_datasets

Get all datasets

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.get_v2_resources_datasets(page=1698.73, limit=6833.85)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `page`                                                              | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `limit`                                                             | *float*                                                             | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ResourcesDatasetsResponseBody](../../models/getv2resourcesdatasetsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_v2_resources_datasets_dataset_id_

Delete a dataset

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

s.resources.delete_v2_resources_datasets_dataset_id_(dataset_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_v2_resources_datasets_dataset_id_

Get one  dataset

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.get_v2_resources_datasets_dataset_id_(dataset_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ResourcesDatasetsDatasetIDResponseBody](../../models/getv2resourcesdatasetsdatasetidresponsebody.md)**

### Errors

| Error Type                                                  | Status Code                                                 | Content Type                                                |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| models.GetV2ResourcesDatasetsDatasetIDResourcesResponseBody | 404                                                         | application/json                                            |
| models.SDKError                                             | 4XX, 5XX                                                    | \*/\*                                                       |

## patch_v2_resources_datasets_dataset_id_

Update a dataset

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.patch_v2_resources_datasets_dataset_id_(dataset_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                     | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                  | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | Dataset ID                                                                                                                    |
| `request_body`                                                                                                                | [Optional[models.PatchV2ResourcesDatasetsDatasetIDRequestBody]](../../models/patchv2resourcesdatasetsdatasetidrequestbody.md) | :heavy_minus_sign:                                                                                                            | N/A                                                                                                                           |
| `retries`                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                              | :heavy_minus_sign:                                                                                                            | Configuration to override the default retry behavior of the client.                                                           |

### Response

**[models.PatchV2ResourcesDatasetsDatasetIDResponseBody](../../models/patchv2resourcesdatasetsdatasetidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_resources_datasets_dataset_id_rows_bulk

Create a list of dataset rows

### Example Usage

```python
import orq_python_client
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.post_v2_resources_datasets_dataset_id_rows_bulk(dataset_id="<id>", request_body={
    "dataset_rows": [
        {
            "messages": [
                {
                    "role": orq_python_client.PostV2ResourcesDatasetsDatasetIDRowsBulkRole.ASSISTANT,
                    "content": "You are a helpful assistant.",
                    "tool_calls": [
                        {
                            "type": orq_python_client.PostV2ResourcesDatasetsDatasetIDRowsBulkType.FUNCTION,
                            "function": {
                                "name": "some-function",
                                "arguments": "some-args",
                            },
                            "id": "tool-id",
                            "index": 0,
                        },
                    ],
                },
            ],
        },
    ],
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                                | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | Dataset ID                                                                                                                                  |
| `request_body`                                                                                                                              | [Optional[models.PostV2ResourcesDatasetsDatasetIDRowsBulkRequestBody]](../../models/postv2resourcesdatasetsdatasetidrowsbulkrequestbody.md) | :heavy_minus_sign:                                                                                                                          | N/A                                                                                                                                         |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |

### Response

**[List[models.PostV2ResourcesDatasetsDatasetIDRowsBulkResponseBody]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_v2_resources_datasets_dataset_id_rows_bulk

Delete a list of dataset rows

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

s.resources.delete_v2_resources_datasets_dataset_id_rows_bulk(dataset_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_resources_datasets_dataset_id_rows

Create a dataset row

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.post_v2_resources_datasets_dataset_id_rows(dataset_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                        | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Dataset ID                                                                                                                          |
| `request_body`                                                                                                                      | [Optional[models.PostV2ResourcesDatasetsDatasetIDRowsRequestBody]](../../models/postv2resourcesdatasetsdatasetidrowsrequestbody.md) | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.PostV2ResourcesDatasetsDatasetIDRowsResponseBody](../../models/postv2resourcesdatasetsdatasetidrowsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_v2_resources_datasets_dataset_id_rows

Retrieve all dataset rows

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.get_v2_resources_datasets_dataset_id_rows(dataset_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ResourcesDatasetsDatasetIDRowsResponseBody](../../models/getv2resourcesdatasetsdatasetidrowsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## delete_v2_resources_datasets_dataset_id_rows_row_id_

Delete a dataset row

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

s.resources.delete_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `row_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Dataset row ID                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## get_v2_resources_datasets_dataset_id_rows_row_id_

Get one dataset row

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.get_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `dataset_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Dataset ID                                                          |
| `row_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | Dataset row ID                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetV2ResourcesDatasetsDatasetIDRowsRowIDResponseBody](../../models/getv2resourcesdatasetsdatasetidrowsrowidresponsebody.md)**

### Errors

| Error Type                                                           | Status Code                                                          | Content Type                                                         |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| models.GetV2ResourcesDatasetsDatasetIDRowsRowIDResourcesResponseBody | 404                                                                  | application/json                                                     |
| models.SDKError                                                      | 4XX, 5XX                                                             | \*/\*                                                                |

## patch_v2_resources_datasets_dataset_id_rows_row_id_

Update a dataset row

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.resources.patch_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                       | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `dataset_id`                                                                                                                                    | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | Dataset ID                                                                                                                                      |
| `row_id`                                                                                                                                        | *str*                                                                                                                                           | :heavy_check_mark:                                                                                                                              | Dataset row ID                                                                                                                                  |
| `request_body`                                                                                                                                  | [Optional[models.PatchV2ResourcesDatasetsDatasetIDRowsRowIDRequestBody]](../../models/patchv2resourcesdatasetsdatasetidrowsrowidrequestbody.md) | :heavy_minus_sign:                                                                                                                              | N/A                                                                                                                                             |
| `retries`                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                             |

### Response

**[models.PatchV2ResourcesDatasetsDatasetIDRowsRowIDResponseBody](../../models/patchv2resourcesdatasetsdatasetidrowsrowidresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |