from models.users import User
from dependencies import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from schemas.users import UserOut, Userin


router = APIRouter()

@router.post("/users", response_model=UserOut)
def create_user(user: Userin, session: SessionDep):
    user_validate = User.model_validate(user)
    user_similar = session.exec(select(User).where(User.email==user.email)).first()
    if user_similar:
        raise HTTPException(status_code=400, detail="User with this email already exist.!")
    session.add(user_validate)
    session.commit()
    session.refresh(user_validate)
    return user_validate

@router.get("/users", response_model=list[UserOut])
def read_all_users(session: SessionDep) -> list[UserOut]:
    users = session.exec(select(User)).all()
    return users

@router.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int, session: SessionDep) -> UserOut:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found..! ")
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found..! ")
    session.delete(user)
    session.commit()
    return {"ok": True}