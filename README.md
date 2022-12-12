# Custom Structures
Repository with useful structures

custom_event.Event - Class to conveniently store all coroutines that should be executed after some repetitive event

#Usage example:

```python
import custom_structures.custom_event as ce
import asyncio


async def print_coroutine0(x1, x2):
    await asyncio.sleep(1)
    for i in range(x1, x2):
        print(f'Hi, {i}')


async def print_coroutine1(x1, x2):
    for i in range(x1, x2):
        print(f'Hello, {i}')


class MyClass(object):
    def __init__(self):
        self.on_data = ce.Event()

    def worker_generated_something_to_pass(self):
        for i in range(0, 10):
            self.on_data.on_event(i*10, 10*(i+1))


worker = MyClass()
worker.on_data.subscribe(print_coroutine0)
worker.on_data.subscribe(print_coroutine1)
worker.worker_generated_something_to_pass()
worker.on_data.unsubscribe(print_coroutine0)
worker.on_data.unsubscribe(print_coroutine1)
```
