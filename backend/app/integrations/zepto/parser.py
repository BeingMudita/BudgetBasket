from app.integrations.base.schemas import (
    IntegrationProduct,
)


class ZeptoParser:
    @staticmethod
    def parse_products(
        response: dict,
    ) -> list[IntegrationProduct]:

        parsed_products = []

        layouts = response.get(
            "layout",
            [],
        )

        for widget in layouts:

            if (
                widget.get("widgetId")
                != "PRODUCT_GRID"
            ):
                continue

            items = (
                widget
                .get("data", {})
                .get("resolver", {})
                .get("data", {})
                .get("items", [])
            )

            for item in items:

                product_response = (
                    item.get(
                        "productResponse",
                        {}
                    )
                )

                product = (
                    product_response.get(
                        "product",
                        {}
                    )
                )

                variant = (
                    product_response.get(
                        "productVariant",
                        {}
                    )
                )

                image_url = None

                images = variant.get(
                    "images",
                    []
                )

                if images:

                    image_url = (
                        "https://cdn.zeptonow.com/"
                        + images[0].get(
                            "path",
                            ""
                        )
                    )

                parsed_products.append(
                    IntegrationProduct(
                        platform="zepto",
                        platform_product_id=str(
                            product_response.get(
                                "id"
                            )
                        ),
                        name=product.get(
                            "name"
                        ),
                        image_url=image_url,
                        selling_price=(
                            product_response.get(
                                "sellingPrice",
                                0,
                            )
                            / 100
                        ),
                        mrp=(
                            product_response.get(
                                "mrp",
                                0,
                            )
                            / 100
                        ),
                        in_stock=not (
                            product_response.get(
                                "outOfStock",
                                False,
                            )
                        ),
                    )
                )

        return parsed_products