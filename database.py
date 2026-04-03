import pandas as pd
import sqlite3
import os

def insert_data():
    print("🚀 Inserting into database...")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # ✅ SAME folder (NO ..)
    clean_path = os.path.join(current_dir, "cleaned_books.csv")
    db_path = os.path.join(current_dir, "books.db")

    print("📂 Looking for cleaned file at:", clean_path)

    if not os.path.exists(clean_path):
        print("❌ cleaned_books.csv not found")
        return

    df = pd.read_csv(clean_path)

    conn = sqlite3.connect(db_path)
    df.to_sql("books", conn, if_exists="replace", index=False)
    conn.close()

    print("✅ Data inserted into SQLite DB!")

if __name__ == "__main__":
    insert_data()