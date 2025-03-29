from src.async_task_interface import AsyncTaskInterface


class AsyncTask(AsyncTaskInterface):
    def _initialize(self):
        print("Initialize AsyncTask")
        self._i = 0

    def _update(self) -> None:
        print(self._i)
        self._i = self._i + 1
