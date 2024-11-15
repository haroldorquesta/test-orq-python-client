# Batch
(*batch*)

## Overview

Batch API

### Available Operations

* [jobs_api_routes_batch_get_batch_jobs](#jobs_api_routes_batch_get_batch_jobs) - Get Batch Jobs
* [jobs_api_routes_batch_create_batch_job](#jobs_api_routes_batch_create_batch_job) - Create Batch Job
* [jobs_api_routes_batch_get_batch_job](#jobs_api_routes_batch_get_batch_job) - Get Batch Job
* [jobs_api_routes_batch_cancel_batch_job](#jobs_api_routes_batch_cancel_batch_job) - Cancel Batch Job

## jobs_api_routes_batch_get_batch_jobs

Get a list of batch jobs for your organization and user.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.batch.jobs_api_routes_batch_get_batch_jobs()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.JobsAPIRoutesBatchGetBatchJobsRequest](../../models/jobsapiroutesbatchgetbatchjobsrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.BatchJobsOut](../../models/batchjobsout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_batch_create_batch_job

Create a new batch job, it will be queued for processing.

### Example Usage

```python
import os
import test_sdk
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.batch.jobs_api_routes_batch_create_batch_job(request={
    "input_files": [
        "d1d4e83f-bb6a-4154-9e25-a41080d645f8",
        "43e2208f-5620-434a-9dd9-d8c5b82c0306",
        "92ce266a-adb5-41ed-b4f3-4410cf74e975",
    ],
    "endpoint": test_sdk.APIEndpoint.ROOT_V1_MODERATIONS,
    "model": "LeBaron",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.BatchJobIn](../../models/batchjobin.md)                     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_batch_get_batch_job

Get a batch job details by its UUID.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.batch.jobs_api_routes_batch_get_batch_job(job_id="41a64b8b-8a35-4a35-9b8b-1158ce78c603")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_batch_cancel_batch_job

Request the cancellation of a batch job.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.batch.jobs_api_routes_batch_cancel_batch_job(job_id="3e7f4d33-06f6-4155-afae-18ac30f578a8")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BatchJobOut](../../models/batchjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |