from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Person(BaseModel):
    name: str
    age: int 
    height: int| None = 0


@app.post("/home")
def root(prs: Person):
    return prs
