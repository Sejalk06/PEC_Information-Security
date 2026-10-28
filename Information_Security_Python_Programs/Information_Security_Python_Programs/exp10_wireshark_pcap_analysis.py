"""Experiment 10: Analyze a saved .pcap/.pcapng capture using Scapy.
Install dependency with: python -m pip install scapy
Capture traffic using Wireshark first, save it as .pcapng, then run this script.
This script analyzes a capture file offline; it does not start packet capture.
"""

from collections import Counter
from pathlib import Path

try:
    from scapy.all import rdpcap, IP, IPv6, TCP, UDP, ICMP, DNS
except ImportError:
    print("Scapy is required. Install it with: python -m pip install scapy")
    raise SystemExit(1)


def main():
    filename = Path(input("Enter path to .pcap/.pcapng file: ").strip().strip('"'))
    if not filename.is_file():
        print("File not found.")
        return

    try:
        packets = rdpcap(str(filename))
    except Exception as exc:
        print("Could not read capture:", exc)
        return

    protocols = Counter()
    conversations = Counter()
    print(f"Total packets: {len(packets)}")

    for packet in packets:
        src = dst = "Non-IP"
        if IP in packet:
            src, dst = packet[IP].src, packet[IP].dst
        elif IPv6 in packet:
            src, dst = packet[IPv6].src, packet[IPv6].dst

        if DNS in packet:
            protocol = "DNS"
        elif TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        elif IP in packet or IPv6 in packet:
            protocol = "Other IP"
        else:
            protocol = "Other"

        protocols[protocol] += 1
        conversations[(src, dst, protocol)] += 1

    print("\\nProtocol counts:")
    for protocol, count in protocols.most_common():
        print(f"{protocol}: {count}")

    print("\\nTop source -> destination conversations:")
    for (src, dst, protocol), count in conversations.most_common(10):
        print(f"{src} -> {dst} [{protocol}]: {count} packet(s)")

    print("\\nAnalysis complete. Use Wireshark for detailed packet inspection.")


if __name__ == "__main__":
    main()
