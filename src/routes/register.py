from fastapi import APIRouter

from src.core.entities.contacts import Contact
from src.infrastructure.mongo import MongoDBInfrastructure
from src.services.lists_registers import lists_contacts_in_mongo
from src.services.register import register_contact_in_mongo
from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact(contact: Contact):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    register_return = register_contact_in_mongo(contact, mongo_connection)
    return register_return


@route.get("/contacts")
def lists_contacts():
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    return_list = lists_contacts_in_mongo(mongo_connection)
    return return_list
