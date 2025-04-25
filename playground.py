from playwright.sync_api import sync_playwright

def get_resy_api_key():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        # Block images/fonts to speed things up
        context.route("**/*.{png,jpg,jpeg,svg,gif,woff,woff2,ttf,otf,ico}", lambda route: route.abort())

        page = context.new_page()
        page.goto("https://resy.com", wait_until="domcontentloaded")

        api_key = page.evaluate("() => window.apiConfig.Config.apiKey")

        browser.close()
        return api_key

print("Extracted Resy API Key:", get_resy_api_key())
