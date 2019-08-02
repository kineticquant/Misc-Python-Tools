#MM - Linux only.
#MM - May have dependency of Python3 functions with input. To use 2.*, change to raw_input.
#MM - Reference regex structures at pythex.org.
#MM - 08.02.2019 - Have removed all shell=True because it is a security hazard.
#MM - 08.02.2019 - Updated to pass parameters in CLI using optparse. To use the old version with user input, reference macchanger.py.

import subprocess
import optparse
import re

def arg_retr():
    #Parser object variable is a child of the class/parent OptionParser.
    parser = optparse.OptionParser()
    #2 options the user can enter. The dest is where we will be retrieving the user input.
    parser.add_option("-i", "--interface", dest="interface", help="Interface to have its MAC address changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        #Error handling when interface option is empty.
        parser.error("[-] Please specify an interface. Use --help for additional information.")
    elif not options.new_mac:
        #Error handling when MAC address option is empty.
        parser.error("[-] Please specify a MAC address. Use --help for additional information.")
    return options

def macchange(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#Call the arg_retr function to get the returned values of parser.parse_args().
options = arg_retr()
#Call the macchange function.
change_mac(options.interface, options.new_mac)

change_res = subprocess.check_output(["ifconfig", options.interface])
print(change_res)

#Regex search for the rule set within the variable mentioned.
mac_search_res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", change_res)
#Prints only the first result from the output.
if mac_search_res:
    print(mac_search_res.group(0))
else:
    print("[-] Error: Unable to retrieve a MAC address.")
