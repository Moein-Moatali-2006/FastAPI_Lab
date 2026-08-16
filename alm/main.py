from fastapi import FastAPI
from database import SessionDep
from models import User


app = FastAPI()



@app.post("/user")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

