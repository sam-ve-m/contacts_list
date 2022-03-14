from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.repository.contacts import ContactsRepository
from src.core.enum.status import Status


def display_contact_detail(_id: Contact, infrastructure: MongoClient) -> dict:
    contact_detail_repository = ContactsRepository(infrastructure)
    contact_detail = contact_detail_repository.find_one(_id)
    status_alias = {
        Status.SUCCESS.name: Status.SUCCESS.value
    }
    contact_detail.update(status_alias)
    return contact_detail
