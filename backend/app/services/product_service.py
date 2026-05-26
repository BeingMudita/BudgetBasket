from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.normalized_product import NormalizedProduct


class ProductService:
    @staticmethod
    async def search_products(
        db: AsyncSession,
        query: str,
        page: int = 1,
        limit: int = 10,
    ):
        offset = (page - 1) * limit

        search_query = (
            select(NormalizedProduct)
            .where(
                func.lower(NormalizedProduct.name).contains(
                    query.lower()
                )
            )
            .offset(offset)
            .limit(limit)
        )

        count_query = (
            select(func.count())
            .select_from(NormalizedProduct)
            .where(
                func.lower(NormalizedProduct.name).contains(
                    query.lower()
                )
            )
        )

        results = await db.execute(search_query)

        products = results.scalars().all()

        total_result = await db.execute(count_query)

        total = total_result.scalar()

        return products, total