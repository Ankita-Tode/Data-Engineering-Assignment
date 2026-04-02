import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for page in range(1,10):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    items = soup.find_all("article",class_="product_pod")

    for item in items:

        title = item.h3.a["title"]
        price = item.find("p",class_="price_color").text
        availability = item.find("p",class_="instock availability").text.strip()

        books.append({
            "title": title,
            "price": price,
            "availability": availability
        })

df = pd.DataFrame(books)

df.to_csv("books_data.csv",index=False)

print("Books data saved")
