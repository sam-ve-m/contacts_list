from typing import List
from pydantic import BaseModel

from src.core.entities.email import Email
from src.core.entities.name import Name
from src.core.entities.phones import Phone
from src.core.entities.address import Address


class Contact(BaseModel):
    name: Name
    email: Email
    address: Address
    phoneList: List[Phone]
