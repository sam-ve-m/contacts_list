from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.repository.get_contact_list import GetContactListContactsRepository


def lists_contacts_in_mongo(infrastructure: MongoClient) -> dict:
    contacts_repository = GetContactListContactsRepository(infrastructure)
    list_of_contacts = contacts_repository.get()
    list_of_contacts_return = [_contact_dict_to_json(dicti) for dicti in list_of_contacts]
    return {'ContactList': list_of_contacts_return, 'status': Status.SUCCESS.value}


def _contact_dict_to_json(dictionary: dict):
    contact_in_dict: Contact = dictionary.get('Contact')
    contact = {
        "contactId": dictionary.get('_id'),
        "firstName": contact_in_dict.name,
        "email": contact_in_dict.email,
        "phoneList": contact_in_dict.phoneList
    }
    return contact
