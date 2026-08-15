from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI()

class Person(BaseModel):
    name: str
    age: int = Path(description="user age between 0 and 100", ge=0, le=100)
    height: int| None = 0


@app.post("/home")
def root(prs: Person, car:str=Query(default="Nothing", min_length=2, max_length=20)):
    return prs, car
