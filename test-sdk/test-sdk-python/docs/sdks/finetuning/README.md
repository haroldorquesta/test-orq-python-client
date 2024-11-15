# FineTuning
(*fine_tuning*)

## Overview

Fine-tuning API

### Available Operations

* [jobs_api_routes_fine_tuning_get_fine_tuning_jobs](#jobs_api_routes_fine_tuning_get_fine_tuning_jobs) - Get Fine Tuning Jobs
* [jobs_api_routes_fine_tuning_create_fine_tuning_job](#jobs_api_routes_fine_tuning_create_fine_tuning_job) - Create Fine Tuning Job
* [jobs_api_routes_fine_tuning_get_fine_tuning_job](#jobs_api_routes_fine_tuning_get_fine_tuning_job) - Get Fine Tuning Job
* [jobs_api_routes_fine_tuning_cancel_fine_tuning_job](#jobs_api_routes_fine_tuning_cancel_fine_tuning_job) - Cancel Fine Tuning Job
* [jobs_api_routes_fine_tuning_start_fine_tuning_job](#jobs_api_routes_fine_tuning_start_fine_tuning_job) - Start Fine Tuning Job

## jobs_api_routes_fine_tuning_get_fine_tuning_jobs

Get a list of fine-tuning jobs for your organization and user.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fine_tuning.jobs_api_routes_fine_tuning_get_fine_tuning_jobs()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                 | [models.JobsAPIRoutesFineTuningGetFineTuningJobsRequest](../../models/jobsapiroutesfinetuninggetfinetuningjobsrequest.md) | :heavy_check_mark:                                                                                                        | The request object to use for the request.                                                                                |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.JobsOut](../../models/jobsout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_create_fine_tuning_job

Create a new fine-tuning job, it will be queued for processing.

### Example Usage

```python
import os
import test_sdk
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fine_tuning.jobs_api_routes_fine_tuning_create_fine_tuning_job(job_in={
    "model": test_sdk.FineTuneableModel.CODESTRAL_LATEST,
    "hyperparameters": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                      | Type                                                                                                                                                                                                                                                                                                           | Required                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job_in`                                                                                                                                                                                                                                                                                                       | [models.JobIn](../../models/jobin.md)                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                             | N/A                                                                                                                                                                                                                                                                                                            |
| `dry_run`                                                                                                                                                                                                                                                                                                      | *OptionalNullable[bool]*                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                             | * If `true` the job is not spawned, instead the query returns a handful of useful metadata<br/>  for the user to perform sanity checks (see `LegacyJobMetadataOut` response).<br/>* Otherwise, the job is started and the query returns the job ID along with some of the<br/>  input parameters (see `JobOut` response).<br/> |
| `retries`                                                                                                                                                                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                            |

### Response

**[models.JobsAPIRoutesFineTuningCreateFineTuningJobResponse](../../models/jobsapiroutesfinetuningcreatefinetuningjobresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_get_fine_tuning_job

Get a fine-tuned job details by its UUID.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fine_tuning.jobs_api_routes_fine_tuning_get_fine_tuning_job(job_id="13975bcd-6f6a-41c0-b702-fbd352fae717")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The ID of the job to analyse.                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DetailedJobOut](../../models/detailedjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_cancel_fine_tuning_job

Request the cancellation of a fine tuning job.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fine_tuning.jobs_api_routes_fine_tuning_cancel_fine_tuning_job(job_id="dcd95cf1-cef5-4de0-a453-c739fc681dfc")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `job_id`                                                            | *str*                                                               | :heavy_check_mark:                                                  | The ID of the job to cancel.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DetailedJobOut](../../models/detailedjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## jobs_api_routes_fine_tuning_start_fine_tuning_job

Request the start of a validated fine tuning job.

### Example Usage

```python
import os
from test_sdk import TestSDK

s = TestSDK(
    api_key=os.getenv("TESTSDK_API_KEY", ""),
)

res = s.fine_tuning.jobs_api_routes_fine_tuning_start_fine_tuning_job(job_id="9481556b-8d5d-492b-b7a7-359108479216")

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

**[models.DetailedJobOut](../../models/detailedjobout.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |