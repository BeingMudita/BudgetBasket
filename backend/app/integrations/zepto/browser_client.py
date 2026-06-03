from app.browser.browser_manager import BrowserManager


class ZeptoBrowserClient:
    def __init__(self):
        self.browser_manager = BrowserManager()

    async def search_products(
        self,
        query: str,
    ):
        await self.browser_manager.start()

        page = await self.browser_manager.new_page()

        captured_response = None

        # ---------------------------------
        # CAPTURE SEARCH API RESPONSE
        # ---------------------------------

        async def handle_response(response):
            nonlocal captured_response

            if (
                "user-search-service/api/v3/search"
                in response.url
                and response.status == 200
            ):
                print("\n====================")
                print("ZEPTO RESPONSE FOUND")
                print("====================")
                print(response.url)

                try:
                    json_data = await response.json()

                    captured_response = json_data

                    print(
                        "TOP LEVEL KEYS:",
                        json_data.keys()
                    )

                except Exception as e:
                    print(
                        "JSON PARSE ERROR:",
                        str(e)
                    )

        page.on(
            "response",
            handle_response,
        )

        # ---------------------------------
        # DEBUG REQUESTS
        # ---------------------------------

        async def handle_request(request):

            if (
                "user-search-service/api/v3/search"
                in request.url
            ):
                print("\n====================")
                print("SEARCH REQUEST")
                print("====================")
                print(request.method)
                print(request.url)

        page.on(
            "request",
            handle_request,
        )

        # ---------------------------------
        # OPEN SEARCH PAGE
        # ---------------------------------

        print("\nOPENING ZEPTO")

        await page.goto(
            "https://www.zepto.com/search",
            wait_until="networkidle",
        )

        print("PAGE LOADED")
        print(page.url)

        await page.wait_for_timeout(
            5000
        )

        # ---------------------------------
        # FIND SEARCH INPUT
        # ---------------------------------

        inputs = await page.locator(
            "input"
        ).all()

        print(
            f"TOTAL INPUTS: {len(inputs)}"
        )

        search_input = None

        for i, inp in enumerate(inputs):

            try:

                placeholder = (
                    await inp.get_attribute(
                        "placeholder"
                    )
                )

                print(
                    i,
                    placeholder,
                )

                if placeholder:

                    if (
                        "search"
                        in placeholder.lower()
                    ):
                        search_input = inp

            except Exception:
                pass

        if not search_input:

            raise Exception(
                "Search input not found"
            )

        # ---------------------------------
        # SEARCH
        # ---------------------------------

        print(
            f"\nSEARCHING: {query}"
        )

        await search_input.click()

        await search_input.fill("")

        await search_input.press_sequentially(
            query
        )

        await page.wait_for_timeout(
            5000
        )

        # ---------------------------------
        # WAIT FOR API
        # ---------------------------------

        for _ in range(20):

            if captured_response:
                break

            await page.wait_for_timeout(
                1000
            )

        # ---------------------------------
        # SCREENSHOT
        # ---------------------------------

        await page.screenshot(
            path="zepto_search_result.png",
            full_page=True,
        )

        print(
            "\nSCREENSHOT SAVED"
        )

        # ---------------------------------
        # OPTIONAL
        # ---------------------------------

        # await self.browser_manager.stop()

        return captured_response