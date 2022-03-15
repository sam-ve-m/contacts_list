from src.core.entities.address import Address
from src.core.entities.contacts import Contact
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import Phone
from src.core.interfaces.repository.i_mongo_repository import IMongo
from src.repository.util.contact_id import create_id


class ContactsRepository(IMongo):
    DATABASE: str = "contact_list"
    COLLECTION: str = "contacts"

    @staticmethod
    def _transform_from_json_to_contact(contact_as_json: dict) -> Contact:
        contact = Contact(
            name=Name(
                lastName=contact_as_json.get("lastName"),
                firstName=contact_as_json.get("firstName"),
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
        return contact

    @staticmethod
    def _transform_from_contact_to_json(contact: Contact) -> dict:
        contact_as_json = {
            "_id": create_id(contact),
            "firstName": contact.name.firstName,
            "lastName": contact.name.lastName,
            "email": contact.email.email,
            "address": contact.address.full_address,
            "phones": [{
                "type": phone.type,
                "number": phone.number,
            } for phone in contact.phoneList],
        }
        return contact_as_json
