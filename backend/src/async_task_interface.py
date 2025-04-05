import asyncio


class AsyncTaskInterface:
    def __init__(
        self, name: str, sleep_period: float = 0.01, start: bool = False
    ) -> None:
        self.name = name
        self._task: asyncio.Task[None] | None = None
        self._sleep_period = sleep_period
        self._initialize()
        if start:
            self.start()

    def start(self) -> None:
        if not self._is_running():
            self._task = asyncio.create_task(self._run())

    async def stop(self) -> None:
        await self._cancel()
        self._initialize()

    async def pause(self) -> None:
        await self._cancel()

    async def restart(self) -> None:
        await self.stop()
        self.start()

    async def _cancel(self) -> None:
        if self._is_running():
            assert self._task is not None  # for mypy
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                print("Task cancelled.")
        self._task = None

    async def _run(self) -> None:
        while True:
            self._update()
            await asyncio.sleep(self._sleep_period)

    def _is_running(self) -> bool:
        return self._task is not None and not self._task.done()

    def _initialize(self) -> None:
        pass

    def _update(self) -> None:
        pass
