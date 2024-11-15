# Models
(*models*)

## Overview

Model Management API

### Available Operations

* [list_models_v1_models_get](#list_models_v1_models_get) - List Models
* [retrieve_model_v1_models_model_id_get](#retrieve_model_v1_models_model_id_get) - Retrieve Model
* [delete_model_v1_models_model_id_delete](#delete_model_v1_models_model_id_delete) - Delete Model
* [jobs_api_routes_fine_tuning_update_fine_tuned_model](#jobs_api_routes_fine_tuning_update_fine_tuned_model) - Update Fine Tuned Model
* [jobs_api_routes_fine_tuning_archive_fine_tuned_model](#jobs_api_routes_fine_tuning_archive_fine_tuned_model) - Archive Fine Tuned Model
* [jobs_api_routes_fine_tuning_unarchive_fine_tuned_model](#jobs_api_routes_fine_tuning_unarchive_fine_tuned_model) - Unarchive Fine Tuned Model

## list_models_v1_models_get

List all models available to the user.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.list_models_v1_models_get()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelList](../../models/modellist.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## retrieve_model_v1_models_model_id_get

Retrieve a model information.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.retrieve_model_v1_models_model_id_get(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to retrieve.                                    | ft:open-mistral-7b:587a6b29:20240514:7e773925                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.RetrieveModelV1ModelsModelIDGetResponseRetrieveModelV1ModelsModelIDGet](../../models/retrievemodelv1modelsmodelidgetresponseretrievemodelv1modelsmodelidget.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## delete_model_v1_models_model_id_delete

Delete a fine-tuned model.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.delete_model_v1_models_model_id_delete(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to delete.                                      | ft:open-mistral-7b:587a6b29:20240514:7e773925                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteModelOut](../../models/deletemodelout.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.APIError            | 4XX, 5XX                   | \*/\*                      |

## jobs_api_routes_fine_tuning_update_fine_tuned_model

Update a model name or description.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.jobs_api_routes_fine_tuning_update_fine_tuned_model(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925", update_ft_model_in={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to update.                                      | ft:open-mistral-7b:587a6b29:20240514:7e773925                       |
| `update_ft_model_in`                                                | [models.UpdateFTModelIn](../../models/updateftmodelin.md)           | :heavy_check_mark:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.FTModelOut](../../models/ftmodelout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_archive_fine_tuned_model

Archive a fine-tuned model.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.jobs_api_routes_fine_tuning_archive_fine_tuned_model(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to archive.                                     | ft:open-mistral-7b:587a6b29:20240514:7e773925                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ArchiveFTModelOut](../../models/archiveftmodelout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_unarchive_fine_tuned_model

Un-archive a fine-tuned model.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.models.jobs_api_routes_fine_tuning_unarchive_fine_tuned_model(model_id="ft:open-mistral-7b:587a6b29:20240514:7e773925")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `model_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The ID of the model to unarchive.                                   | ft:open-mistral-7b:587a6b29:20240514:7e773925                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.UnarchiveFTModelOut](../../models/unarchiveftmodelout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |