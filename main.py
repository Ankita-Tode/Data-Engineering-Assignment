from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from db import fetch_data

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def show_books():
    data = fetch_data()

    html = "<h1>Books Data</h1><table border='1'>"
    html += "<tr><th>ID</th><th>Title</th><th>Price</th><th>Availability</th></tr>"

    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"

    html += "</table>"
    return html