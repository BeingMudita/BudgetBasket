from app.integrations.blinkit.client import BlinkitClient


class BlinkitService:
    def __init__(self):
        self.client = BlinkitClient()

    async def search_products(
        self,
        query: str,
    ):
        return {
            "platform": "blinkit",
            "query": query,
            "results": [],
        }