from struct import pack
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packets)


def process_packets(packet):
    for layer in packet.layers():
        print(scapy.ls(layer))
        print(layer)
    print(packet.payload)


sniff("wlan0")

#  192.168.29.163  0e:26:dd:36:fc:86      1      42  Unknown vendor
