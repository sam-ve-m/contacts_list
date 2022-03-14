from src.core.entities.contacts import Contact
from src.core.interfaces.repository.i_mongo_repository import IMongo


class ContactsRepository(IMongo):
    DATABASE: str = "contact_list"
    COLLECTION: str = "contacts"

    def register_a_contact(self, contact: Contact) -> bool:
        contact_as_json = {
            "_id": self._create_id(contact),
            "name": contact.name.full_name,
            "email": contact.email.email,
            "phones": [{
                "type": phone.type,
                "number": phone.number,
            } for phone in contact.phoneList],
            "address": contact.address.full_address,
        }
        insert_status = self.insert_update_one(contact_as_json)
        return insert_status

    @staticmethod
    def _create_id(contact: Contact) -> str:
        _id = (
            f"{contact.name.full_name}:"
            f"{contact.email.email}:"
            f"{contact.phoneList[0].number}"
        )
        return _id
