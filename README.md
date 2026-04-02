# Data-Engineering-Assignment
Project Title: Automated Book Data Scraping and Analysis Pipeline
Project Overview
This project is a full-stack data engineering and API development task. It involves taking raw book dataset files, performing automated data cleaning and validation using Python (Pandas), storing the structured data in a MySQL relational database, and serving that data through a modern FastAPI web service.

Key Features
Data Pipeline: Automated cleaning of raw CSV data (handling missing values, formatting titles, and deduplication) using the Pandas library.

Database Integration: Implementation of a robust MySQL schema to store and query book information efficiently.

RESTful API: A high-performance backend built with FastAPI that allows users to interact with the book database via standard HTTP methods.

Environment Management: Secure project structure utilizing Virtual Environments (.venv) to manage dependencies like mysql-connector-python and uvicorn.

Tech Stack
Language: Python 3.x

Data Manipulation: Pandas

Database: MySQL

Web Framework: FastAPI (ASGI)

Server: Uvicorn

Installation & Setup
Clone the repository:
git clone <your-repo-url>

Install dependencies:
pip install pandas fastapi[standard] mysql-connector-python

Database Configuration:
Ensure your MySQL server is running and update the db.py configuration with your credentials.

Run the API:
fastapi dev main.py
