import httpx

from app.integrations.swiggy.constants import (
    SWIGGY_SEARCH_URL,
    STORE_ID,
    PRIMARY_STORE_ID,
    LAYOUT_ID,
    DEVICE_ID,
    BUILD_VERSION,
)


class SwiggyBrowserClient:

    async def search_products(
        self,
        query: str,
    ):

        params = {
            "offset": 0,
            "ageConsent": "false",
            "layoutId": LAYOUT_ID,
            "voiceSearchTrackingId": "",
            "storeId": STORE_ID,
            "primaryStoreId": PRIMARY_STORE_ID,
            "secondaryStoreId": "",
        }

        payload = {
            "facets": [],
            "sortAttribute": "",
            "query": query,
            "search_results_offset": "0",
            "page_type": "INSTAMART_SEARCH_PAGE",
            "is_pre_search_tag": False,
        }

        headers = {
            "accept": "*/*",
            "content-type": "application/json",
            "origin": "https://www.swiggy.com",
            "referer": (
                "https://www.swiggy.com/"
            ),
            "user-agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/149.0.0.0 Safari/537.36"
            ),
            "x-build-version": BUILD_VERSION,
            "x-device-id": DEVICE_ID,
        }

        async with httpx.AsyncClient(
            timeout=30
        ) as client:

            response = await client.post(
                SWIGGY_SEARCH_URL,
                params=params,
                json=payload,
                headers=headers,
            )

            print(
                "SWIGGY STATUS:",
                response.status_code
            )

            if response.status_code != 200:
                return None

            return response.json()