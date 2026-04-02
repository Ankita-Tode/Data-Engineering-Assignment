import  pandas as pd

df = pd.read_csv("books_data.csv")

df.drop_duplicates(inplace=True)

df["title"] = df["title"].str.strip()

df["price"] = df["price"].str.replace(r"[^\d.]", "", regex=True)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["availability"] = df["availability"].str.strip()
df["availability"] = df["availability"].str.replace(r"\s+", " ", regex=True)

df.reset_index(drop=True, inplace=True)

df.to_csv("books_data_clean.csv", index=False)

print("Cleaned books data saved")
