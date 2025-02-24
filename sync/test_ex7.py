

from playwright.sync_api import sync_playwright
# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    print(page.title())
    # page.fill("#kw", "上海-悠悠")
    page.fill("id=kw", "上海-悠悠")
    page.click('text=百度一下')
    page.wait_for_timeout(5000)
    browser.close()
