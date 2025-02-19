from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory="assets",html = True), name="assets")

@app.get("/api")
async def root():
    return {"message": "Hello World"}
