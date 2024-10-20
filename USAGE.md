<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from orq_python_client import Orq
import os

s = Orq(
    bearer=os.getenv("ORQ_BEARER", ""),
)

res = s.contacts.post_contacts(request={
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
from orq_python_client import Orq
import os

async def main():
    s = Orq(
        bearer=os.getenv("ORQ_BEARER", ""),
    )
    res = await s.contacts.post_contacts_async(request={
        "external_id": "<id>",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->