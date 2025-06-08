import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load model once
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_sentiment(text):
    try:
        result = sentiment_pipeline(text[:512])[0]  # limit input length
        label = result["label"]
        score = result["score"]

        # Optional: Define "neutral" zone manually
        if score < 0.6:
            return "NEUTRAL"
        return label.upper()
    except:
        return "NEUTRAL"

def run_sentiment_analysis(input_file="data/cleaned/cleaned_boa_reviews.csv", output_file="data/cleaned/boa_with_sentiment.csv"):
    df = pd.read_csv(input_file)

    print("🔍 Running sentiment analysis...")
    tqdm.pandas()
    df["sentiment"] = df["review_text"].progress_apply(classify_sentiment)

    df.to_csv(output_file, index=False)
    print(f"✅ Saved results to {output_file}")

    return df

def aggregate_sentiment(df):
    print("\n📊 Sentiment by Star Rating:")
    grouped = df.groupby(["rating", "sentiment"]).size().unstack(fill_value=0)
    print(grouped)

if __name__ == "__main__":
    df_result = run_sentiment_analysis()
    aggregate_sentiment(df_result)
