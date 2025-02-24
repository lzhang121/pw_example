
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 启动浏览器
    page = browser.new_page()  # 创建一个新的页面
    page.goto("https://example.com")  # 访问网站
    print(page.title())  # 获取标题
    browser.close()  # 关闭浏览器
