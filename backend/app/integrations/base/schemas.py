from pydantic import BaseModel


class IntegrationProduct(BaseModel):
    platform: str
    platform_product_id: str

    name: str

    image_url: str | None = None

    selling_price: float | None = None

    mrp: float | None = None

    in_stock: bool = True