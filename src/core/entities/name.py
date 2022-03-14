from pydantic import BaseModel


class Name(BaseModel):
    full_name: str
