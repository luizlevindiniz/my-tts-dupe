import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.settings import settings

app = FastAPI(title=settings.APP_TITLE)

app.include_router(router, prefix="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"message": f"Welcome to the {settings.APP_TITLE}."}

if __name__ == "__main__":
    """
    Server configurations
    """
    print(f"Starting server for: {settings.APP_TITLE}")
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=5000,
        reload=True,
        log_level="info",
        use_colors=True
    )
