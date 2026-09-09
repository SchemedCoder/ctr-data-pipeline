import pandas as pd
import sqlite3

# Load data
df = pd.read_csv("../data/ad_events.csv")

# Data quality
df = df.dropna()

# Separate events
impressions = df[df["event_type"] == "impression"]
clicks = df[df["event_type"] == "click"]

# Aggregation
impression_count = impressions.groupby("ad_id").size().reset_index(name="impressions")
click_count = clicks.groupby("ad_id").size().reset_index(name="clicks")

# Join
ctr_df = pd.merge(impression_count, click_count, on="ad_id", how="left")
ctr_df["clicks"] = ctr_df["clicks"].fillna(0)

# Calculate CTR
ctr_df["ctr"] = ctr_df["clicks"] / ctr_df["impressions"]

# Save to DB
conn = sqlite3.connect("../ctr.db")
ctr_df.to_sql("ctr_metrics", conn, if_exists="replace", index=False)

conn.close()

print("✅ CTR Pipeline Completed")

