from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("Starting capture...")

sniff(count=10, prn=packet_callback)