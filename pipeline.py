import os

os.system("python scraper/scraper.py")
os.system("python pipeline/cleaning.py")
os.system("python database/db.py")
