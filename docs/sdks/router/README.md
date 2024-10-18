# Router
(*router*)

## Overview

### Available Operations

* [post_v2_router_embeddings](#post_v2_router_embeddings) - Embeddings
* [post_v2_router_chat_completions](#post_v2_router_chat_completions) - Chat
* [post_v2_router_completions](#post_v2_router_completions) - legacy completions route
* [post_v2_router_rerank](#post_v2_router_rerank) - rerank route
* [post_v2_router_images_generations](#post_v2_router_images_generations)

## post_v2_router_embeddings

Creates an embedding vector representing the input text.

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.router.post_v2_router_embeddings(request={
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

res = s.router.post_v2_router_chat_completions(request={
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

res = s.router.post_v2_router_completions()

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

res = s.router.post_v2_router_rerank()

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

res = s.router.post_v2_router_images_generations()

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