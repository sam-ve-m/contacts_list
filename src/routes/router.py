from fastapi import APIRouter

from src.core.entities.contacts_parameters import ContactParameters
from src.infrastructure.mongo import MongoDBInfrastructure
from src.services.contact_detail import display_contact_detail
from src.services.lists_registers import lists_contacts_in_mongo
from src.services.register import register_contact
from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact_route(contact: ContactParameters):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    register_return = register_contact(contact, mongo_connection)
    return register_return


@route.get("/contacts")
def lists_contacts():
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    contacts_list = lists_contacts_in_mongo(mongo_connection)
    return contacts_list


@route.get("/contact/{_id}")
def contact_detail(_id: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    contact_details = display_contact_detail(_id, mongo_connection)
    return contact_details
