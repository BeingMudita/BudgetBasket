from app.integrations.base.schemas import (
    IntegrationProduct,
)


class BlinkitParser:
    @staticmethod
    def parse_products(response: dict):

        print("=" * 50)
        print("TOP LEVEL KEYS")
        print(response.keys())
        print("=" * 50)

        return []