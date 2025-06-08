🧪 Methodology
This project focuses on analyzing user experience with Ethiopian fintech mobile applications by collecting and processing user reviews from the Google Play Store. The methodology includes the following key steps:

1. Data Collection
   Used google-play-scraper (Python library) to extract 400+ recent user reviews for the Commercial Bank of Ethiopia Mobile app.

For each review, collected:

Review Text: The user’s feedback content

Rating: 1–5 star score

Date: Posting date of the review

Bank Name: App source (e.g., "Commercial Bank of Ethiopia Mobile")

Source: Platform, i.e., "Google Play"

Reviews are saved as CSV in data/raw/.

2. Preprocessing
   Duplicates removed based on identical review text

Missing data cleaned by dropping entries with empty review text, rating, or date

Dates normalized to YYYY-MM-DD format

Cleaned reviews saved to data/cleaned/

3. Folder Structure

fintech-apps-user-analytics/
├── data/
│ ├── raw/
│ └── cleaned/
├── scripts/
│ ├── scrape/
│ └── preprocess/
├── notebooks/
├── requirements.txt
└── README.md

4. Next Steps
   Text preprocessing and cleaning (tokenization, lowercasing, etc.)

Sentiment analysis using TextBlob or VADER

Visualization of rating trends and common user feedback

Comparative analysis across multiple fintech apps (CBE, BOA, Dashen)
