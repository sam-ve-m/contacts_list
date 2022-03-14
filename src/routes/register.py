from fastapi import APIRouter

from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact():
    pass
