from app.browser.browser_manager import BrowserManager


class BlinkitBrowserClient:
    def __init__(self):
        self.browser_manager = BrowserManager()

    async def search_products(
        self,
        query: str,
        location: str = "gurgaon",
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
        async def handle_request(request):
            if "layout/search" in request.url:
                print("FOUND SEARCH REQUEST")
                print(request.method)
                print(request.url)
                print(request.headers)

        page.on("request", handle_request)

        page.on(
            "request",
            lambda req: print(
                req.method,
                req.url
            )
        )
        await page.goto(
            "https://blinkit.com",
            wait_until="networkidle",
        )

        # WAIT FOR LOCATION MODAL
        await page.wait_for_timeout(3000)

        inputs = await page.locator("input").all()

        print(f"TOTAL INPUTS: {len(inputs)}")

        for i, inp in enumerate(inputs):
            try:
                placeholder = await inp.get_attribute("placeholder")
                print(i, placeholder)
            except Exception:
                pass

        location_input = inputs[0]  # Assuming the first input is the location input

        await location_input.fill(location)
        await page.wait_for_timeout(3000)

        await page.keyboard.press("ArrowDown")

        await page.wait_for_timeout(1000)

        await page.keyboard.press("Enter")

        await page.wait_for_timeout(3000)

        await page.wait_for_timeout(5000)

        all_divs = await page.locator("div").all()

        print(f"TOTAL DIVS: {len(all_divs)}")

        for i, div in enumerate(all_divs[:50]):
            try:
                text = await div.inner_text()

                if text.strip():
                    print(i, text[:100])

            except Exception:
                pass

        await page.wait_for_timeout(5000)

        # SEARCH INPUT
        locators = await page.locator("*").all()

        for i, el in enumerate(locators[:500]):
            try:
                text = await el.inner_text()

                if "Search" in text:
                    print(i, text)

            except:
                pass

        await search_input.click()

        await search_input.press_sequentially(query)

        await page.keyboard.press("Enter")

        await page.wait_for_timeout(5000)
        print(page.url)
        await page.screenshot(
            path="blinkit_search_result.png"
        )

        # await self.browser_manager.stop()

        return captured_response