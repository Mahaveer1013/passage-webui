from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets",html = True), name="assets")

@app.get("/")
async def read_index():
    return FileResponse('assets/index.html')

def generate_html_response():
    html_content = """
            <h1>Look ma! HTML!</h1>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/sample", response_class=HTMLResponse)
async def root():
    return generate_html_response()

