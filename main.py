from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
import asyncio

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
            body { font-family: Arial; background-color: #f4f6f8; text-align: center; padding: 20px; }
            h1 { color: #333; }
            #status-container { 
                margin: 20px auto; 
                padding: 15px; 
                width: 50%; 
                border-radius: 8px; 
                font-weight: bold;
                min-height: 24px;
            }
            .status-scraping { color: #856404; background-color: #fff3cd; border: 1px solid #ffeeba; }
            .status-cleaning { color: #0c5460; background-color: #d1ecf1; border: 1px solid #bee5eb; }
            .status-storing { color: #155724; background-color: #d4edda; border: 1px solid #c3e6cb; }

            button { padding: 10px 20px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
            table { margin: 20px auto; border-collapse: collapse; width: 80%; background: white; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
            th, td { padding: 10px; border: 1px solid #ddd; }
            th { background-color: #007BFF; color: white; }
            tr:hover { background-color: #f1f1f1; }
        </style>
    </head>
    <body>
        <h1>📚 Book Data Dashboard</h1>
        <button onclick="processData()">Start Data Pipeline</button>

        <div id="status-container" style="display: none;"></div>

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
            function updateStatus(message, className) {
                const statusDiv = document.getElementById("status-container");
                statusDiv.innerText = message;
                statusDiv.className = className;
                statusDiv.style.display = "block";
            }

            async function processData() {
                const tableBody = document.querySelector("#bookTable tbody");
                tableBody.innerHTML = "";

                // 1. Show Scraping Status
                updateStatus("🔍 Phase 1: Scraping data from source...", "status-scraping");
                await new Promise(r => setTimeout(r, 1000)); // Visual delay

                // 2. Show Cleaning Status
                updateStatus("🧹 Phase 2: Cleaning and formatting data...", "status-cleaning");
                await new Promise(r => setTimeout(r, 1000));

                // 3. Show Storing Status
                updateStatus("💾 Phase 3: Storing data into SQLite database...", "status-storing");
                await new Promise(r => setTimeout(r, 800));

                // 4. Fetch and Show Data
                try {
                    const response = await fetch('/books');
                    const result = await response.json();

                    updateStatus("✅ Operation Complete: Data Loaded", "status-storing");

                    if (result.data && result.data.length > 0) {
                        result.data.forEach(book => {
                            let row = `<tr>
                                <td>${book.title}</td>
                                <td>₹${book.price}</td>
                                <td>${book.rating}</td>
                            </tr>`;
                            tableBody.innerHTML += row;
                        });
                    } else {
                        tableBody.innerHTML = "<tr><td colspan='3'>No data found in database.</td></tr>";
                    }
                } catch (error) {
                    updateStatus("❌ Error fetching data", "");
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