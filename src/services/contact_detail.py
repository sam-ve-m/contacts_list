from pymongo import MongoClient

from src.core.entities.contacts import Contact
from src.core.enum.status import Status
from src.repository.get_contact_details import GetContactDetailsContactsRepository


def display_contact_detail(_id: str, infrastructure: MongoClient) -> dict:
    contact_detail_repository = GetContactDetailsContactsRepository(infrastructure)
    try:
        contact_detail: Contact = contact_detail_repository.get(_id)
        contact_as_json = {
            "contactId": contact_detail.contactId,
            "firstName": contact_detail.name.firstName,
            "lastName": contact_detail.name.lastName,
            "email": contact_detail.email.email,
            "phoneList": [{
                "number": phone.number,
                "type": phone.type,
            } for phone in contact_detail.phoneList],
            str(Status.SUCCESS.name).lower(): Status.SUCCESS.value,
        }
        return contact_as_json
    except AttributeError:
        return {"status": Status.ERROR.value}

