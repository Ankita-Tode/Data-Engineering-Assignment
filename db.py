import pandas as pd
import mysql.connector

try:
    # Load cleaned data
    path = "books_data_clean.csv"
    df = pd.read_csv(path)

    # Connect to MySQL (no password)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        database="clean_book"
    )

    cursor = conn.cursor()

    # Insert query
    query = """
    INSERT INTO clean_book (title, price, availability)
    VALUES (%s, %s, %s)
    """

    # Insert rows
    for index, row in df.iterrows():
        cursor.execute(query, (
            row["title"],
            row["price"],
            row["availability"]
        ))

    # Commit changes
    conn.commit()

    print("Data inserted successfully")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()
