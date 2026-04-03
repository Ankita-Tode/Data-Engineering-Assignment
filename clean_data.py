import pandas as pd
import os

def clean_data():
    print("🚀 Cleaning started...")

    # ✅ Get correct path of current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    raw_path = os.path.join(current_dir, "raw_books.csv")
    clean_path = os.path.join(current_dir, "cleaned_books.csv")

    print("📂 Looking for raw file at:", raw_path)

    # ❌ If raw file not found
    if not os.path.exists(raw_path):
        print("❌ raw_books.csv NOT FOUND!")
        return

    # ✅ Read CSV
    df = pd.read_csv(raw_path)

    print("\n📊 Raw Data Sample:")
    print(df.head())

    print(f"\nBefore cleaning: {len(df)} rows")

    # ✅ Clean price
    df["price"] = df["price"].astype(str).str.replace("Â£", "")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # ✅ Clean stock
    df["stock"] = df["stock"].astype(str).str.strip()

    # ✅ Drop null values
    df = df.dropna()

    print(f"After cleaning: {len(df)} rows")

    # ✅ Save cleaned file
    print("💾 Saving cleaned file at:", clean_path)

    df.to_csv(clean_path, index=False)

    # ✅ Confirm file creation
    if os.path.exists(clean_path):
        print("✅ cleaned_books.csv created successfully!")
    else:
        print("❌ File NOT created!")

# 🔥 RUN FILE DIRECTLY
if __name__ == "__main__":
    clean_data()