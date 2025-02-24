
import re
import asyncio
from playwright.async_api import async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.baidu.com")
        await expect(page).to_have_title(re.compile("百度一下，你就知道"))
        await browser.close()


def test_title():
    asyncio.run(main())


if __name__ == "__main__":
    test_title()
