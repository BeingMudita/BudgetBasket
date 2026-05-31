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

        captured_response = []

        # ----------------------------------
        # CAPTURE SEARCH RESPONSES
        # ----------------------------------

        async def handle_response(response):
            nonlocal captured_response

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

                    print(type(captured_response))

                    if isinstance(captured_response, dict):
                        print(captured_response.keys())

                        import json

                        with open(
                            "blinkit_response.json",
                            "w",
                            encoding="utf-8"
                        ) as f:
                            json.dump(
                                captured_response,
                                f,
                                indent=2
                            )

                        print(
                            "JSON SAVED -> blinkit_response.json"
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

        for i in range(20):

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

        return captured_response