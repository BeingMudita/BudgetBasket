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
        return await self.client.search_products(
            query=query
        )