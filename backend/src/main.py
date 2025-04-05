import uvicorn


def add(a: int, b: int) -> int:
    return a + b


def main() -> None:
    uvicorn.run("src.api.api:app", host="127.0.0.1", port=8000, reload=True, workers=2)


if __name__ == "__main__":
    main()
