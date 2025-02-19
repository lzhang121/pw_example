import re
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://playwright.dev")
    expect(page).to_have_title(re.compile("Playwright"))
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")


def test_context():
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    test_context
