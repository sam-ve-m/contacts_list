from fastapi import APIRouter

from src.core.entities.contacts_parameters import ContactParameters
from src.core.interfaces.services.i_register import IRegister
from src.infrastructure.mongo import MongoDBInfrastructure
from src.infrastructure.redis import RedisKeyDBInfrastructure
from src.services.contact_detail import display_contact_detail
from src.services.lists_registers import lists_contacts_in_mongo
from src.services.register import RegisterContact
from src.services.utils.env_config import config

route = APIRouter(prefix=config("ROUTERS_PREFIX"))


@route.post("/register")
def register_contact_route(contact: ContactParameters):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    redis_connection = RedisKeyDBInfrastructure.get_singleton_connection()
    register_service: IRegister = RegisterContact(mongo_connection, redis_connection)
    register_return = register_service.register(contact)
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
