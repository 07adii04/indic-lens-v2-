# This service takes image bytes as input
# sends them to Google Vision API
# and returns the extracted text and detected language
import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

def extract_text_from_image(image_bytes: bytes) -> dict:
    # step 1 — get API key from environment
    api_key = os.getenv("GOOGLE_VISION_API_KEY")
    
    # step 2 — convert image bytes to base64
    # hint: base64.b64encode(image_bytes).decode("utf-8")
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    # step 3 — build the request body Google expects
    # Google wants: {"requests": [{"image": {"content": base64_image}, "features": [{"type": "TEXT_DETECTION"}]}]}
    request_body = {
        "requests": [
            {
                "image": {
                    "content": base64_image
                },
                "features": [
                    {
                        "type": "TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    # step 4 — send POST request to Google Vision API
    # URL: f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
    response = requests.post(url, json=request_body)

    # step 5 — extract text and language from response
    response_data = response.json()
    # ✅ correct order
    if "fullTextAnnotation" not in response_data["responses"][0]:
        return {"extracted_text": "", "detected_language": "unknown"}

    extracted_text = response_data["responses"][0]["fullTextAnnotation"]["text"]
    detected_language = response_data["responses"][0]["textAnnotations"][0]["locale"]
    return {"extracted_text": extracted_text, "detected_language": detected_language}
# This function takes extracted text and a target language
# sends it to Google Translate API
# and returns the translated text
def translate_text(text: str, target_language: str) -> str:
    api_key = os.getenv("GOOGLE_VISION_API_KEY")
    url = f"https://translation.googleapis.com/language/translate/v2?key={api_key}"
    
    request_body = {
        "q": text,
        "target": target_language
    }
    
    response = requests.post(url, json=request_body)
    response_data = response.json()    
    translated_text = response_data["data"]["translations"][0]["translatedText"]
    return translated_text