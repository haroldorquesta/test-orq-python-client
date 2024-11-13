<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_poc_python_client import Orq
import os

s = Orq(
    open_ai=os.getenv("ORQ_OPEN_AI", ""),
)

res = s.contacts.create(request={
    "external_id": "<id>",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from orq_poc_python_client import Orq
import os

async def main():
    s = Orq(
        open_ai=os.getenv("ORQ_OPEN_AI", ""),
    )
    res = await s.contacts.create_async(request={
        "external_id": "<id>",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->