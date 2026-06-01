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

        captured_responses = []

        # ----------------------------------
        # CAPTURE SEARCH RESPONSES
        # ----------------------------------

        async def handle_response(response):
            nonlocal captured_responses

            if (
                "/v1/layout/search" in response.url
                and response.status == 200
            ):
                print("\n========================")
                print("FOUND SEARCH RESPONSE")
                print("========================")
                print(response.url)

                try:
                    response_json = await response.json()

                    captured_responses.append(
                        response_json
                    )

                    print(
                        f"TOTAL CAPTURED RESPONSES: "
                        f"{len(captured_responses)}"
                    )

                    print("\n========================")
                    print("RESPONSE CAPTURED")
                    print("========================")


                    print(
                        f"Captured responses: "
                        f"{len(captured_responses)}"
                    )
                except Exception as e:
                    print("JSON ERROR:", e)

        page.on("response", handle_response)

        # ----------------------------------
        # CAPTURE SEARCH REQUESTS
        # ----------------------------------

        async def handle_request(request):
            if "/v1/layout/search" in request.url:
                print("\n========================")
                print("FOUND SEARCH REQUEST")
                print("========================")
                print("METHOD:", request.method)
                print("URL:", request.url)

                try:
                    print("HEADERS:")
                    print(request.headers)
                except Exception:
                    pass

        page.on("request", handle_request)

        # ----------------------------------
        # OPEN SEARCH PAGE DIRECTLY
        # ----------------------------------

        print("\nOPENING SEARCH PAGE")

        await page.goto(
            f"https://blinkit.com/s/?q={query}",
            wait_until="networkidle",
        )

        print("\nSEARCH PAGE LOADED")
        print("URL:", page.url)

        # Give Blinkit enough time
        await page.wait_for_timeout(15000)
        print(
            "\nSTARTING AUTO SCROLL"
        )

        for i in range(17):

            await page.mouse.wheel(
                0,
                5000
            )

            await page.wait_for_timeout(
                2000
            )

            print(
                f"SCROLL {i + 1}"
            )

        # ----------------------------------
        # SCREENSHOT
        # ----------------------------------

        await page.screenshot(
            path="blinkit_search_result.png",
            full_page=True,
        )

        print(
            "\nSCREENSHOT SAVED: blinkit_search_result.png"
        )

        # ----------------------------------
        # RETURN
        # ----------------------------------

        all_snippets = []

        for response in captured_responses:

            response_data = response.get(
                "response",
                {}
            )

            snippets = response_data.get(
                "snippets",
                []
            )

            all_snippets.extend(
                snippets
            )

        print(
            f"\nTOTAL RAW SNIPPETS: "
            f"{len(all_snippets)}"
        )

        unique_products = {}

        for snippet in all_snippets:

            product_id = (
                snippet.get(
                    "data",
                    {}
                ).get(
                    "product_id"
                )
            )

            if product_id:

                unique_products[
                    str(product_id)
                ] = snippet

        all_snippets = list(
            unique_products.values()
        )

        print(
            f"UNIQUE PRODUCTS: "
            f"{len(all_snippets)}"
        )

        return {
            "response": {
                "snippets": all_snippets
            }
        }