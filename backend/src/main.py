import asyncio
import signal
from types import FrameType
from typing import Optional

from src.async_task import AsyncTask

task: Optional[AsyncTask] = None


def signal_handler(sig: int, frame: Optional[FrameType]) -> None:
    print("You pressed Ctrl+C!")


async def main() -> None:
    task = AsyncTask()
    task.start()

    signal.signal(signal.SIGINT, signal_handler)
    print("Press Ctrl+C")
    signal.pause()
    await task.stop()
    print("Exiting...")


async def updating_task() -> None:
    while True:
        await asyncio.sleep(2)
        print("hello")


async def input_handler() -> None:
    while True:
        user_input = await asyncio.to_thread(input, "Type 'x' to stop: ")
        if user_input.strip().lower() == "x":
            print("Stopping...")
            break


if __name__ == "__main__":
    asyncio.run(main())
