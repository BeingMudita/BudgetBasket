from app.integrations.blinkit.browser_client import (
    BlinkitBrowserClient,
)
from app.integrations.blinkit.parser import BlinkitParser


class BlinkitService:
    def __init__(self):
        self.client = BlinkitBrowserClient()

    async def search_products(
        self,
        query: str,
    ):
        response = await self.client.search_products(
            query=query,
        )

        if not response:
            return {
                "success": False,
                "message": "No response from Blinkit",
                "results": [],
            }

        products = BlinkitParser.parse_products(
            response
        )

        return {
            "success": True,
            "platform": "blinkit",
            "query": query,
            "results": products,
        }