from pydantic import BaseModel


class User(BaseModel):
    id: int
    firstname: str
    lastname: str

    class Create(BaseModel):
        firstname: str
        lastname: str
