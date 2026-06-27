# Indic Lens V2 — Data Models
# I need a model for what the user sends us: an image file and a target language
# I need a model for what we send back: extracted text, translated text, detected language
from fastapi import APIRouter, UploadFile, File
from models.schemas import OCRResponse
from services.vision import extract_text_from_image

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "ocr"}

@router.post("/extract", response_model=OCRResponse)
async def extract_text(file: UploadFile = File(...), target_language: str = "english"):
    image_bytes = await file.read()
    result = extract_text_from_image(image_bytes)
    return OCRResponse(
        extracted_text=result["extracted_text"],
        detected_language=result["detected_language"],
        translated_text="translation coming soon"
    )