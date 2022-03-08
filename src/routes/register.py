from fastapi import APIRouter
from src.services.utils.env_config import config

register_route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@register_route.get("/register")
def register_contact():
    pass
