# Embeddings
(*router.embeddings*)

## Overview

### Available Operations

* [create](#create) - Embeddings

## create

Creates an embedding vector representing the input text.

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.router.embeddings.create(input_="<value>", model="LeBaron")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `input`                                                               | [models.Input](../../models/input.md)                                 | :heavy_check_mark:                                                    | Input text to embed, encoded as a string or array of tokens.          |
| `model`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | ID of the model to use                                                |
| `encoding_format`                                                     | [Optional[models.EncodingFormat]](../../models/encodingformat.md)     | :heavy_minus_sign:                                                    | Type of the document element                                          |
| `dimensions`                                                          | *Optional[float]*                                                     | :heavy_minus_sign:                                                    | The number of dimensions the resulting output embeddings should have. |
| `user`                                                                | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | A unique identifier representing your end-user                        |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.RouterEmbeddingResponseBody](../../models/routerembeddingresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |