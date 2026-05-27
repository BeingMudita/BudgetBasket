import json

from app.browser.browser_manager import BrowserManager


class BlinkitBrowserClient:
    def __init__(self):
        self.browser_manager = BrowserManager()

    async def search_products(
        self,
        query: str,
    ):
        await self.browser_manager.start()

        page = await self.browser_manager.new_page()

        captured_response = None

        async def handle_response(response):
            nonlocal captured_response

            if (
                "/v1/layout/search" in response.url
                and response.status == 200
            ):
                try:
                    captured_response = await response.json()
                except Exception:
                    pass

        page.on("response", handle_response)

        await page.goto("https://blinkit.com" , wait_until="networkidle")
        print(await page.title())
        await page.screenshot(path="blinkit_homepage.png")
        await page.fill(
            'input[placeholder*="Search"]',
            query,
        )

        await page.keyboard.press("Enter")

        await page.wait_for_timeout(5000)

        await self.browser_manager.stop()

        return captured_response