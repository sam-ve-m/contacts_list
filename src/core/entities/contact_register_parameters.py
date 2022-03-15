from typing import List

from pydantic import BaseModel

from src.core.entities.phones import Phone


class ContactRegisterParameters(BaseModel):
    email: str
    address: str
    lastName: str
    firstName: str
    phoneList: List[Phone]
