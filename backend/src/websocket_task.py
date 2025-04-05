from src.async_task_interface import AsyncTaskInterface
from src.connection_manager import ConnectionManager


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
        await self._manager.send_message(f"Message {self._i}")
        self._i = self._i + 1
