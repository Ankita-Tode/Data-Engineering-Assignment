from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ FIXED DB PATH (absolute path)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "books.db")


# ✅ HOME PAGE (UI)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Book Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background-color: #f4f6f8;
                text-align: center;
                padding: 20px;
            }

            h1 {
                color: #333;
            }

            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background-color: #0056b3;
            }

            table {
                margin: 20px auto;
                border-collapse: collapse;
                width: 80%;
                background: white;
                box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            }

            th, td {
                padding: 10px;
                border: 1px solid #ddd;
            }

            th {
                background-color: #007BFF;
                color: white;
            }

            tr:hover {
                background-color: #f1f1f1;
            }
        </style>
    </head>

    <body>

        <h1>📚 Book Data Dashboard</h1>

        <button onclick="fetchData()">Fetch Data</button>

        <table id="bookTable">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Price</th>
                    <th>Rating</th>
                </tr>
            </thead>
            <tbody>
            </tbody>
        </table>

        <script>
            async function fetchData() {
                const response = await fetch('/books');
                const result = await response.json();

                const tableBody = document.querySelector("#bookTable tbody");
                tableBody.innerHTML = "";

                if (result.data && result.data.length > 0) {
                    result.data.forEach(book => {
                        let row = `
                            <tr>
                                <td>${book.title}</td>
                                <td>₹${book.price}</td>
                                <td>${book.rating}</td>
                            </tr>
                        `;
                        tableBody.innerHTML += row;
                    });
                } else {
                    tableBody.innerHTML = "<tr><td colspan='3'>No data found</td></tr>";
                }
            }
        </script>

    </body>
    </html>
    """


# ✅ API (FETCH FROM SQLITE)
@app.get("/books")
def get_books():
    if not os.path.exists(DB_PATH):
        return {"data": []}

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    conn.close()

    data = []
    for row in rows:
        data.append({
            "title": row[0],
            "price": row[1],
            "rating": row[2]
        })

    return {"data": data}