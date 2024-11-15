<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from test_sdk import TestSDK

async def main():
    s = TestSDK(
        api_key=os.getenv("TESTSDK_API_KEY", ""),
    )
    res = await s.models.list_models_v1_models_get_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->