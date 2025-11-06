from fastapi import APIRouter, HTTPException, Request
from app.models.TTSRequest import TTSRequest
from typing import Any

router = APIRouter()

@router.post("/tts")
async def tts(request_data: TTSRequest, request: Request) -> dict[str, Any]:
    kokoro = request.app.state.kokoro

    if not kokoro.is_ready():
        raise HTTPException(status_code=503, detail="Kokoro model is not loaded")

    try:
        graphemes, phonemes, audio_b64 = kokoro.generate(request_data.text, request_data.voice, request_data.speed)
        return {"graphemes": graphemes, "phonemes": phonemes, "b64_audio": audio_b64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {e}")