from fastapi import FastAPI
from routers import ocr

app = FastAPI(title="Indic Lens V2")

app.include_router(ocr.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Indic Lens V2 — check /docs"}