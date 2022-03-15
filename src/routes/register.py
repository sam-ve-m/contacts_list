from fastapi import APIRouter

from src.core.entities.contacts import Contact
from src.infrastructure.mongo import MongoDBInfrastructure
from src.services.contact_detail import display_contact_detail
from src.services.register import register_contact_in_mongo
from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact(contact: Contact):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    register_return = register_contact_in_mongo(contact, mongo_connection)
    return register_return


@route.get("/contact/{_id}")
def contact_detail(_id: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    register_return = display_contact_detail(_id, mongo_connection)
    return register_return
