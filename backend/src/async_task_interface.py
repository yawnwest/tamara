import asyncio


class AsyncTaskInterface:
    def __init__(self, sleepPeriod: float = 0.000000001) -> None:
        print("Initializing AsyncTask")
        self._task: asyncio.Task[None] = None
        self._sleepPeriod = sleepPeriod
        self._initialize()

    def start(self) -> None:
        if self._task is None or self._task.done():
            print("Start AsyncTask")
            self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        if self._task is not None and not self._task.done():
            print("Stop AsyncTask")
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                print("Task cancelled.")
            self._task = None

    async def restart(self) -> None:
        if self._task is not None and not self._task.done():
            print("Restart AsyncTask")
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                print("Task cancelled.")
        self._initialize()
        self.start()

    async def _run(self) -> None:
        while True:
            await asyncio.sleep(self._sleepPeriod)
            self._update()

    def _initialize(self):
        pass

    def _update(self) -> None:
        pass
