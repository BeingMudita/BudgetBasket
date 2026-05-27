from app.integrations.base.schemas import (
    IntegrationProduct,
)


class BlinkitParser:
    @staticmethod
    def parse_products(
        response: dict,
    ) -> list[IntegrationProduct]:
        parsed_products = []

        snippets = response.get("snippets", [])

        for snippet in snippets:
            data = snippet.get("data", {})

            product_id = data.get("product_id")

            name = data.get("name")

            image_url = data.get("image_url")

            selling_price = data.get("price")

            mrp = data.get("mrp")

            if not product_id or not name:
                continue

            parsed_products.append(
                IntegrationProduct(
                    platform="blinkit",
                    platform_product_id=str(product_id),
                    name=name,
                    image_url=image_url,
                    selling_price=selling_price,
                    mrp=mrp,
                    in_stock=True,
                )
            )

        return parsed_products