from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router


app = FastAPI(
    title="LegalEase API",
    description="AI-powered legal document drafting backend",
    version="1.0.0",
)


# Allow Streamlit frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routes
app.include_router(router)


@app.get("/", tags=["Health"])
def root():
    return {
        "status": "ok",
        "service": "LegalEase API"
    }


@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "healthy"
    }
