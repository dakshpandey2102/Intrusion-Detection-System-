import pandas as pd
from sklearn.ensemble import IsolationForest
import socket

#  Function to get domain name from IP
def get_domain(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

#  Load dataset
df = pd.read_csv("traffic.csv")

print("Sample Data:")
print(df.head())

#  Drop non-numeric columns (important for ML)
df_model = df.drop(columns=["src_ip", "dst_ip"])

#  Train Isolation Forest
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(df_model)

#  Predict anomalies
df["anomaly"] = model.predict(df_model)

#  Filter anomalies
anomalies = df[df["anomaly"] == -1]

print("\nTotal rows:", len(df))
print("Total anomalies:", len(anomalies))

print("\n Detected Anomalies:\n")

#  Loop through anomalies with domain info
for _, row in anomalies.iterrows():
    domain = get_domain(row["src_ip"])

    if row["packet_size"] > 1000:
        print(f"[Large Packet] {row['src_ip']} ({domain}) → size {row['packet_size']}")

    elif row["dst_port"] > 50000:
        print(f"[High Port Usage] {row['src_ip']} ({domain}) → port {row['dst_port']}")

    else:
        print(f"[General Anomaly] {row['src_ip']} ({domain})")