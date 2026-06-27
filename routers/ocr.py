from fastapi import APIRouter, UploadFile, File
from models.schemas import OCRResponse
from services.vision import extract_text_from_image, translate_text

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "ocr"}

@router.post("/extract", response_model=OCRResponse)
async def extract_text(file: UploadFile = File(...), target_language: str = "hi"):
    image_bytes = await file.read()
    result = extract_text_from_image(image_bytes)
    translated = translate_text(result["extracted_text"], target_language)
    
    return OCRResponse(
        extracted_text=result["extracted_text"],
        detected_language=result["detected_language"],
        translated_text=translated
    )
