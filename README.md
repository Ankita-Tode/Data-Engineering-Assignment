# **B2B Book Data Pipeline**
Deployment link:https://book-scrapper-data-engineering--ankitamate.replit.app
# **🌟 Problem Statement**
Many businesses need up-to-date product data for analysis, pricing comparisons, or inventory tracking.  
This project demonstrates a **B2B-style data pipeline** that:

- Scrapes product data from an online bookstore  
- Cleans and standardizes the data  
- Stores it in a database  
- Exposes the data via an API for easy consumption  

**Source:** Books to Scrape (demo scraping site)

🏗️ Project Architecture
The system is designed as a modular ETL (Extract, Transform, Load) pipeline, serving data through a modern API.

🕵️ Scraper (scraper.py)

Responsible for navigating target websites and extracting raw book data.

Outputs: raw_books.csv.

🧹 Data Cleaning (clean_data.py)

Handles data validation, removing duplicates, and formatting prices/ratings.

Outputs: cleaned_books.csv.

🗄️ Database (database.py)

Manages the SQLite connection and schema.

Handles the "Load" phase, persisting cleaned data into books.db.

🚀 API (fastapi.py)

A RESTful interface built with FastAPI to serve the stored book data to external users or front-end applications.


## Project Structure

```text
bookscrapper/
├── book_pipeline/
│   ├── venv/                   # Virtual environment
│   ├── books.db                # SQLite database
│   ├── check_db.py             # Script to verify database entries
│   ├── clean_data.py           # Data cleaning logic
│   ├── cleaned_books.csv       # Processed data output
│   ├── database.py             # Database connection/schema setup
│   ├── main.py                 # Main entry point
│   ├── pipeline.py             # Orchestrates the ETL process
│   ├── raw_books.csv           # Raw scraped data
│   ├── requirements.txt        # Project dependencies
│   ├── runtime.txt             # Python runtime specification
│   └── scraper.py              # Web scraping logic
└── External Libraries/         # Python 3.12 interpreter files
```

# **🛠 Tech Stack**

- **Scraping:** Python, Requests, BeautifulSoup  
- **Data Cleaning:** Pandas, NumPy  
- **Database:** Sqlite 
- **API:** FastAPI
- **Automation:** Cron Jobs  
- **Deployment:** Local machine,  Replit  

# **⚡ Setup Instructions**

✅ Step 1: Install Requirements (First Time Only)

Install these:

Python (3.9+ recommended) Git

Check:python --version git --version

✅ Step 2:git clone https://github.com/Ankita-Tode/BOOK-SCRAPPER-DATA-ENGINEERING.git Clone the Repository

Then go inside: cd BOOK-SCRAPPER-DATA-ENGINEERING

✅ Step 3: Create Virtual Environment python -m venv venv

✅ Step 4: Activate Environment Windows:venv\Scripts\activate

✅ Step 5: Install Dependencies pip install -r requirements.txt

✅ Step 6: Run Your Project

Based on your project type (FastAPI): uvicorn main:app --reload

🌐 Step 7: Open in Browser

Go to:http://127.0.0.1:8000
