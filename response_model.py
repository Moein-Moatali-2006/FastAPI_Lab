from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel


app = FastAPI()

class UserIn(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str

@app.post("/home", response_model=UserOut, status_code=status.HTTP_200_OK)
def root(user: UserIn):
    if user.username == "admin":
        raise HTTPException(detail="username cannt be admin",
                            status_code=status.HTTP_400_BAD_REQUEST,
                            headers={"X-Error": "This is my Error"})
    return user
