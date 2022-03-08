from fastapi import FastAPI

from src.routes.register import register_route

app = FastAPI()
app.include_router(register_route)
