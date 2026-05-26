from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base import Base


class NormalizedProduct(Base):
    __tablename__ = "normalized_products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        index=True,
    )

    slug: Mapped[str] = mapped_column(
        String,
        unique=True,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    image_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    quantity: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    brand_id: Mapped[int | None] = mapped_column(
        ForeignKey("brands.id"),
        nullable=True,
    )

    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.id"),
        nullable=True,
    )

    brand = relationship("Brand")

    category = relationship("Category")

    platform_products = relationship(
        "PlatformProduct",
        back_populates="normalized_product",
    )