from src.api.connection_manager import ConnectionManager
from src.tasks.async_task_interface import AsyncTaskInterface


class WebsocketTask(AsyncTaskInterface):
    def __init__(
        self,
        name: str,
        manager: ConnectionManager,
        sleep_period: float = 0.01,
        start: bool = True,
    ) -> None:
        super().__init__(name, sleep_period, start)
        self._manager = manager

    def _initialize(self) -> None:
        self._i = 0

    async def _update(self) -> None:
        print(self._i)
        await self._manager.send_message(f"{self._i}")
        self._i = self._i + 1
