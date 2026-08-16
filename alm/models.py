from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(index=True)
    email: str
    password : str
    age: int