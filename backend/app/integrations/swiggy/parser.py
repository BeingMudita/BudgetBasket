from .constants import (
    PLATFORM,
    IMAGE_BASE_URL,
)
from .schemas import (
    SwiggyProductSchema,
)

class SwiggyParser:

    @staticmethod
    def parse(response):

        products = []

        cards = (
            response
            .get("data", {})
            .get("cards", [])
        )

        for card_wrapper in cards:

            try:

                items = (
                    card_wrapper["card"]["card"]
                    ["gridElements"]
                    ["infoWithStyle"]
                    ["items"]
                )

            except Exception:
                continue

            for item in items:

                variations = item.get(
                    "variations",
                    [],
                )

                if not variations:
                    continue

                variation = variations[0]

                image_url = None

                image_ids = (
                    variation.get(
                        "imageIds",
                        []
                    )
                )

                if image_ids:

                    image_url = (
                        IMAGE_BASE_URL
                        + image_ids[0]
                    )

                products.append(
                    SwiggyProductSchema(
                        platform=PLATFORM,
                        platform_product_id=item.get(
                            "productId",
                            ""
                        ),
                        name=item.get(
                            "displayName",
                            ""
                        ),
                        image_url=image_url,
                        selling_price=float(
                            variation["price"]
                            ["offerPrice"]
                            ["units"]
                        ),
                        mrp=float(
                            variation["price"]
                            ["mrp"]
                            ["units"]
                        ),
                        in_stock=variation
                        .get(
                            "inventory",
                            {}
                        )
                        .get(
                            "inStock",
                            False
                        ),
                    )
                )

        return products