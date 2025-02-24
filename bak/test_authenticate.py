import re
from playwright.sync_api import Playwright, expect


def test_authenticate(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://github.com/login')

    # Interact with login form
    page.get_by_label("Username or email address").fill("zhspark@gmail.com")
    page.get_by_label("Password").fill("Qatest2024")
    page.get_by_role("button", name="Sign in").click()
    expect(page).to_have_title(re.compile("Dashboard"))


def test_authenticate_2(playwright: Playwright) -> None:
    page = await context.new_page()
    await page.goto('https://github.com/login')
    # Interact with login form
    await page.get_by_label("Username or email address").fill("username")
    await page.get_by_label("Password").fill("password")
    await page.page.get_by_role("button", name="Sign in").click()
