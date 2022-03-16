from typing import List

from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.repository.get_contact_list import GetContactListContactsRepository


def lists_contacts_in_mongo(infrastructure: MongoClient) -> dict:
    contacts_repository = GetContactListContactsRepository(infrastructure)
    list_of_contacts: List[Contact] = contacts_repository.get()
    list_of_contacts_return = [{
        "contactId": contact.contactId,
        "firstName": contact.name.firstName,
        "lastName": contact.name.lastName,
        "email": contact.email,
        "phoneList": [{
            "number": phone.number,
            "type": phone.type,
        } for phone in contact.phoneList]
    } for contact in list_of_contacts]
    return {'ContactList': list_of_contacts_return, 'status': Status.SUCCESS.value}
