from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    username: str = Field(index=True)
    email: str
    password : str
    age: int