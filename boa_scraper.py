
from google_play_scraper import reviews, Sort
import pandas as pd

def scrape_boa_reviews(count=400):
    app_id = "com.boa.boaMobileBanking"
    bank_name = "Bank of Abyssinia"

    print(f"🔍 Scraping reviews for: {bank_name} (ID: {app_id})")

    result, _ = reviews(
        app_id,
        lang="en",
        country="et",  # Use Ethiopia region
        sort=Sort.NEWEST,
        count=count
    )

    if not result:
        print("⚠️ No reviews were fetched.")
        return

    df = pd.DataFrame(result)

    # Create the required 5 columns
    df_clean = pd.DataFrame({
        "review_text": df["content"],
        "rating": df["score"],
        "date": df["at"].dt.date,  # remove time
        "bank_name": bank_name,
        "source": "Google Play"
    })

    df_clean.to_csv("bank_of_abyssinia_reviews.csv", index=False)
    print(f"✅ Saved {len(df_clean)} reviews to bank_of_abyssinia_reviews.csv.")

if __name__ == "__main__":
    scrape_boa_reviews()
