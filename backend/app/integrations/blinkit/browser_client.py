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
                print("\nFOUND SEARCH RESPONSE")
                print(response.url)

                try:
                    captured_response = await response.json()
                    print("RESPONSE CAPTURED")
                except Exception as e:
                    print("JSON ERROR:", e)

        page.on("response", handle_response)

        async def handle_request(request):
            if "layout/search" in request.url:
                print("\nFOUND SEARCH REQUEST")
                print("METHOD:", request.method)
                print("URL:", request.url)

        page.on("request", handle_request)

        await page.goto(
            "https://blinkit.com",
            wait_until="networkidle",
        )

        print("\nPAGE LOADED")
        print("URL:", page.url)

        await page.wait_for_timeout(3000)

        # ----------------------------
        # LOCATION INPUT
        # ----------------------------

        inputs = await page.locator("input").all()

        print(f"\nTOTAL INPUTS: {len(inputs)}")

        for i, inp in enumerate(inputs):
            try:
                placeholder = await inp.get_attribute(
                    "placeholder"
                )

                print(i, placeholder)

            except Exception:
                pass

        if len(inputs) == 0:
            raise Exception(
                "No input found for location"
            )

        location_input = inputs[0]

        print("\nSETTING LOCATION")

        await location_input.fill(location)

        await page.wait_for_timeout(3000)

        await page.keyboard.press("ArrowDown")

        await page.wait_for_timeout(1000)

        await page.keyboard.press("Enter")

        print("\nLOCATION SELECTED")

        await page.wait_for_timeout(8000)

        print("\nCURRENT URL:")
        print(page.url)

        # ----------------------------
        # FIND EVERYTHING CONTAINING
        # SEARCH TEXT
        # ----------------------------

        print("\nLOOKING FOR SEARCH ELEMENTS")

        all_elements = await page.locator("*").all()

        print(
            f"TOTAL ELEMENTS: {len(all_elements)}"
        )

        search_candidates = []

        for i, el in enumerate(all_elements[:2000]):
            try:
                text = (
                    await el.inner_text()
                ).strip()

                if (
                    "Search" in text
                    or "search" in text
                ):
                    print(
                        f"\nMATCH {len(search_candidates)}"
                    )

                    print("INDEX:", i)
                    print("TEXT:", text[:200])

                    search_candidates.append(el)

            except Exception:
                pass

        print(
            f"\nFOUND {len(search_candidates)} SEARCH CANDIDATES"
        )

        # ----------------------------
        # CLICK FIRST SEARCH CANDIDATE
        # ----------------------------

        if len(search_candidates) > 0:

            print(
                "\nCLICKING FIRST SEARCH CANDIDATE"
            )

            try:
                await search_candidates[0].click()

                await page.wait_for_timeout(
                    3000
                )

                print(
                    "AFTER CLICK URL:",
                    page.url
                )

            except Exception as e:
                print(
                    "CLICK FAILED:",
                    str(e)
                )

        # ----------------------------
        # DEBUG SCREENSHOT
        # ----------------------------

        await page.screenshot(
            path="blinkit_debug.png",
            full_page=True
        )

        print(
            "\nSCREENSHOT SAVED: blinkit_debug.png"
        )

        return {
            "status": "debug_complete",
            "captured_response": captured_response
        }