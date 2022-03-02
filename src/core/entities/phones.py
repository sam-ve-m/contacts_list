from pydantic import BaseModel


class Phone(BaseModel):
    number: int
    type: str
