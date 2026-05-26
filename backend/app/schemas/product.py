from app.schemas.pagination import PaginationMeta
from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    name: str
    slug: str
    image_url: str | None = None
    quantity: str | None = None

    class Config:
        from_attributes = True

class PlatformPrice(BaseModel):
    platform: str
    selling_price: float
    mrp: float | None = None
    discount_percent: float | None = None
    in_stock: bool

class ProductComparisonResponse(ProductBase):
    prices: list[PlatformPrice]

class ProductSearchResponse(BaseModel):
    success: bool = True
    message: str
    data: list[ProductBase]
    pagination: PaginationMeta