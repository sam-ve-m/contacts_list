from pymongo import MongoClient

from src.core.enum.status import Status
from src.repository.contacts import ContactsRepository


def lists_contacts_in_mongo(infrastructure: MongoClient) -> dict:
    contacts_repository = ContactsRepository(infrastructure)
    try:
        list_of_contacts = contacts_repository.get_contacts_list()
    except:
        return {'ContactList': [], 'status': Status.ERROR.value}

    return {'ContactList': list_of_contacts, 'status': Status.SUCCESS.value}
