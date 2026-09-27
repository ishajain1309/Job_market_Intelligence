from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

url = "https://quotes.toscrape.com/js/"
driver.get(url)

time.sleep(2)

quotes = driver.find_elements(By.CLASS_NAME, "quote")

print("Quotes found:", len(quotes))

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text

    print("\nQuote:", text)
    print("Author:", author)

driver.quit()

print("\nSelenium scraping completed!")