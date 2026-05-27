from app.integrations.base.client import BaseClient
from app.integrations.blinkit.constants import (
    BLINKIT_BASE_URL,
    BLINKIT_SEARCH_ENDPOINT,
    DEFAULT_HEADERS,
)


class BlinkitClient(BaseClient):
    BASE_URL = BLINKIT_BASE_URL

    async def search_products(
        self,
        query: str,
        offset: int = 0,
        limit: int = 12,
    ):
        params = {
            "q": query,
            "search_type": "type_to_search",
            "offset": offset,
            "limit": limit,
        }

        return await self.get(
            endpoint=BLINKIT_SEARCH_ENDPOINT,
            params=params,
            headers=DEFAULT_HEADERS,
        )