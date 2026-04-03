import sqlite3
import csv

def init_db():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            availability TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    with open("data/cleaned_books.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO books (title, price, availability)
                VALUES (?, ?, ?)
            """, (row["title"], row["price"], row["availability"]))

    conn.commit()
    conn.close()
    print("✅ Data inserted into DB")


def fetch_data():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()

    conn.close()
    return data


if __name__ == "__main__":
    init_db()
    insert_data()