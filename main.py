from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
tmpl = Jinja2Templates(directory="templates")

@app.get("/home/{username}", response_class=HTMLResponse)
def root(request: Request, username: str):
    print("="*90)
    print(list(request))
    print("="*90)
    return tmpl.TemplateResponse(request=request, name="home.html", context={"username": username})
