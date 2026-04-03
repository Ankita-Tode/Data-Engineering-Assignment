import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print(cursor.fetchone())

conn.close()