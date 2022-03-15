from pydantic import BaseModel


class Name(BaseModel):
    firstName: str
    lastName: str
