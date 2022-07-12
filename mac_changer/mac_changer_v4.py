import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help=" Please choose an interface")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help=" Please provide a new mac addres")
    (options, args) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface")
    if not options.new_mac:
        parser.error("[-] Please Specify an new mac address")
    return options


def change_mac_address(interface, new_mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface +
                    " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)


def get_current_mac_address(interface):
    result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result))
    if search_result:
        return search_result.group(0)
    return None


options = get_arguments()
change_mac_address(options.interface, options.new_mac)
current_mac_address = get_current_mac_address(options.interface)
print(current_mac_address)
