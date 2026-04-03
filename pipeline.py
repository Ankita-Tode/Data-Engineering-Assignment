from scraper import scrape_books
from clean_data import clean_data
from database import insert_data

def run_pipeline():
    print("🚀 Starting pipeline...")

    scrape_books()
    clean_data()
    insert_data()

    print("✅ Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()