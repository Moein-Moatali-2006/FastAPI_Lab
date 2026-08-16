from fastapi import FastAPI, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated


app = FastAPI()

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(index=True)
    email: str
    password : str

sql_file_name = "mydb.sqlite"
sqlite_url = f"sqlite:///{sql_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/user")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
