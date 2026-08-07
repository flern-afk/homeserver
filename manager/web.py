from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from core.docker_client import get_gameservers, get_info

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):

    servers = [
        get_info(server)
        for server in get_gameservers()
    ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "servers": servers,
        },
    )
