# DeploymentsSDK
(*deployments*)

## Overview

### Available Operations

* [post_v2_deployments_get_config](#post_v2_deployments_get_config) - Get config
* [post_v2_deployments_invoke](#post_v2_deployments_invoke) - Invoke
* [post_v2_deployments_id_metrics](#post_v2_deployments_id_metrics) - Add metrics

## post_v2_deployments_get_config

Retrieve the deployment configuration

### Example Usage

```python
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.deployments.post_v2_deployments_get_config(request={
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

res = s.deployments.post_v2_deployments_invoke(request={
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

res = s.deployments.post_v2_deployments_id_metrics(id="<id>", request_body={})

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