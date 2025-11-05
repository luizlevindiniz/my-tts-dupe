import base64
import io
import numpy as np
import soundfile as sf

def create_b64_audio(audio_data: np.ndarray, sample_rate: int) -> str:
  try:
    buffer = io.BytesIO()
    sf.write(buffer, audio_data, sample_rate, format='WAV', subtype='PCM_16')
    wav_bytes = buffer.getvalue()
    audio_b64 = base64.b64encode(wav_bytes).decode('utf-8')
    return audio_b64
  except Exception as e:
    raise RuntimeError(f"Failed to create Base64 audio: {str(e)}")