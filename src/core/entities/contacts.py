from typing import List
from pydantic import BaseModel
from src.core.entities.phones import Phone
from src.core.entities.address import Address


class Contact(BaseModel):
    contactId: str
    firstName: str
    lastName: str
    email: str
    address: Address
    phoneList: List[Phone]
