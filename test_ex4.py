import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("test")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("test")
    expect(page.get_by_label("Toggle Todo")).not_to_be_checked()

    # ---------------------
    context.close()
    browser.close()


def test_run():
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    test_run()
