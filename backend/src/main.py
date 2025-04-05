import uvicorn
from fastapi import FastAPI

from src.async_task import AsyncTask

app = FastAPI()
task: AsyncTask | None = None


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/start")
async def start():
    global task
    if task is None:
        task = AsyncTask("my_task", 1, True)
    else:
        task.start()
    return "start"


@app.post("/stop")
async def stop():
    global task
    if task is None:
        return None

    await task.stop()
    task = None
    return "stop"


@app.post("/pause")
async def pause() -> None:
    global task
    if task is None:
        return

    await task.pause()


@app.post("/restart")
async def restart() -> None:
    global task
    if task is None:
        return

    await task.restart()


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True, workers=2)
