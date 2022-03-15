from pymongo import MongoClient

from src.core.enum.status import Status
from src.repository.contacts import ContactsRepository


def lists_contacts_in_mongo(infrastructure: MongoClient) -> dict:
    contacts_repository = ContactsRepository(infrastructure)
    list_of_contacts = contacts_repository.get_contacts_list()
    list_of_contacts_return = [_contact_dict_to_json(dicti) for dicti in list_of_contacts]
    return {'ContactList': list_of_contacts_return, 'status': Status.SUCCESS.value}


def _contact_dict_to_json(dictionary: dict):
    contact_in_dict = dictionary.get('Contact')
    contact = {
        "contactId": dictionary.get('_id'),
        "firstName": contact_in_dict.contact.name,
        "email": contact_in_dict.contact.email,
        "phoneList": contact_in_dict.contact.phoneList
    }
    return contact
