from fastapi import FastAPI
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.test_db import router as test_db_router

origins = [
    "http://localhost:3000",
]


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(test_db_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "QuickCompare API Running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }