from typing import List

from pydantic import BaseModel, validator

from src.core.entities.phones import Phone, assert_have_max_of_3


class ContactRegisterParameters(BaseModel):
    email: str
    address: str
    lastName: str
    firstName: str
    phoneList: List[Phone]

    _max_3_phones = validator('phoneList', allow_reuse=True)(assert_have_max_of_3)
