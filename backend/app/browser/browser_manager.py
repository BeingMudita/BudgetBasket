from playwright.async_api import async_playwright


class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None

    async def start(self):
        self.playwright = await async_playwright().start()

        self.browser = await self.playwright.chromium.launch(
            headless=False,
            slow_mo=500,
        )

    async def stop(self):
        await self.browser.close()
        await self.playwright.stop()

    async def new_page(self):
        return await self.browser.new_page()