from typing import List, Dict, Type
from hashlib import md5
from src.core.entities.address import Address
from src.core.entities.contacts import Contact
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import Phone
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

        return md5(_id.encode()).hexdigest()


    def get_contacts_list(self) -> List[Dict[str, Type[Contact]]]:
        list_of_contacts = self.find_all()
        list_of_contacts_return = []
        for contact_as_json in list_of_contacts:
            contact = Contact(
                name=Name(
                    full_name=contact_as_json.get('name')
                ),
                email=Email(
                    email=contact_as_json.get('email')
                ),
                phoneList=[Phone(
                    type=phone.get('type'),
                    number=phone.get('number')
                ) for phone in contact_as_json.get('phones')],
                address=Address(
                    full_address=contact_as_json.get('address')
                )
            )
            list_of_contacts_return.append({'_id': contact_as_json.get('_id'), 'Contact': contact})

        return list_of_contacts_return
