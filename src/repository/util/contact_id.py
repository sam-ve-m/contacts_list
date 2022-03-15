from hashlib import md5

from src.core.entities.contacts import Contact


def create_id(contact: Contact) -> str:
    _id = (
        f"{contact.name.firstName + contact.name.lastName}:"
        f"{contact.email.email}:"
        f"{contact.phoneList[0].number}"
    )
    return md5(_id.encode()).hexdigest()

