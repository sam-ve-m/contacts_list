from pydantic import BaseModel
from typing import List

from src.core.entities.phones import Phone


class ContactParameters(BaseModel):
    firstName: str
    lastName: str
    email: str
    address: str
    phoneList: List[Phone]
