from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.repository.register_a_contact import RegisterContactsRepository


def register_contact(
        contact_parameters: Contact,
        mongo_infrastructure: MongoClient,
) -> dict:
    return _register_contact_in_mongo(contact_parameters, mongo_infrastructure)


def _register_contact_in_mongo(contact: Contact, infrastructure: MongoClient):
    contacts_repository = RegisterContactsRepository(infrastructure)
    register_status = contacts_repository.register(contact)
    status_alias = {
        True: Status.SUCCESS.value,
        False: Status.ERROR.value
    }
    return_status = status_alias.get(register_status)
    register_return = {"status": return_status}
    return register_return
