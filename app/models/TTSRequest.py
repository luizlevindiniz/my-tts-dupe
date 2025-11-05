from pydantic import BaseModel, Field

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to be synthesized. Cannot be empty.")
    voice: str = Field('af_heart', description="The voice to use for synthesis. Default is 'af_heart'.")
    speed: float = Field(1.0, gt=0, le=2.0, description="Playback speed (e.g., 1.0 = normal, 0.5 = half speed). Default is 1.0.")
