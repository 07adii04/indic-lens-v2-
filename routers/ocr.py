# Indic Lens V2 — Data Models
# I need a model for what the user sends us: an image file and a target language
# I need a model for what we send back: extracted text, translated text, detected language
from fastapi import APIRouter
from models.schemas import OCRRequest, OCRResponse

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "ocr"}

@router.post("/extract")
async def extract_text():
    return {"message": "OCR route working — real implementation coming soon"}