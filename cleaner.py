import csv
import os

def clean_books_csv():
    print("🚀 Cleaning started...")

    if not os.path.exists("data/raw_books.csv"):
        print("❌ raw_books.csv not found")
        return

    with open("data/raw_books.csv", "r", encoding="utf-8") as infile, \
         open("data/cleaned_books.csv", "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["title", "price", "availability"])

        writer.writeheader()

        for row in reader:
            title = row["title"].strip()

            price = row["price"]
            price = price.replace("£", "").replace("Â", "").strip()

            try:
                price = float(price)
            except:
                price = 0.0

            availability = row["availability"].strip()

            writer.writerow({
                "title": title,
                "price": price,
                "availability": availability
            })

    print("✅ Cleaned CSV created!")

if __name__ == "__main__":
    clean_books_csv()