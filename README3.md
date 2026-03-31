# Network Intrusion Detection System

**Anomaly-Based Threat Detection using Isolation Forest | Python | Machine Learning | Network Security**

---

## Overview

This project implements a **Network Intrusion Detection System (NIDS)** capable of capturing live network traffic and identifying anomalous or potentially malicious activity. The system combines **rule-based packet analysis** with an **unsupervised machine learning model (Isolation Forest)** to detect deviations from normal traffic behavior without requiring pre-labeled datasets.

The project demonstrates practical application of cybersecurity principles, network programming, and machine learning in a unified pipeline — from raw packet capture to automated threat detection.

> **Disclaimer:** This tool is developed strictly for educational purposes and authorized network security research. Deployment on any network requires explicit permission from the network owner.

---

## Key Features

- **Real-Time Packet Capture** — Intercepts and processes live network traffic using Scapy with support for TCP, UDP, and ICMP protocols
- **Automated Feature Extraction** — Parses raw packets into structured numerical features including source/destination IPs, ports, protocol type, and packet size
- **Unsupervised Anomaly Detection** — Applies Isolation Forest to identify outliers in traffic patterns without dependency on labeled training data
- **Traffic Logging** — Persists captured traffic data to CSV for offline analysis and model retraining
- **Alert Generation** — Flags and logs suspicious packets in real time upon anomaly detection

---

## System Architecture

```
Live Network Traffic
        |
        v
  Packet Capture Layer        [capture.py]
  (Scapy - raw socket capture)
        |
        v
  Data Collection & Storage   [data_collection.py]
  (Pandas DataFrame / CSV)
        |
        v
  Feature Extraction          [feature_extraction.py]
  (Protocol, Port, Size, IP)
        |
        v
  Isolation Forest Model      [model.py]
  (Scikit-learn - unsupervised)
        |
        v
  Anomaly Detection Engine    [detection.py]
        |
        v
  Alert Output / Threat Log
```

---

## Project Structure

```
network-ids/
|
|-- capture.py                # Real-time packet capture via Scapy
|-- data_collection.py        # Traffic storage and data management
|-- feature_extraction.py     # Feature parsing from raw packet data
|-- model.py                  # Isolation Forest model training and serialization
|-- detection.py              # Live anomaly detection and alert engine
|
|-- data/
|   |-- traffic_log.csv       # Auto-generated traffic dataset
|
|-- requirements.txt
|-- README.md
```

---

## Technologies and Libraries

| Component            | Technology                          |
|----------------------|-------------------------------------|
| Language             | Python 3.8+                         |
| Packet Capture       | Scapy                               |
| Data Processing      | Pandas, NumPy                       |
| Machine Learning     | Scikit-learn (Isolation Forest)     |
| Anomaly Detection    | Unsupervised Learning               |
| Storage Format       | CSV (extensible to SQL/NoSQL)       |

---

## Machine Learning Approach

### Algorithm: Isolation Forest

Isolation Forest is an ensemble-based, unsupervised anomaly detection algorithm particularly effective for high-dimensional data with low anomaly contamination rates.

**Core principle:** Anomalous data points are easier to isolate via random recursive partitioning — they require fewer splits to be separated from normal observations. This translates to a lower average path length and a higher anomaly score.

**Why Isolation Forest for network traffic:**
- Does not require labeled attack data for training
- Computationally efficient for real-time traffic streams
- Robust to irrelevant features and high-dimensional feature spaces
- Effective at detecting novel, previously unseen attack patterns

```python
from sklearn.ensemble import IsolationForest

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,   # Expected anomaly rate (~5%)
    random_state=42
)

model.fit(X_train)
predictions = model.predict(X_test)
# Output: +1 = Normal traffic | -1 = Anomalous / Suspicious
```

---

## Extracted Feature Set

| Feature        | Description                              | Type        |
|----------------|------------------------------------------|-------------|
| `src_ip`       | Source IP address                        | Categorical |
| `dst_ip`       | Destination IP address                   | Categorical |
| `src_port`     | Source port number                       | Numerical   |
| `dst_port`     | Destination port number                  | Numerical   |
| `protocol`     | Network protocol (TCP / UDP / ICMP)      | Categorical |
| `packet_size`  | Packet length in bytes                   | Numerical   |
| `timestamp`    | Unix timestamp of packet capture         | Numerical   |

---

## Installation and Usage

### Prerequisites

- Python 3.8 or higher
- Root / Administrator privileges (required for raw socket access via Scapy)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/network-ids.git
cd network-ids
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

```
scapy
pandas
scikit-learn
numpy
```

### Step 3 — Start Packet Capture

```bash
sudo python capture.py
```

### Step 4 — Run Anomaly Detection

```bash
sudo python detection.py
```

---

## Sample Output

```
[INFO]  Starting packet capture on interface eth0...
[INFO]  Packet #1024 | SRC: 192.168.1.5:54231 -> DST: 10.0.0.1:22  | Protocol: TCP  | Size: 64B
[INFO]  Packet #1025 | SRC: 192.168.1.5:54232 -> DST: 10.0.0.1:23  | Protocol: TCP  | Size: 64B
[INFO]  Packet #1026 | SRC: 192.168.1.5:54233 -> DST: 10.0.0.1:443 | Protocol: TCP  | Size: 128B
[ALERT] Anomaly detected  | Packet #1025 flagged as suspicious
[ALERT] Possible indicator: Sequential port scan pattern identified
[INFO]  Alert logged to threat_log.csv
```

---

## Roadmap

| Feature                                              | Status  |
|------------------------------------------------------|---------|
| Real-time monitoring dashboard (Streamlit / Plotly)  | Planned |
| PCAP file ingestion for offline analysis             | Planned |
| Deep learning model (Autoencoder-based detection)    | Planned |
| Multi-class attack classification (DoS, Port Scan, MITM) | Planned |
| SIEM integration (Splunk / Elastic Stack)            | Planned |
| Email and SMS alert notifications                    | Planned |

---

## Security and Ethical Use

This project is intended solely for:
- Academic research and learning
- Authorized penetration testing environments
- Personal or lab network monitoring with explicit consent

Unauthorized use of packet capture tools may violate applicable laws including the Computer Fraud and Abuse Act (CFAA) and equivalent legislation in other jurisdictions.

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes with clear messages (`git commit -m "Add: feature description"`)
4. Push to your branch (`git push origin feature/your-feature`)
5. Open a Pull Request with a detailed description of changes


---

*If you find this project useful, consider leaving a star on the repository.*
