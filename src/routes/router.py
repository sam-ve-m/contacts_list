from fastapi import APIRouter

from src.core.entities.contacts_parameters import ContactParameters
from src.core.interfaces.services.i_detail import IDetail
from src.core.interfaces.services.i_list import IList
from src.core.interfaces.services.i_register import IRegister
from src.core.interfaces.services.i_update import IUpdate
from src.infrastructure.mongo import MongoDBInfrastructure
from src.infrastructure.redis import RedisKeyDBInfrastructure
from src.services.contact_detail import ContactDetail
from src.services.lists_registers import ListsContacts
from src.services.register import RegisterContact
from src.services.update_contact import UpdateContact
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
    list_contact_service: IList = ListsContacts(mongo_connection)
    contacts_list = list_contact_service.get_list()
    return contacts_list


@route.get("/contact/{_id}")
def contact_detail(_id: str):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    get_contact_detail_service: IDetail = ContactDetail(mongo_connection)
    contact_details = get_contact_detail_service.get_detail(_id)
    return contact_details


@route.post("/edit/{_id}")
def contact_detail(_id: str, updates: ContactParameters):
    mongo_connection = MongoDBInfrastructure.get_singleton_connection()
    get_contact_detail_service: IUpdate = UpdateContact(mongo_connection)
    contact_details = get_contact_detail_service.update(_id, updates)
    return contact_details
