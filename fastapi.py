from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/jobs")
def get_jobs():

    conn = psycopg2.connect(
        host="localhost",
        database="clean_book",
        user="root",
        password=""
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM clean_book LIMIT 50")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows
