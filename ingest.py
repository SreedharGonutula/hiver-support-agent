"""Ingest one brand from Customer Support on Twitter."""
from pathlib import Path
import argparse
import pandas as pd

REQUIRED = {"tweet_id","author_id","inbound","created_at","text",
            "response_tweet_id","in_response_to_tweet_id"}

def load_brand(csv_path, brand="AppleSupport", sample_size=20_000, seed=42):
    parts = []
    for chunk in pd.read_csv(
        csv_path, chunksize=200_000,
        dtype={"tweet_id":"Int64","author_id":"string","inbound":"boolean",
               "created_at":"string","text":"string",
               "response_tweet_id":"string","in_response_to_tweet_id":"string"}):
        missing = REQUIRED - set(chunk.columns)
        if missing:
            raise ValueError(f"Missing columns: {sorted(missing)}")
        x = chunk[chunk["author_id"].eq(brand)].copy()
        if not x.empty:
            parts.append(x)

    if not parts:
        raise ValueError(f"No rows found for brand={brand!r}")

    df = pd.concat(parts, ignore_index=True)
    df["text"] = (df["text"].fillna("").astype(str)
                  .str.replace(r"\s+", " ", regex=True).str.strip())
    df = df[df["text"].ne("")].drop_duplicates("tweet_id")

    if sample_size and len(df) > sample_size:
        df = df.sample(sample_size, random_state=seed)

    return df.reset_index(drop=True)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True)
    p.add_argument("--brand", default="AppleSupport")
    p.add_argument("--sample-size", type=int, default=20_000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", default="data/processed/brand_tweets.csv")
    a = p.parse_args()

    df = load_brand(a.csv, a.brand, a.sample_size, a.seed)
    out = Path(a.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"brand={a.brand}\nrows={len(df):,}\noutput={out}")

if __name__ == "__main__":
    main()
