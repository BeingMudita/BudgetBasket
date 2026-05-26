from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.core.config import settings
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.db.session import get_db
from app.models.user import User
from app.schemas.token import Token
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Auth"],
)

@router.post(
    "/signup",
    response_model=UserResponse,
)
async def signup(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    existing_user = await db.execute(
        select(User).where(User.email == user_data.username)
    )

    user = existing_user.scalar_one_or_none()

    if user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    new_user = User(
        email=user_data.username,
        hashed_password=hash_password(form_data.password),
    )

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return {
        "success": True,
        "message": "User created successfully",
        "data": {
            "id": new_user.id,
            "email": new_user.email,
        },
    }

@router.post(
    "/login",
    response_model=Token,
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(User).where(User.email == form_data.username)
    )

    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    if not verify_password(
        form_data.password,
        user.hashed_password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    access_token = create_access_token(
        subject=user.id,
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        
    }