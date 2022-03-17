from typing import Optional, List

from pydantic import validator, BaseModel

from src.core.entities.phones import Phone, assert_have_max_of_3


class ContactParameters(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    phoneList: Optional[List[Phone]] = None

    _max_3_phones = validator('phoneList', allow_reuse=True)(assert_have_max_of_3)
