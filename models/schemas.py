from pydantic import BaseModel

# What the user provides alongside their image
class OCRRequest(BaseModel):
    target_language: str

# What the server sends back after processing
class OCRResponse(BaseModel):
    extracted_text: str
    translated_text: str
    detected_language: str