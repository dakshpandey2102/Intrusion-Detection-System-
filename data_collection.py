from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time

data = []

def extract_features(packet):
    if IP in packet:
        src_ip = packet[IP].src                         
        dst_ip = packet[IP].dst
        packet_size = len(packet)

        protocol = 0
        dst_port = 0

        if TCP in packet:
            protocol = 1
            dst_port = packet[TCP].dport
        elif UDP in packet:
            protocol = 2
            dst_port = packet[UDP].dport

        # CORRECT feature block (includes timestamp)
        features = {
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "packet_size": packet_size,
            "protocol": protocol,
            "dst_port": dst_port,
            "timestamp": time.time()
        }

        data.append(features)

        # Optional: show live packets (remove later for speed)
        print(features)


def packet_callback(packet):
    extract_features(packet)


print("Collecting traffic data... (auto stops after 1000 packets)")

#  Auto-stop to avoid Ctrl+C issue
sniff(prn=packet_callback, store=0, count=1000)

print("\nSaving data...")

df = pd.DataFrame(data)
df.to_csv("traffic.csv", index=False)

print("Data saved to traffic.csv")
