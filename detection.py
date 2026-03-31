from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time

packet_count = defaultdict(int)
start_time = defaultdict(float)
port_tracker = defaultdict(set)

THRESHOLD = 30
TIME_WINDOW = 5

MY_IP = "10.54.19.183"   # replace if your IP changes

def detect(packet):
    if IP in packet:
        src_ip = packet[IP].src

        # Ignore your own traffic
        if src_ip == MY_IP:
            return

        # Ignore normal web traffic
        if TCP in packet and packet[TCP].dport in [80, 443]:
            return

        # Ignore DNS traffic
        if UDP in packet and packet[UDP].dport == 53:
            return

        current_time = time.time()

        # Initialize start time
        if start_time[src_ip] == 0:
            start_time[src_ip] = current_time

        packet_count[src_ip] += 1

        elapsed_time = current_time - start_time[src_ip]

        # Rate-based detection
        if elapsed_time <= TIME_WINDOW:
            if packet_count[src_ip] > THRESHOLD:
                print(f"[Rate Alert] {src_ip} sent {packet_count[src_ip]} packets in {elapsed_time:.2f} sec")
        else:
            packet_count[src_ip] = 1
            start_time[src_ip] = current_time

        #  Port scan detection
        if TCP in packet:
            dst_port = packet[TCP].dport
            port_tracker[src_ip].add(dst_port)

            if len(port_tracker[src_ip]) > 10:
                print(f"[Port Scan Alert] {src_ip} is accessing multiple ports: {port_tracker[src_ip]}")


def packet_callback(packet):
    detect(packet)


print("Monitoring traffic (rate + port scan detection)...")

try:
    sniff(prn=packet_callback, store=0)
except KeyboardInterrupt:
    print("\nStopping IDS...")
    