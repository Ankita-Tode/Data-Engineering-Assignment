import requests
from bs4 import BeautifulSoup
import csv
import os

def scrape_books_to_csv():
    print("🚀 Scraping started...")

    url = "https://books.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, timeout=10)

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    os.makedirs("data", exist_ok=True)

    with open("data/raw_books.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "price", "availability"])

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip()
            availability = book.find("p", class_="instock availability").text.strip()

            writer.writerow([title, price, availability])

    print("✅ Raw CSV created!")

if __name__ == "__main__":
    scrape_books_to_csv()