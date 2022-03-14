from fastapi import FastAPI

from src.routes.register import route

app = FastAPI()
app.include_router(route)
