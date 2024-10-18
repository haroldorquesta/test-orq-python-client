# Public
(*public*)

## Overview

### Available Operations

* [post_v2_deployments_get_config](#post_v2_deployments_get_config) - Get config
* [post_v2_deployments_invoke](#post_v2_deployments_invoke) - Invoke
* [post_v2_deployments_id_metrics](#post_v2_deployments_id_metrics) - Add metrics
* [post_v2_files](#post_v2_files) - Upload file
* [post_v2_files_bulk](#post_v2_files_bulk) - Bulk upload file
* [post_v2_router_embeddings](#post_v2_router_embeddings) - Embeddings
* [post_v2_router_chat_completions](#post_v2_router_chat_completions) - Chat
* [post_v2_router_completions](#post_v2_router_completions) - legacy completions route
* [post_v2_router_rerank](#post_v2_router_rerank) - rerank route
* [post_v2_router_images_generations](#post_v2_router_images_generations)
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

## post_v2_deployments_get_config

Retrieve the deployment configuration

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_deployments_get_config(request={
    "key": "<key>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.PostV2DeploymentsGetConfigRequestBody](../../models/postv2deploymentsgetconfigrequestbody.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.PostV2DeploymentsGetConfigResponseBody](../../models/postv2deploymentsgetconfigresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_deployments_invoke

Invoke a deployment with a given payload

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_deployments_invoke(request={
    "key": "<key>",
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.Deployments](../../models/deployments.md)                   | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PostV2DeploymentsInvokeResponse](../../models/postv2deploymentsinvokeresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_deployments_id_metrics

Add metrics to a deployment

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_deployments_id_metrics(id="<id>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `id`                                                                                                  | *str*                                                                                                 | :heavy_check_mark:                                                                                    | Deployment ID                                                                                         |
| `request_body`                                                                                        | [models.PostV2DeploymentsIDMetricsRequestBody](../../models/postv2deploymentsidmetricsrequestbody.md) | :heavy_check_mark:                                                                                    | The deployment request payload                                                                        |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.PostV2DeploymentsIDMetricsResponseBody](../../models/postv2deploymentsidmetricsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_files

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_files()

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

## post_v2_files_bulk

Files are used to upload documents that can be used with features like [Deployments](https://docs.orq.ai/reference/post_v2-deployments-get-config).

### Example Usage

```python
import orq_python_client
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_files_bulk(request={
    "files": [
        "<value>",
    ],
    "purpose": orq_python_client.PostV2FilesBulkPurpose.RETRIEVAL,
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

## post_v2_router_embeddings

Creates an embedding vector representing the input text.

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_router_embeddings(request={
    "input": "<value>",
    "model": "Accord",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `request`                                                                                     | [models.PostV2RouterEmbeddingsRequestBody](../../models/postv2routerembeddingsrequestbody.md) | :heavy_check_mark:                                                                            | The request object to use for the request.                                                    |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.PostV2RouterEmbeddingsResponseBody](../../models/postv2routerembeddingsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_router_chat_completions

For sending requests to chat completion models

### Example Usage

```python
import orq_python_client
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_router_chat_completions(request={
    "model": "Land Cruiser",
    "messages": [
        {
            "role": orq_python_client.PostV2RouterChatCompletionsMessagesRouterPublicRole.TOOL,
            "tool_call_id": "<id>",
            "content": "<value>",
        },
    ],
})

if res is not None:
    for event in res:
        # handle event
        print(event, flush=True)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `request`                                                                                               | [models.PostV2RouterChatCompletionsRequestBody](../../models/postv2routerchatcompletionsrequestbody.md) | :heavy_check_mark:                                                                                      | The request object to use for the request.                                                              |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.PostV2RouterChatCompletionsResponse](../../models/postv2routerchatcompletionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_router_completions

For sending requests to legacy completion models

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_router_completions()

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

## post_v2_router_rerank

For sending requests to rerank models

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_router_rerank()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `request`                                                                             | [models.PostV2RouterRerankRequestBody](../../models/postv2routerrerankrequestbody.md) | :heavy_check_mark:                                                                    | The request object to use for the request.                                            |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.PostV2RouterRerankResponseBody](../../models/postv2routerrerankresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_router_images_generations

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_router_images_generations()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                   | [models.PostV2RouterImagesGenerationsRequestBody](../../models/postv2routerimagesgenerationsrequestbody.md) | :heavy_check_mark:                                                                                          | The request object to use for the request.                                                                  |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.PostV2RouterImagesGenerationsResponseBody](../../models/postv2routerimagesgenerationsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |

## post_v2_resources_datasets

Create a dataset

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.public.post_v2_resources_datasets()

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

res = s.public.get_v2_resources_datasets(page=1698.73, limit=6833.85)

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

s.public.delete_v2_resources_datasets_dataset_id_(dataset_id="<id>")

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

res = s.public.get_v2_resources_datasets_dataset_id_(dataset_id="<id>")

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

res = s.public.patch_v2_resources_datasets_dataset_id_(dataset_id="<id>")

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

res = s.public.post_v2_resources_datasets_dataset_id_rows_bulk(dataset_id="<id>", request_body={
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

s.public.delete_v2_resources_datasets_dataset_id_rows_bulk(dataset_id="<id>")

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

res = s.public.post_v2_resources_datasets_dataset_id_rows(dataset_id="<id>")

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

res = s.public.get_v2_resources_datasets_dataset_id_rows(dataset_id="<id>")

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

s.public.delete_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

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

res = s.public.get_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

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

res = s.public.patch_v2_resources_datasets_dataset_id_rows_row_id_(dataset_id="<id>", row_id="<id>")

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