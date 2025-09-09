from pydantic import BaseModel


class User(BaseModel):
    id: int
    fistname: str
    lastname: str

    class Create(BaseModel):
        fistname: str
        lastname: str
