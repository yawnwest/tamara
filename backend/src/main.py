import asyncio
import tkinter as tk

from src.async_task import AsyncTask

task: AsyncTask | None = None


async def main() -> None:
    root = tk.Tk()
    root.title("Simple UI")

    button1 = tk.Button(
        root, text="Start Task", command=lambda: asyncio.create_task(start())
    )
    button1.pack(pady=10)

    button2 = tk.Button(
        root, text="Stop Task", command=lambda: asyncio.create_task(stop())
    )
    button2.pack(pady=10)

    button3 = tk.Button(
        root, text="Pause Task", command=lambda: asyncio.create_task(pause())
    )
    button3.pack(pady=10)

    button4 = tk.Button(
        root, text="Restart Task", command=lambda: asyncio.create_task(restart())
    )
    button4.pack(pady=10)

    await run_tkinter_with_asyncio(root)


async def start() -> None:
    global task
    if task is None:
        task = AsyncTask("my_task", 1, True)
    else:
        task.start()


async def stop() -> None:
    global task
    if task is None:
        return

    await task.stop()
    task = None


async def pause() -> None:
    global task
    if task is None:
        return

    await task.pause()


async def restart() -> None:
    global task
    if task is None:
        return

    await task.restart()


async def run_tkinter_with_asyncio(root: tk.Tk) -> None:
    while True:
        root.update()
        await asyncio.sleep(0.01)


if __name__ == "__main__":
    asyncio.run(main())
