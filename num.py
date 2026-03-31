packet = {
    "src_ip": "192.168.1.5",
    "dst_ip": "192.168.1.10",
    "port": 80,
    "packet_rate": 120
}

if packet["packet_rate"] > 100:
    print(" Possible attack detected from", packet["src_ip"])
else:
    print("Normal traffic")