import asyncio


class Event:
    def __init__(self):
        self.coroutine_queue = []
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.ioloop = asyncio.get_event_loop()

    def __del__(self):
        self.ioloop.close()

    def subscribe(self, coroutine):
        self.coroutine_queue.append(coroutine)

    def unsubscribe(self, function):
        self.coroutine_queue.remove(function)

    def on_event(self, *args):
        tasks = []
        for crt in self.coroutine_queue:
            tasks.append(self.ioloop.create_task(crt(*args)))
        wait_tasks = asyncio.wait(tasks)
        self.ioloop.run_until_complete(wait_tasks)
