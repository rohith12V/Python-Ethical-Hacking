import scapy.all as scapy
import argparse


def performARP(ip):
    request = scapy.ARP()
    request.pdst = ip
    broadcast = scapy.Ether()
    # broad cast address
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout=1)[0]
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip", dest="ipAddress",
                        help=" Please provide an Ip range")
    args = parser.parse_args()
    if args.ipAddress:
        performARP(args.ipAddress)
    else:
        parser.error("Please Provide an IP Address")


parseArgs()
