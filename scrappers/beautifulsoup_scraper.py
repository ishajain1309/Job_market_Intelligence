# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"

# response = requests.get(url)

# print("Status Code:", response.status_code)

# soup = BeautifulSoup(response.text, "html.parser")

# books = soup.find_all("h3")

# for book in books:
#     title = book.find("a")["title"]
#     print(title)

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://books.toscrape.com/"

# response = requests.get(url)

# print("Status Code:", response.status_code)

# soup = BeautifulSoup(response.text, "html.parser")

# books = soup.find_all("h3")

# data = []

# for book in books:
#     title = book.find("a")["title"]
#     data.append({"title": title})

# df = pd.DataFrame(data)

# df.to_csv("data/books.csv", index=False)

# print("\nData extracted successfully!")
# print(df)

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url = "https://books.toscrape.com/"

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# books = soup.find_all("article", class_="product_pod")

# data = []

# for book in books:
#     title = book.find("h3").find("a")["title"]
#     price = book.find("p", class_="price_color").text
#     rating = book.find("p", class_="star-rating")["class"][1]
#     availability = book.find("p", class_="instock").text.strip()

#     data.append({
#         "title": title,
#         "price": price,
#         "rating": rating,
#         "availability": availability
#     })

# df = pd.DataFrame(data)

# df.to_csv("data/books.csv", index=False)

# print("Data extracted successfully!")
# print(df)

# import pandas as pd

# df = pd.read_csv("data/books.csv")

# print("Before cleaning:")
# print(df)

# # Remove extra spaces
# df["title"] = df["title"].str.strip()
# df["availability"] = df["availability"].str.strip()

# # Convert price from text to number
# df["price"] = df["price"].str.replace("Â£", "", regex=False).astype(float)

# # Convert rating words to numbers
# rating_map = {
#     "One": 1,
#     "Two": 2,
#     "Three": 3,
#     "Four": 4,
#     "Five": 5
# }

# df["rating"] = df["rating"].map(rating_map)

# # Remove duplicate records
# df = df.drop_duplicates()

# df.to_csv("data/books_cleaned.csv", index=False)

# print("\nCleaning completed!")
# print(df)

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

data = []

for page in range(1, 6):
    url = base_url.format(page)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        availability = book.find("p", class_="instock").text.strip()

        data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": availability
        })

    print(f"Page {page} scraped successfully")

df = pd.DataFrame(data)

# Cleaning
df["title"] = df["title"].str.strip()
df["availability"] = df["availability"].str.strip()

df["price"] = (
    df["price"]
    .str.replace("Â£", "", regex=False)
    .astype(float)
)

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

df = df.drop_duplicates()

df.to_csv("data/books_cleaned.csv", index=False)

print("\nScraping completed!")
print("Total records:", len(df))