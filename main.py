from fastapi import FastAPI

from src.routes.register import route
import uvicorn

app = FastAPI()
app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=5556,
    )
