
from playwright.sync_api import sync_playwright
# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto("https://www.baidu.com")
    print(page.title())
    # 等待5秒
    page.wait_for_timeout(5000)
    page.fill('#kw', "上海-悠悠博客")
    page.click('#su')
    browser.close()
