from app.integrations.base.schemas import (
    IntegrationProduct,
)


class ZeptoParser:

    @staticmethod
    def parse_products(response):

        products = []

        layout = response.get(
            "layout",
            []
        )

        for widget in layout:

            if (
                widget.get("widgetId")
                != "PRODUCT_GRID"
            ):
                continue

            items = (
                widget.get("data", {})
                .get("resolver", {})
                .get("data", {})
                .get("items", [])
            )

            for item in items:

                try:

                    product_response = item[
                        "productResponse"
                    ]

                    product = (
                        product_response[
                            "product"
                        ]
                    )

                    variant = (
                        product_response[
                            "productVariant"
                        ]
                    )

                    image_url = None

                    if variant.get("images"):

                        image_url = (
                            variant["images"][0]
                            .get("path")
                        )

                    products.append(
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
                                    0
                                )
                                / 100
                            ),
                            mrp=(
                                product_response.get(
                                    "mrp",
                                    0
                                )
                                / 100
                            ),
                            in_stock=not (
                                product_response.get(
                                    "outOfStock",
                                    False
                                )
                            ),
                        )
                    )

                except Exception:
                    pass

        return products