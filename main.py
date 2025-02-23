from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
import os

from pydantic import BaseModel

from utils import walk_directory, passage_execute, passage_exitstatus, search_directory, passage_new

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets",html = True), name="assets")

templates = Jinja2Templates(directory="templates")

def getStorePath():
    return os.path.join(os.environ.get("HOME"), ".passage", "store")

@app.get("/")
async def read_index(request: Request):
    directory = getStorePath()  # Construct the full path
    # directory = "/home/ubuntu/.passage/store"
    file_data = walk_directory(directory)
    return templates.TemplateResponse(
        request=request, name="base.html", context={"file_data":file_data}
    )

#    return FileResponse('assets/index.html')

@app.get("/new")
async def read_index():
    return FileResponse('assets/new-password.html')

@app.get("/settings")
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
    directory = getStorePath()
    file_data = walk_directory(directory)
    return templates.TemplateResponse(
        request=request, name="password-table.html", context={"file_data":file_data}
    )

@app.get("/search")
async def search_items(request: Request,search: str):
    directory = getStorePath()
    file_data = search_directory(directory, search)
    return templates.TemplateResponse(
        request=request, name="password-table.html", context={"file_data":file_data}
    )


@app.post("/new_password")
async def search_items(request: Request,path: str = Form(...),username: str = Form(...), password: str = Form(...), notes: str = Form(...)):
    if path and username and password:
        newpath = path+"/"+username
        passage_new(password, newpath)
        return HTMLResponse(content=f"<div>Password saved for, {newpath}</div>", status_code=200)
    else:
        return HTMLResponse(content="<div>Missing username or password</div>", status_code=400)  # 400 Bad Request

