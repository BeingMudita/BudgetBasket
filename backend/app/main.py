from fastapi import FastAPI
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.test_db import router as test_db_router
from app.api.routes.auth import router as auth_router
from app.api.routes.user import router as users_router
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import (
    generic_exception_handler,
    validation_exception_handler,
)
from app.core.middleware import request_middleware
from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.api.routes.integrations import (
    router as integrations_router,
)

origins = [
    "http://localhost:3000",
]


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.middleware("http")(request_middleware)
app.include_router(test_db_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(health_router)
app.include_router(products_router)
app.include_router(integrations_router)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)

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