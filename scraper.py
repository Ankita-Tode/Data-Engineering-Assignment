import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_books():
    print("🚀 Scraping started...")

    books = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for page in range(1, 6):
        url = BASE_URL.format(page)
        print(f"🔎 Scraping: {url}")

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Error fetching page {page}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("article", class_="product_pod")

        print(f"📄 Found {len(items)} items")

        for item in items:
            try:
                title = item.h3.a["title"]
                price = item.find("p", class_="price_color").text
                stock = item.find("p", class_="instock availability").text.strip()

                books.append({
                    "title": title,
                    "price": price,
                    "stock": stock
                })
            except Exception as e:
                print("⚠️ Error parsing item:", e)
                continue

        time.sleep(1)

    print(f"📊 Total books scraped: {len(books)}")

    # ❗ FORCE at least one row (to ensure file creation)
    if len(books) == 0:
        print("⚠️ No data scraped — creating dummy file")
        books.append({
            "title": "No Data",
            "price": "0",
            "stock": "Unavailable"
        })

    df = pd.DataFrame(books)

    # ✅ SAVE EXACTLY WHERE scraper.py IS
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "raw_books.csv")

    print("📁 Saving to:", file_path)

    df.to_csv(file_path, index=False)

    # ✅ VERIFY FILE CREATED
    if os.path.exists(file_path):
        print("✅ File successfully created!")
    else:
        print("❌ File NOT created!")

    return file_path
if __name__ == "__main__":
    scrape_books()