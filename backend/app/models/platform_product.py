from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.enums import PlatformEnum


class PlatformProduct(Base):
    __tablename__ = "platform_products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    platform: Mapped[PlatformEnum] = mapped_column(
        Enum(PlatformEnum),
        nullable=False,
        index=True,
    )

    platform_product_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    product_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    image_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    normalized_product_id: Mapped[int] = mapped_column(
        ForeignKey("normalized_products.id"),
        nullable=False,
    )

    normalized_product = relationship(
        "NormalizedProduct",
        back_populates="platform_products",
    )

    prices = relationship(
        "ProductPrice",
        back_populates="platform_product",
    )