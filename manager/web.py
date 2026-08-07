from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from core.docker_client import (
    get_gameservers,
    get_info,
    start,
    stop,
    restart,
)

app = FastAPI(title="HomeControl")

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


@app.post("/server/{name}/start")
def start_server(name: str):

    start(name)

    return RedirectResponse(
        url="/",
        status_code=303,
    )


@app.post("/server/{name}/stop")
def stop_server(name: str):

    stop(name)

    return RedirectResponse(
        url="/",
        status_code=303,
    )


@app.post("/server/{name}/restart")
def restart_server(name: str):

    restart(name)

    return RedirectResponse(
        url="/",
        status_code=303,
    )


@app.get("/server/{name}", response_class=HTMLResponse)
def server_row(request: Request, name: str):

    for container in get_gameservers():

        info = get_info(container)

        if info["name"] == name:

            return templates.TemplateResponse(
                request=request,
                name="partials/server_row.html",
                context={
                    "request": request,
                    "server": info,
                },
            )

    raise HTTPException(status_code=404)
