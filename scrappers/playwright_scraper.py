from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")

    quotes = page.locator(".quote")

    print("Quotes found:", quotes.count())

    for i in range(quotes.count()):
        quote = quotes.nth(i)

        text = quote.locator(".text").inner_text()
        author = quote.locator(".author").inner_text()

        print("\nQuote:", text)
        print("Author:", author)

    browser.close()

print("\nPlaywright scraping completed!")