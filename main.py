from fastapi import FastAPI
from routers import ocr
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI(title="Indic Lens V2")

app.include_router(ocr.router, prefix="/api/v1")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html") as f:
        return f.read()
