from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    age: int


class UserOut(UserBase):
    id: int

class UserIn(UserBase):
    password: str