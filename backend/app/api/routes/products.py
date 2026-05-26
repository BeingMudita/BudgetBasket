from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.pagination import PaginationMeta
from app.schemas.product import ProductSearchResponse
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"],
)


@router.get(
    "/search",
    response_model=ProductSearchResponse,
)
async def search_products(
    query: str = Query(..., min_length=1),
    page: int = 1,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    products, total = await ProductService.search_products(
        db=db,
        query=query,
        page=page,
        limit=limit,
    )

    return {
        "success": True,
        "message": "Products fetched successfully",
        "data": products,
        "pagination": PaginationMeta(
            page=page,
            limit=limit,
            total=total,
        ),
    }