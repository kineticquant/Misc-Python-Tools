#MM - Linux Only.
#MM - May have dependency of Python3 functions with input. To use 2.*, change to raw_input.
#MM - 08.02.2019 - Have removed all shell=True because it is a security hazard.
#MM - 08.02.2019 - Updated to pass parameters in CLI using optparse.

import subprocess
import optparse

def arg_retr():
    #Parser object variable is a child of the class/parent OptionParser.
    parser = optparse.OptionParser()
    #2 options the user can enter. The dest is where we will be retrieving the user input.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to have its MAC address changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

def macchange(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#Call the arg_retr function to get the returned values of parser.parse_args().
(options, arguments) = arg_retr()

#Call the macchange function.
change_mac(options.interface, options.new_mac)
