from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

router = APIRouter()


@router.get("/db-test")
async def test_db(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "result": result.scalar()
    }