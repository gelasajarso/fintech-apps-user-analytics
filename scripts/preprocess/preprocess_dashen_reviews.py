import pandas as pd

def preprocess_reviews(input_file="dashen_bank_reviews.csv", 
output_file="cleaned_dashen_reviews.csv"):
    print("🔍 Loading data...")
    df = pd.read_csv(input_file)

    print(f"📦 Original rows: {len(df)}")

    # 1. Remove duplicates based on review_text
    df = df.drop_duplicates(subset="review_text")
    print(f"✅ After removing duplicates: {len(df)}")

    # 2. Handle missing data: drop rows with missing values in key columns
    df = df.dropna(subset=["review_text", "rating", "date"])
    print(f"✅ After dropping missing data: {len(df)}")

    # 3. Normalize date format to YYYY-MM-DD
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Save the cleaned file
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to {output_file}")

if __name__ == "__main__":
    preprocess_reviews()
