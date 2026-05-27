import httpx

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed


class BaseClient:
    BASE_URL = ""

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(2),
    )
    async def get(
        self,
        endpoint: str,
        params: dict | None = None,
        headers: dict | None = None,
    ):
        async with httpx.AsyncClient(
            timeout=10.0,
        ) as client:
            response = await client.get(
                f"{self.BASE_URL}{endpoint}",
                params=params,
                headers=headers,
            )

            response.raise_for_status()

            return response.json()