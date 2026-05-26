from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class ProductPrice(Base):
    __tablename__ = "product_prices"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    selling_price: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    mrp: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    discount_percent: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    in_stock: Mapped[bool] = mapped_column(
        default=True,
    )

    platform_product_id: Mapped[int] = mapped_column(
        ForeignKey("platform_products.id"),
        nullable=False,
    )

    platform_product = relationship(
        "PlatformProduct",
        back_populates="prices",
    )