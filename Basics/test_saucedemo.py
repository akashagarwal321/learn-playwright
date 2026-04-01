from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"], channel='msedge')
    page = browser.new_page(no_viewport=True)
    page.goto("https://www.saucedemo.com")
    
    page.wait_for_timeout(200)

    page.fill("#user-name", "standard_user")

    page.wait_for_timeout(200)

    page.fill("#password", "secret_sauce")

    page.wait_for_timeout(200)


    page.click("#login-button")

    page.wait_for_timeout(3000)
    browser.close()