from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
page = browser.new_page(no_viewport=True)
page.goto("https://www.google.com/")
page.fill("textarea[name='q']", "Playwright Python")
page.press("textarea[name='q']", "Enter")


page.wait_for_timeout(3000)
browser.close()



playwright.stop()