from pymongo import MongoClient

from src.core.enum.status import Status
from src.core.entities.contacts import Contact
from src.core.entities.contacts_parameters import ContactParameters
from src.repository.register_a_contact import RegisterContactsRepository
from src.services.utils.transform_parameters_to_contact import transform_parameters_to_contact


def register_contact(
        contact_parameters: ContactParameters,
        mongo_infrastructure: MongoClient,
) -> dict:
    contact = transform_parameters_to_contact(contact_parameters)
    return _register_contact_in_mongo(contact, mongo_infrastructure)


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
