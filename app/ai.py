import torch
from kokoro import KPipeline
from typing import Optional, Tuple, Any
import numpy as np
from app.services.create_b64_audio import create_b64_audio

class Kokoro:
    pipeline: Optional[KPipeline] = None

    def __init__(self, lang_code: str = 'a'):
        try:
            self.pipeline = KPipeline(lang_code=lang_code)
        except Exception as e:
            print(f"!!! [KokoroTTS] ERROR: Failed to load Kokoro model: {e}")

    def is_ready(self) -> bool:
        return self.pipeline is not None

    def generate(self, text: str, voice: str = 'af_heart', speed: float = 1) -> Tuple[str, str, str]:
        if not self.is_ready():
            raise RuntimeError("TTS Model is not loaded. Check server logs.")

        if not text or not text.strip():
            raise ValueError("Text cannot be empty or just whitespace. Please provide a valid text.")

        try:
            generator = self.pipeline(
                text,
                voice=voice,
                speed=speed
            )

            graphemes, phonemes, audio_data = next(generator)

            if audio_data is None:
                raise ValueError("Audio generation failed, received no data.")

            audio_data_np = audio_data.cpu().numpy()
            sample_rate = 24000
            audio_b64 = create_b64_audio(audio_data_np, sample_rate)

            return graphemes, phonemes, audio_b64
        except StopIteration:
            raise ValueError("Text was empty or invalid, no audio generated.")
        except Exception as e:
            raise RuntimeError(f"An internal error occurred during TTS generation: {str(e)}")
