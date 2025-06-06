
from google_play_scraper import reviews, Sort
import pandas as pd

def scrape_cbe_reviews(count=400):
    app_id = "com.combanketh.mobilebanking"
    bank_name = "Commercial Bank of Ethiopia Mobile"

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

    df_clean.to_csv("commercial_bank_of_ethiopia_reviews.csv", index=False)
    print(f"✅ Saved {len(df_clean)} reviews to commercial_bank_of_ethiopia_reviews.csv.")

if __name__ == "__main__":
    scrape_cbe_reviews()
