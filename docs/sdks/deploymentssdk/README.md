# DeploymentsSDK
(*deployments*)

## Overview

### Available Operations

* [get_config](#get_config) - Get config
* [invoke](#invoke) - Invoke
* [add_metrics](#add_metrics) - Add metrics
* [list](#list) - List all deployments

## get_config

Retrieve the deployment configuration

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.deployments.get_config(request={
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

## invoke

Invoke a deployment with a given payload

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.deployments.invoke(request={
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

## add_metrics

Add metrics to a deployment

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.deployments.add_metrics(id="<id>", request_body={})

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

## list

Returns a list of your deployments. The deployments are returned sorted by creation date, with the most recent deployments appearing first.

### Example Usage

```python
from orq_poc_python_client import Orq
import os

s = Orq(
    api_key=os.getenv("ORQ_API_KEY", ""),
)

res = s.deployments.list()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                                                                                                         | Required                                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`                                                                                                                                                                                                                                                                                                                                      | *Optional[float]*                                                                                                                                                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                           | A limit on the number of objects to be returned. Limit can range between 1 and 50, and the default is 10                                                                                                                                                                                                                                     |
| `after`                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                           | A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 20 objects, ending with `ed33dade-ae32-4959-8c5c-7ae4aad748b5`, your subsequent call can include `after=ed33dade-ae32-4959-8c5c-7ae4aad748b5` in order to fetch the next page of the list. |
| `retries`                                                                                                                                                                                                                                                                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                           | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                          |

### Response

**[models.GetV2DeploymentsResponseBody](../../models/getv2deploymentsresponsebody.md)**

### Errors

| Error Type          | Status Code         | Content Type        |
| ------------------- | ------------------- | ------------------- |
| models.HonoAPIError | 500                 | application/json    |
| models.SDKError     | 4XX, 5XX            | \*/\*               |