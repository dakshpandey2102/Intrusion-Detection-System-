import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
df = pd.read_csv("traffic.csv")

print("Sample Data:")
print(df.head())

# Drop non-numeric columns
df_model = df.drop(columns=["src_ip", "dst_ip"])

# Train Isolation Forest
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(df_model)

# Predict anomalies
df["anomaly"] = model.predict(df_model)

# Show anomalies
anomalies = df[df["anomaly"] == -1]

print("\nTotal rows:", len(df))
print("Total anomalies:", len(anomalies))

print("\n Detected Anomalies:")
print(anomalies.head(10))
for _, row in anomalies.iterrows():
    if row["packet_size"] > 1000:
        print(f"[Large Packet] {row['src_ip']} → size {row['packet_size']}")

    elif row["dst_port"] > 50000:
        print(f"[High Port Usage] {row['src_ip']} → port {row['dst_port']}")

    else:
        print(f"[General Anomaly] {row['src_ip']}")