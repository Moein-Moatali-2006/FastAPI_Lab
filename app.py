from fastapi import FastAPI

app = FastAPI()

# @app.get("/home/{name}/{age}")
# def root(name:str, age:int):
#     return {"Message": f"{name} is {age} years old."}


@app.get("/home/{name}")
def root(name:str, age:int=0):
    return {"Message": f"{name} is {age} years old."}