import subprocess
import optparse


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


options = get_arguments()
change_mac_address(options.interface, options.new_mac)
