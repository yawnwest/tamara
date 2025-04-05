from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from src.api.connection_manager import ConnectionManager
from src.tasks.websocket_task import WebsocketTask

app = FastAPI()
manager = ConnectionManager()
task: WebsocketTask | None = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Replace with your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.post("/start")
async def start() -> str:
    global task, manager
    if task is None:
        task = WebsocketTask("my_task", manager, 1, True)
    else:
        task.start()
    return "start"


@app.post("/stop")
async def stop() -> str | None:
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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await manager.connect(websocket)
    while True:
        try:
            data = await websocket.receive_text()
            await manager.send_message(data)
        except Exception as e:
            print(e)
            break
    manager.disconnect(websocket)
