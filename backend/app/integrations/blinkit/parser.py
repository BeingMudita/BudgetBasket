from app.integrations.base.schemas import (
    IntegrationProduct,
)


class BlinkitParser:

    @staticmethod
    def parse_products(
        response: dict,
    ) -> list[IntegrationProduct]:

        parsed_products = []

        response_data = response.get(
            "response",
            {}
        )

        snippets = response_data.get(
            "snippets",
            []
        )

        print(
            f"TOTAL SNIPPETS: {len(snippets)}"
        )

        for snippet in snippets:

            data = snippet.get(
                "data",
                {}
            )

            product_id = data.get(
                "product_id"
            )

            name = (
                data.get("name", {})
                .get("text")
            )

            image_url = (
                data.get("image", {})
                .get("url")
            )

            cart_item = (
                data.get(
                    "atc_action",
                    {}
                )
                .get(
                    "add_to_cart",
                    {}
                )
                .get(
                    "cart_item",
                    {}
                )
            )

            selling_price = cart_item.get(
                "price"
            )

            mrp = cart_item.get(
                "mrp"
            )

            print(
                product_id,
                name,
                selling_price
            )

            if not product_id:
                continue

            parsed_products.append(
                IntegrationProduct(
                    platform="blinkit",
                    platform_product_id=str(
                        product_id
                    ),
                    name=name,
                    image_url=image_url,
                    selling_price=selling_price,
                    mrp=mrp,
                    in_stock=True,
                )
            )

        print(
            f"PARSED PRODUCTS: {len(parsed_products)}"
        )

        return parsed_products