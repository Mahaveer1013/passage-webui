from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

from utils import walk_directory, passage_execute, passage_exitstatus, search_directory

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets",html = True), name="assets")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_index(request: Request):
    directory = "/home/goldayan/.passage/store"
    file_data = walk_directory(directory)
    return templates.TemplateResponse(
        request=request, name="base.html", context={"file_data":file_data}
    )

#    return FileResponse('assets/index.html')

@app.get("/new")
async def read_index():
    return FileResponse('assets/new-password.html')

@app.get("/user")
async def read_index():
    return FileResponse('assets/user.html')

@app.get("/passshow", response_class=HTMLResponse)
async def root(request: Request,folder_name: str, file_name: str, folder_id: str, file_id: str):
    pass_path=folder_name.replace(" > ", "/")+"/"+file_name
    password = passage_execute(["passage",pass_path])
    return templates.TemplateResponse(
        request=request,
        name="password-show.html",
        context={"folder_name":folder_name, "file_name": file_name, "folder_id": folder_id, "file_id": file_id, "password": password}
    )

@app.get("/passhide", response_class=HTMLResponse)
async def root(request: Request,folder_name: str, file_name: str, folder_id: str, file_id: str):
    return templates.TemplateResponse(
        request=request,
        name="password-show.html",
        context={"folder_name":folder_name, "file_name": file_name, "folder_id": folder_id, "file_id": file_id}
    )

@app.get("/delete")
async def read_index(request: Request,folder_name: str, file_name: str, folder_id: str, file_id: str):
    pass_path=folder_name.replace(" > ", "/")+"/"+file_name
    password = passage_exitstatus(["passage","rm","-f",pass_path]) # force password delete
    directory = "/home/goldayan/.passage/store"
    file_data = walk_directory(directory)
    return templates.TemplateResponse(
        request=request, name="password-table.html", context={"file_data":file_data}
    )

@app.get("/search")
async def read_index(request: Request,search: str):
    directory = "/home/goldayan/.passage/store"
    file_data = search_directory(directory, search)
    return templates.TemplateResponse(
        request=request, name="password-table.html", context={"file_data":file_data}
    )

