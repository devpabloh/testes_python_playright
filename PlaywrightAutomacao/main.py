from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("input[name='q']", "Playwright")
    page.press("input[name='q']", "Enter")
    page.wait_for_timeout(2000)  # Wait for 2 seconds to see the results
    browser.close()