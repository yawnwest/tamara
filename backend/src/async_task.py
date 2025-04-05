from src.async_task_interface import AsyncTaskInterface


class AsyncTask(AsyncTaskInterface):
    def __init__(
        self, name: str, sleep_period: float = 0.01, start: bool = True
    ) -> None:
        super().__init__(name, sleep_period, start)

    def _initialize(self) -> None:
        self._i = 0

    def _update(self) -> None:
        print(self._i)
        self._i = self._i + 1
