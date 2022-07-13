import scapy.all as scapy

request = scapy.ARP()
request.pdst = '192.168.29.0/24'
broadcast = scapy.Ether()
# broad cast address
broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout=1)[0]
for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)
