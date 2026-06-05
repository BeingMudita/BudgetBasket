from .browser_client import (
    SwiggyBrowserClient,
)

from .parser import (
    SwiggyParser,
)

class SwiggyService:

    def __init__(self):
        self.client = (
            SwiggyBrowserClient()
        )

    async def search_products(
        self,
        query: str,
    ):

        response = (
            await self.client
            .search_products(query)
        )

        if not response:

            return {
                "success": False,
                "message":
                "No response from Swiggy",
                "results": [],
            }

        products = (
            SwiggyParser.parse(
                response
            )
        )

        return {
            "success": True,
            "platform": "swiggy",
            "query": query,
            "results": products,
        }