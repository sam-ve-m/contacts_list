from typing import List, Optional

from pydantic import BaseModel, validator

from src.core.entities.address import Address
from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import PhoneList, Phone, assert_have_max_of_3


class ContactParameters(BaseModel):
    email: Optional[str]
    address: Optional[str]
    lastName: Optional[str]
    firstName: Optional[str]
    phoneList: Optional[List[Phone]]

    _max_3_phones = validator('phoneList', allow_reuse=True)(assert_have_max_of_3)


class Contact(PhoneList):
    contactId: str
    name: Name
    email: Email
    address: Address

