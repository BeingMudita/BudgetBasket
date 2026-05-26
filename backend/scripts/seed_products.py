import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.models.normalized_product import NormalizedProduct


sample_products = [
    {
        "name": "Amul Taaza Milk 500ml",
        "slug": "amul-taaza-milk-500ml",
        "quantity": "500ml",
    },
    {
        "name": "Coca Cola 750ml",
        "slug": "coca-cola-750ml",
        "quantity": "750ml",
    },
    {
        "name": "Lay's Classic Chips 52g",
        "slug": "lays-classic-chips-52g",
        "quantity": "52g",
    },
]


async def seed():
    async with AsyncSessionLocal() as db:
        for product in sample_products:
            db.add(NormalizedProduct(**product))

        await db.commit()


if __name__ == "__main__":
    asyncio.run(seed())