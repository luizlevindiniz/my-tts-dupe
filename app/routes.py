from fastapi import APIRouter, HTTPException, Request
from app.kokoro import Kokoro
from app.models.TTSRequest import TTSRequest
from typing import Any, Tuple

router = APIRouter()

try:
    kokoro = Kokoro()
    if not kokoro.is_ready():
        print("!!! [APIRouter] Kokoro model failed to load at startup. /tts endpoint will fail.")
except Exception as e:
    print(f"!!! [APIRouter] Critical error initializing Kokoro: {e}")
    kokoro = None

@router.post("/tts")
async def tts(request_data: TTSRequest) -> dict[str, Any]:

    if not kokoro.is_ready():
        raise HTTPException(status_code=500, detail="Kokoro model is not loaded")

    try:
        graphemes, phonemes, audio_b64 = kokoro.generate(request_data.text, request_data.voice, request_data.speed)
        return {"graphemes": graphemes, "phonemes": phonemes, "b64_audio": audio_b64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {e}")