from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.repository.contacts import ContactsRepository


def register_contact_in_mongo(contact: Contact, infrastructure: MongoClient) -> dict:
    contacts_repository = ContactsRepository(infrastructure)
    register_status = contacts_repository.register_a_contact(contact)
    status_alias = {
        True: Status.SUCCESS.value,
        False: Status.ERROR.value
    }
    return_status = status_alias.get(register_status)
    register_return = {"status": return_status}
    return register_return

