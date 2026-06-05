from pydantic import BaseModel


class SwiggyProductSchema(BaseModel):
    platform: str
    platform_product_id: str
    name: str
    image_url: str | None
    selling_price: float
    mrp: float
    in_stock: bool