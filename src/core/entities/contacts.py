from src.core.entities.address import Address
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import PhoneList


class Contact(PhoneList):
    contactId: str
    name: Name
    email: Email
    address: Address

