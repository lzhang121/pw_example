import re
from playwright.sync_api import sync_playwright, expect


def test_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://playwright.dev")
        expect(page).to_have_title(re.compile("Playwright"))
        print(page.title())
        browser.close()
