from app.browser.browser_manager import BrowserManager

import json


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

        # -----------------------------
        # CAPTURE SEARCH API RESPONSE
        # -----------------------------

        async def handle_response(response):
            nonlocal captured_response

            if (
                "user-search-service/api/v3/search"
                in response.url
                and "/filters" not in response.url
                and response.status == 200
            ):
                try:
                    json_data = await response.json()

                    if "layout" in json_data:
                        captured_response = json_data

                        with open(
                            "zepto_response.json",
                            "w",
                            encoding="utf-8"
                        ) as f:
                            json.dump(
                                json_data,
                                f,
                                indent=2,
                                ensure_ascii=False,
                            )

                    import json

                    with open(
                        "zepto_response.json",
                        "w",
                        encoding="utf-8"
                    ) as f:
                        json.dump(
                            json_data,
                            f,
                            indent=2,
                            ensure_ascii=False,
                        )

                    print(
                        "PRODUCT COUNT:",
                        json_data.get(
                            "totalProductCount"
                        )
                    )
                    print(
                        "\n===================="
                    )
                    print(
                        "ZEPTO RESPONSE FOUND"
                    )
                    print(
                        "===================="
                    )

                    print(
                        "TOP LEVEL KEYS:",
                        json_data.keys()
                    )

                    with open(
                        "zepto_response.json",
                        "w",
                        encoding="utf-8",
                    ) as f:
                        json.dump(
                            json_data,
                            f,
                            indent=2,
                            ensure_ascii=False,
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

        # -----------------------------
        # DEBUG REQUESTS
        # -----------------------------

        async def handle_request(request):

            if (
                "user-search-service/api/v3/search"
                in request.url
            ):
                print(
                    "\n===================="
                )
                print(
                    "SEARCH REQUEST"
                )
                print(
                    "===================="
                )

                print(request.method)
                print(request.url)

        page.on(
            "request",
            handle_request,
        )

        # -----------------------------
        # OPEN ZEPTO
        # -----------------------------

        print(
            "\nOPENING ZEPTO"
        )

        await page.goto(
            "https://www.zepto.com/search",
            wait_until="domcontentloaded",
            timeout=60000,
        )

        print(
            "PAGE LOADED"
        )

        print(page.url)

        await page.wait_for_timeout(
            5000
        )
        inputs = await page.locator("input").all()

        print(f"TOTAL INPUTS: {len(inputs)}")

        for i, inp in enumerate(inputs):
            try:
                placeholder = await inp.get_attribute(
                    "placeholder"
                )

                print(i, placeholder)

            except Exception:
                pass
        # -----------------------------
        # PRODUCT SEARCH BOX
        # -----------------------------

        search_input = (
            page.get_by_placeholder(
                "Search for over 5000 products"
            )
        )

        await search_input.click()

        await search_input.fill(query)

        await page.keyboard.press(
            "Enter"
        )

        # -----------------------------
        # WAIT FOR RESPONSE
        # -----------------------------

        for _ in range(20):

            if captured_response:
                break

            await page.wait_for_timeout(
                1000
            )

        # -----------------------------
        # DEBUG SCREENSHOT
        # -----------------------------

        await page.screenshot(
            path="zepto_search_result.png",
            full_page=True,
        )

        print(
            "\nSCREENSHOT SAVED"
        )

        # await self.browser_manager.stop()

        return captured_response