import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.settings import settings
from app.ai import Kokoro
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--- Loading Kokoro model ---")
    kokoro_model = Kokoro()
    app.state.kokoro = kokoro_model
    if kokoro_model.is_ready():
        print("--- Kokoro model loaded successfully ---")
    else:
        print("!!! --- Kokoro model FAILED to load --- !!!")

    yield
    print("--- Cleaning up resources ---")
    app.state.kokoro = None

app = FastAPI(title=settings.APP_TITLE, lifespan=lifespan)
app.include_router(router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health(request: Request):
    model_ready = False
    if hasattr(request.app.state, 'kokoro'):
        model_ready = request.app.state.kokoro.is_ready()

    return {
        "message": f"Welcome to the {settings.APP_TITLE}.",
        "model_ready": model_ready
    }