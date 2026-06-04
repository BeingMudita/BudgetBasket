from app.integrations.zepto.browser_client import (
    ZeptoBrowserClient,
)

from app.integrations.zepto.parser import (
    ZeptoParser,
)


class ZeptoService:
    def __init__(self):
        self.client = ZeptoBrowserClient()

    async def search_products(
        self,
        query: str,
    ):
        response = (
            await self.client.search_products(
                query=query,
            )
        )

        if not response:

            return {
                "success": False,
                "message": (
                    "No response from Zepto"
                ),
                "results": [],
            }

        products = (
            ZeptoParser.parse_products(
                response
            )
        )

        return {
            "success": True,
            "platform": "zepto",
            "query": query,
            "results": products,
        }