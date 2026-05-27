from fastapi import APIRouter

from app.integrations.blinkit.service import (
    BlinkitService,
)

router = APIRouter(
    prefix="/api/v1/integrations",
    tags=["Integrations"],
)


@router.get("/blinkit/search")
async def blinkit_search(
    query: str,
):
    service = BlinkitService()

    return await service.search_products(query)