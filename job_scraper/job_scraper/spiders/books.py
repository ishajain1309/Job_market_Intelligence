# import scrapy


# class BooksSpider(scrapy.Spider):
#     name = "books"
#     allowed_domains = ["books.toscrape.com"]
#     start_urls = ["https://books.toscrape.com"]

#     def parse(self, response):
#         pass

import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    def parse(self, response):
        books = response.css("article.product_pod")

        for book in books:
            yield {
                "title": book.css("h3 a::attr(title)").get(),
                "price": book.css("p.price_color::text").get(),
                "availability": book.css("p.instock::text").getall()[-1].strip(),
                "rating": book.css("p.star-rating::attr(class)").get()
            }