from scapy.all import sniff, IP, TCP, UDP

def extract_features(packet):
    features = {}

    if IP in packet:
        features["src_ip"] = packet[IP].src
        features["dst_ip"] = packet[IP].dst
        features["packet_size"] = len(packet)

        if TCP in packet:
            features["protocol"] = "TCP"
            features["src_port"] = packet[TCP].sport
            features["dst_port"] = packet[TCP].dport

        elif UDP in packet:
            features["protocol"] = "UDP"
            features["src_port"] = packet[UDP].sport
            features["dst_port"] = packet[UDP].dport

        print(features)

def packet_callback(packet):
    extract_features(packet)

print("Capturing and extracting features...")

sniff(count=10, prn=packet_callback)